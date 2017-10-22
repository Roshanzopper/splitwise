from django.utils import timezone

from .models import SplitUser, ExpenseGroup, ExpenseGroupDetails
from django.core import serializers
from rest_framework import serializers


class SplitUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SplitUser
        #fields = '__all__'
        fields = ('id', 'username','password','emailid','createdon')
        extra_kwargs = {'password': {'write_only': True}}

    # def get_serializer_context(self):
    #     """
    #     Optionally restricts the returned purchases to a given user,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     # queryset = SplitUser.objects.all()
    #     import pdb;
    #     pdb.set_trace()
    #     # username = self.request.query_params.get('username', None)
    #     # if username is not None:
    #     #     queryset = queryset.filter(splituser__username=username)
    #     # return queryset
    #     # username = self.kwargs['username']
    #     # return SplitUser.objects.filter(purchaser__username=username)
    #     # def get_serializer_context(self):
    #     return {"customer_id": self.kwargs['username']}


class ExpenseGroupDetailsSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField("username",read_only=True, source="UserID")
    user = SplitUserSerializer(source="UserID" ,read_only=True)
    # userid = SplitUserSerializer()
    expgrpdetid = serializers.IntegerField(write_only=True)
    class Meta:
        model = ExpenseGroupDetails
        fields = ["UserID","user","username","ExpenseGroupID","id","expgrpdetid","IsDelete","DeletedOn"]


class ExpenseGroupSerializer(serializers.ModelSerializer):
    details = ExpenseGroupDetailsSerializer(many=True,write_only=True)
    expensegroupdetails = ExpenseGroupDetailsSerializer(many=True, read_only=True,source="ExpenseGroupID")
    class Meta:
        model = ExpenseGroup
        fields = [ "expensegroupdetails","details","ExpenseGroupName","id"]

    def create(self, validated_data):
       print(validated_data)
       expensegroup = validated_data.pop("details")
       expense_group = super().create(validated_data) #ExpenseGroup.objects.create(**validated_data)
       for exdetais in expensegroup:
           exdetais["ExpenseGroupID"] = expense_group
           ExpenseGroupDetails.objects.create(**exdetais)
       return expense_group

    def update(self, instance, validated_data):
        print("validated data :")
        print(validated_data)
        expensegroup = validated_data.pop("details")
        instance.ExpenseGroupName = validated_data.get('ExpenseGroupName', instance.ExpenseGroupName)
        instance.save()

        # Delete any detail not included in the request
        # exg1 = expensegroup.objects.filter(expgrpdetid__isnull=False)
        expgrpdet_ids = [item.get('expgrpdetid') for item in expensegroup]
        expgrpdet_ids = filter(None,expgrpdet_ids)
        for expd in ExpenseGroupDetails.objects.all():
            if expd.id not in expgrpdet_ids:
                expd.IsDelete = True
                expd.DeletedOn = timezone.now()
                expd.DeletedBy = instance.CreatedBy
                expd.save()
                # expd.delete()


        # Create or update owner
        for exgrpd in expensegroup:
            print(exgrpd)
            try:
                expObj = ExpenseGroupDetails.objects.get(pk=exgrpd['expgrpdetid'])
            except Exception:
                expObj = None
            # import pdb;pdb.set_trace()
            # print(expobj)
            if expObj:
                expObj.UserID = exgrpd['UserID']
                expObj.save()
            else:
                exgrpd["ExpenseGroupID"] = instance
                ExpenseGroupDetails.objects.create(**exgrpd)

        return validated_data



from MainApp.serializers import SplitUserSerializer,ExpenseGroupSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import  SplitUser,ExpenseGroup, ExpenseGroupDetails
from django.views import generic
from django.db.models import Prefetch
from rest_framework.decorators import api_view

class SplitUserList(viewsets.ModelViewSet):
    queryset = SplitUser.objects.all()
    serializer_class = SplitUserSerializer


class ExpenseGroupList(viewsets.ModelViewSet):
    queryset = ExpenseGroup.objects.all()
    serializer_class = ExpenseGroupSerializer

    def get_queryset(self):
        return self.queryset.prefetch_related('ExpenseGroupID')


@api_view(['POST'])
def login(request):
    username1 = request.data.get("username")
    password1 = request.data.get("password")
    if request.method == 'POST':
        # password = request.data.get("password")
        # try:
        # import pdb; pdb.set_trace()
        snippets = SplitUser.objects.filter(username=username1,password=password1)
        serializer = SplitUserSerializer(snippets, many=True)
        return Response(serializer.data)
        # except Exception:
        #     return Response(status=status.HTTP_404_NOT_FOUND)

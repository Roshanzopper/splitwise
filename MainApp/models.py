import datetime
from django.db import models
from django.utils import timezone

Expense_Type_List = [('Internet', 'Internet'),
                          ('Shopping', 'Shopping'),
                          ('Rent', 'Rent'),
                          ('Bills', 'Bills')]

class SplitUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    emailid = models.CharField(max_length=50)
    createdon = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('createdon',)


class ExpenseGroup(models.Model):
    ExpenseGroup_Type_List = [('Apartment', 'Apartment'),
                              ('House', 'House'),
                              ('Trip', 'Trip'),
                              ('Other', 'Other')]

    ExpenseGroupName = models.CharField(max_length=250)
    SimplifyGroupDebts = models.BooleanField(default=False)
    ExpenseGroupType = models.CharField( choices=ExpenseGroup_Type_List, default='Apartment', max_length=50)
    CreatedBy = models.ForeignKey(SplitUser,null=True, related_name='ExpenseGroup_CreatedBy')
    CreatedOn =models.DateTimeField(auto_now_add=True)
    IsDelete = models.BooleanField(default=False)
    DeletedOn = models.DateTimeField(null=True, blank=True)
    DeletedBy = models.ForeignKey(SplitUser,null=True, related_name='ExpenseGroup_DeletedBy')


class ExpenseGroupDetails(models.Model):
    ExpenseGroupID = models.ForeignKey(ExpenseGroup, null=True, related_name='ExpenseGroupID')
    UserID = models.ForeignKey(SplitUser,  null=True, related_name='UserID')
    CreatedOn =models.DateTimeField(auto_now_add=True)
    IsDelete = models.BooleanField(default=False)
    DeletedBy = models.ForeignKey(SplitUser,  null=True, related_name='ExpenseGroupDetails_DeletedBy')
    DeletedOn = models.DateTimeField(null=True, blank=True)


class Expense(models.Model):
    Title = models.CharField(max_length=250)
    Amount = models.DecimalField(max_digits=10,decimal_places=10)
    Notes = models.CharField(max_length=500,  null=True)
    Date = models.DateTimeField(default=timezone.now)
    PaidByUserID = models.ForeignKey(SplitUser, on_delete=models.CASCADE, null=True, related_name='Expense_PaidByUserID')
    ExpenseType = models.CharField(choices=Expense_Type_List,default='Shopping', max_length=50)
    CreatedBy = models.ForeignKey(SplitUser, on_delete=models.CASCADE, null=True, related_name='Expense_CreatedBy')
    CreatedOn = models.DateTimeField(auto_now_add=True)
    IsDelete = models.BooleanField(default=False)
    DeletedBy = models.ForeignKey(SplitUser, on_delete=models.CASCADE, null=True, related_name='Expense_DeletedBy')
    DeletedOn = models.DateTimeField(null=True, blank=True)
    ModifiedBy = models.ForeignKey(SplitUser, on_delete=models.CASCADE, null=True, related_name='Expense_ModifiedBy')
    ModifiedOn = models.DateTimeField(null=True, blank=True)
#
#
class ExpenseDetails(models.Model):
    ExpenseID = models.ForeignKey(Expense, on_delete=models.CASCADE, null=True, related_name='ExpenseDetails_ExpenseID')
    ExpenseGroupDetailsID = models.ForeignKey(ExpenseGroupDetails, on_delete=models.CASCADE, null=True, related_name='ExpenseDetails_ExpenseGroupDetailsID')
    ShareAmount = models.DecimalField(max_digits=10,decimal_places=10)
    IsDelete = models.BooleanField(default=False)
    DeletedBy = models.ForeignKey(SplitUser, on_delete=models.CASCADE, null=True, related_name='ExpenseDetails_DeletedBy')
    DeletedOn = models.DateTimeField(null=True, blank=True)
    CreatedBy = models.ForeignKey(SplitUser, on_delete=models.CASCADE, null=True, related_name='ExpenseDetails_CreatedBy')
    CreatedOn = models.DateTimeField(auto_now_add=True)

#
# class ExpenseNotes(models.Model):
#     ExpenseID = models.ForeignKey(Expense, on_delete=models.CASCADE, null=True, related_name='ExpenseNotes_ExpenseID')
#     Notes = models.CharField(max_length=500)
#     CreatedBy = models.ForeignKey(SplitUser, on_delete=models.CASCADE, null=True, related_name='ExpenseNotes_CreatedBy')
#     CreatedOn = models.DateTimeField(auto_now_add=True)


# class Settlement(models.Model):
#     SettleBy = models.ForeignKey(SplitUser, on_delete=models.CASCADE, null=True, related_name='Settlement_SettleBy')
#     CreatedBy = models.ForeignKey(SplitUser, on_delete=models.CASCADE, null=True, related_name='Settlement_CreatedBy')
#     CreatedOn = models.DateTimeField(auto_now_add=True)
#
#
# class SettlementDetails(models.Model):
#     SettlementID =  models.ForeignKey(Settlement, on_delete=models.CASCADE)
#     SettleOfID =   models.ForeignKey(SplitUser, on_delete=models.CASCADE)
#     Amount = models.DecimalField(max_digits=10,decimal_places=10)

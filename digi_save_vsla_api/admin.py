from django.contrib import admin
from .models import *
from rest_framework.authtoken.models import Token

# Token auth
admin.site.register(Token)

# Register your models here.
admin.site.register(GroupProfile)
admin.site.register(ConstitutionTable)
admin.site.register(Users)
admin.site.register(GroupMembers)
admin.site.register(CycleSchedules)
admin.site.register(Positions)
admin.site.register(AssignedPositions)
admin.site.register(GroupForm)
admin.site.register(SavingsAccount)
admin.site.register(GroupFees)
admin.site.register(CycleMeeting)
admin.site.register(Meeting)
admin.site.register(MemberShares)
admin.site.register(WelfareAccount)
admin.site.register(ActiveCycleMeeting)
admin.site.register(Shares)
admin.site.register(Social)
admin.site.register(LoanApplications)
admin.site.register(SocialFundApplications)
admin.site.register(CycleStartMeeting)
admin.site.register(PaymentInfo)
admin.site.register(Fines)
admin.site.register(GroupCycleStatus)
admin.site.register(Loans)
admin.site.register(LoanDisbursement)
admin.site.register(LoanPayments)
admin.site.register(ShareOut)
admin.site.register(ReversedTransactions)
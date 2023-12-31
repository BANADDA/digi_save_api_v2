# serializers.py
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import *


class UserProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfiles
        fields = '__all__'  
class GroupFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupForm
        fields = '__all__'

class SavingsAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsAccount
        fields = '__all__'
        
class AssignedPositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignedPositions
        fields = '__all__'
        
class ConstitutionTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstitutionTable
        fields = '__all__'
        
class CycleSchedulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CycleSchedules
        fields = '__all__'
        
class GroupMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMembers
        fields = '__all__'
        
class GroupProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupProfile
        fields = '__all__'
        
class PositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = '__all__'
        
class UsersSerializer(serializers.ModelSerializer):
    """override create method to change the password into hash."""
    def create(self, validated_data):
            validated_data["unique_code"] = make_password(validated_data.get("unique_code"))
            return super(UsersSerializer, self).create(validated_data)

    class Meta:
        model = Users
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    phone = serializers.CharField()  # Modify based on your field types
    unique_code = serializers.CharField()  # Modify based on your field types
    class Meta:
            model = Users
            fields = ['phone','unique_code']

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'fname', 'lname')

        
class GroupFeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupFees
        fields = '__all__'
        
class CycleMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CycleMeeting
        fields = '__all__'
        
class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'
        
class MemberSharesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberShares
        fields = '__all__'
        
class WelfareAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = WelfareAccount
        fields = '__all__'
        
class ActiveCycleMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveCycleMeeting
        fields = '__all__'
        
class SharesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shares
        fields = '__all__'
        
class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'
        
class LoanApplicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanApplications
        fields = '__all__'
        
class SocialFundApplicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialFundApplications
        fields = '__all__'
        
class CycleStartMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CycleStartMeeting
        fields = '__all__'
        
class PaymentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentInfo
        fields = '__all__'
        
class FinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fines
        fields = '__all__'
        
class GroupCycleStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupCycleStatus
        fields = '__all__'
        
class LoansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loans
        fields = '__all__'
        
class LoanDisbursementSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanDisbursement
        fields = '__all__'
        
class LoanPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanPayments
        fields = '__all__'
        
class ShareOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareOut
        fields = '__all__'
        
class ReversedTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReversedTransactions
        fields = '__all__'
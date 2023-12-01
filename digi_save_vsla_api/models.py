from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.db import models
import uuid
    
class Country(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=255,default=None)
    
class District(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=255,default=None)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
class County(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=255,default=None)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    
class Subcounty(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=255,default=None)
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    
class Village(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=255,default=None)
    sub_country = models.ForeignKey(Subcounty, on_delete=models.CASCADE)

class Users(AbstractUser):
    unique_code = models.CharField(max_length=100)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15, unique=True)
    sex = models.CharField(max_length=10)
    

class UserProfiles(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True, unique=True)
    user_id = models.OneToOneField(Users, on_delete=models.CASCADE, blank=True, unique=True)
    
    date_of_birth = models.DateField(auto_now=True, blank=True, null=True)
    image = models.TextField(default=None, blank=True, null=True)
    
    country = models.ForeignKey(Country, on_delete=models.CASCADE,  blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE,  blank=True, null=True)
    subCounty = models.ForeignKey(Subcounty, on_delete=models.CASCADE,  blank=True, null=True)
    village = models.ForeignKey(Village, on_delete=models.CASCADE,  blank=True, null=True)

    number_of_dependents = models.IntegerField(default=0)
    family_information = models.TextField()
    next_of_kin_name = models.CharField(max_length=100)
    next_of_kin_has_phone_number = models.BooleanField(default=False)
    next_of_kin_phone_number = models.CharField(max_length=15, default=None, blank=True, null=True)
    pwd_type = models.CharField(max_length=20, default=None, blank=True, null=True)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.unique_code:
            # Hash the unique_code field before saving
            self.unique_code = make_password(self.unique_code)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.phone

class GroupProfile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True, unique=True)
    groupName = models.CharField(max_length=255, default=None, blank=True, null=True)
    countryOfOrigin = models.CharField(max_length=255, default=None, blank=True, null=True)
    meetingLocation = models.CharField(max_length=255, default=None, blank=True, null=True)
    groupStatus = models.CharField(max_length=255, default=None, blank=True, null=True)
    groupLogoPath = models.CharField(max_length=255, default=None, blank=True, null=True)
    partnerID = models.CharField(max_length=255, default=None, blank=True, null=True)
    workingWithPartner = models.CharField(max_length=255, default=None, blank=True, null=True)
    isWorkingWithPartner = models.IntegerField(default=None, blank=True, null=True)
    numberOfCycles = models.CharField(max_length=255, default=None, blank=True, null=True)
    numberOfMeetings = models.CharField(max_length=255, default=None, blank=True, null=True)
    loanFund = models.CharField(max_length=255, default=None, blank=True, null=True)
    socialFund = models.CharField(max_length=255, default=None, blank=True, null=True)

    def __str__(self):
        return self.groupName
    
class ConstitutionTable(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True, unique=True)
    group_id = models.ForeignKey(GroupProfile, on_delete=models.CASCADE)
    hasConstitution = models.IntegerField(default=None, blank=True, null=True)
    constitutionFiles = models.BinaryField(default=None, blank=True, null=True)
    usesGroupShares = models.BooleanField(default=None, blank=True, null=True)
    shareValue = models.FloatField(default=None, blank=True, null=True)
    maxSharesPerMember = models.IntegerField(default=None, blank=True, null=True)
    minSharesRequired = models.IntegerField(default=None, blank=True, null=True)
    frequencyOfContributions = models.CharField(max_length=255, default=None, blank=True, null=True)
    offersLoans = models.BooleanField(default=None, blank=True, null=True)
    maxLoanAmount = models.FloatField(default=None, blank=True, null=True)
    interestRate = models.FloatField(default=None, blank=True, null=True)
    interestMethod = models.CharField(max_length=255, default=None, blank=True, null=True)
    loanTerms = models.CharField(max_length=255, default=None, blank=True, null=True)
    registrationFee = models.CharField(max_length=255, default=None, blank=True, null=True)
    selectedCollateralRequirements = models.CharField(max_length=255, default=None, blank=True, null=True)

    def __str__(self):
        return f"ConstitutionTable for Group ID: {self.group_id}  - Has Constitution: {self.hasConstitution}"


class GroupMembers(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True, unique=True)
    user_id = models.ForeignKey(UserProfiles, on_delete=models.CASCADE)
    group_id = models.ForeignKey(GroupProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"GroupMember {self.user_id} for Group ID: {self.group_id}"

class CycleSchedules(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True, unique=True)
    group_id = models.ForeignKey(GroupProfile, on_delete=models.CASCADE)
    meeting_duration = models.TextField()
    number_of_meetings = models.IntegerField()
    meeting_frequency = models.TextField()
    day_of_week = models.TextField()
    start_date = models.DateField(auto_now=True, blank=True)
    share_out_date = models.DateField(auto_now=True, blank=True)
    
    def __str__(self):
        return f"CycleSchedules for Group ID: {self.group_id}"
    

class Positions(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True, unique=True)
    name = models.TextField()
    
    def __str__(self):
        return self.name
    
class AssignedPositions(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True, unique=True)
    position_name = models.TextField(default=None, blank=True, null=True)
    member_id = models.ForeignKey(UserProfiles, on_delete=models.CASCADE)
    group_id = models.ForeignKey(GroupProfile, on_delete=models.CASCADE)
    
    def __str__(self):
     return f"Assigned position for Group Id{self.group_id}"


class GroupForm(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True, unique=True)
    group_profile_id = models.IntegerField(default=None, blank=True, null=True)
    group_id = models.ForeignKey(GroupProfile, on_delete=models.CASCADE)
    logged_in_users_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    constitution_id = models.ForeignKey(ConstitutionTable, on_delete=models.CASCADE)
    cycle_schedule_id = models.ForeignKey(CycleSchedules, on_delete=models.CASCADE)
    group_member_id = models.ForeignKey(UserProfiles, on_delete=models.CASCADE)
    assigned_position_id = models.ForeignKey(Positions, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Group Id: {self.group_id}"
    
class SavingsAccount(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True, unique=True)
    logged_in_users_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateField(datetime.now().date())
    purpose = models.TextField()
    amount = models.FloatField()
    
    group = models.ForeignKey(GroupForm, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.group)

class GroupFees(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True, unique=True)
    member = models.ForeignKey(UserProfiles, on_delete=models.CASCADE)
    group_id = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    registration_fee = models.FloatField()
    
    def __str__(self):
        return str(self.member)

class CycleMeeting(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True, unique=True)
    date = models.DateField(auto_now=True, blank=True)
    time = models.TextField(default=None, blank=True, null=True)
    endTime = models.TextField(default=None, blank=True, null=True)
    location = models.TextField(default=None, blank=True, null=True)
    facilitator = models.TextField(default=None, blank=True, null=True)
    meetingPurpose = models.TextField(default=None, blank=True, null=True)
    latitude = models.FloatField(default=None, blank=True, null=True)
    longitude = models.FloatField(default=None, blank=True, null=True)
    address = models.TextField(default=None, blank=True, null=True)
    objectives = models.TextField(default=None, blank=True, null=True)
    attendanceData = models.TextField(default=None, blank=True, null=True)
    representativeData = models.TextField(default=None, blank=True, null=True)
    proposals = models.TextField(default=None, blank=True, null=True)
    totalLoanFund = models.IntegerField(default=None, blank=True, null=True)
    totalSocialFund = models.IntegerField(default=None, blank=True, null=True)
    socialFundContributions = models.TextField(default=None, blank=True, null=True)
    sharePurchases = models.TextField(default=None, blank=True, null=True)
    
    group_id = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.group_id)
    
class Meeting(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True, unique=True)
    date = models.DateField(auto_now=True, blank=True)
    time = models.TextField(default=None, blank=True, null=True)
    endTime = models.TextField(default=None, blank=True, null=True)
    location = models.TextField()
    facilitator = models.TextField()
    meetingPurpose = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField()
    objectives = models.TextField()
    attendanceData = models.TextField()
    representativeData = models.TextField()
    proposals = models.TextField()
    socialFundContributions = models.TextField()
    sharePurchases = models.TextField()
    totalLoanFund = models.IntegerField()
    totalSocialFund = models.IntegerField()
    
    group_id = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    cycle_id = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.group_id)
    
    
class MemberShares(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True, unique=True)
    logged_in_users_id = models.ForeignKey(Users,  on_delete=models.CASCADE, related_name='logged_in_users_id')
    date = models.TextField()
    sharePurchases = models.TextField()
    
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    users = models.ForeignKey(UserProfiles,  on_delete=models.CASCADE, related_name='group_member')
    group_id = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    cycle_id = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.group_id)
    
class WelfareAccount(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True, unique=True)
    logged_in_users_id = models.ForeignKey(Users,  on_delete=models.CASCADE)
    amount = models.FloatField()
    group_id = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    meeting_id = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    cycle_id = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.group_id)

class ActiveCycleMeeting(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True, unique=True)
    
    group_id = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    cycleMeetingID = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.group_id)

class Shares(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True, unique=True)
    sharePurchases = models.TextField()
    
    meetingId = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    cycle_id = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE)
    group_id = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.group_id)


class Social(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True, unique=True)
    socialFund = models.TextField()
    group_id = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    meetingId = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.meetingId)

class LoanApplications(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True, unique=True)
    group_id = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    cycle_id = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE)
    meeting_id = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    submission_date = models.DateField(auto_now=True, blank=True)
    loan_applicant = models.TextField()
    group_member = models.ForeignKey(UserProfiles, on_delete=models.CASCADE)
    amount_needed = models.FloatField()
    loan_purpose = models.TextField()
    repayment_date = models.DateField(auto_now=True, blank=True)
    
    def __str__(self):
        return str(self.group_id)


class SocialFundApplications(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True, unique=True)
    group_id = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    cycle_id = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE)
    meeting_id = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    submission_date = models.DateField(auto_now=True, blank=True)
    applicant = models.TextField()
    group_member = models.IntegerField(default=None, blank=True, null=True)
    amount_needed = models.FloatField()
    social_purpose = models.TextField()
    repayment_date = models.DateField(auto_now=True, blank=True)
    
    def __str__(self):
        return str(self.group_id)


class CycleStartMeeting(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True, unique=True)
    group = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    date = models.TextField()
    time = models.TextField()
    location = models.TextField()
    facilitator = models.TextField()
    meeting_purpose = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField()
    objectives = models.TextField()
    attendance_data = models.TextField()
    representative_data = models.TextField()
    proposals = models.TextField()
    end_time = models.TextField()
    assigned_funds = models.TextField()
    social_fund_bag = models.TextField()
    social_fund_contributions = models.TextField()
    share_purchases = models.TextField()


class PaymentInfo(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True, unique=True)
    group = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    cycle_id = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE)
    meeting_id = models.IntegerField(default=None, blank=True, null=True)
    member_id = models.ForeignKey(UserProfiles, on_delete=models.CASCADE)
    payment_amount = models.FloatField()
    payment_date = models.TextField()
    
    def __str__(self):
        return str(self.group)
    

class Fines(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True, unique=True)
    memberId = models.ForeignKey(UserProfiles, on_delete=models.CASCADE)
    amount = models.IntegerField()
    reason = models.TextField()
    groupId = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    cycleId = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE)
    meetingId = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    savingsAccountId = models.ForeignKey(SavingsAccount, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.groupId)


class GroupCycleStatus(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True, unique=True)
    group = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    cycleId = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE)
    is_cycle_started = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.group)

class Loans(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True, unique=True)
    member = models.ForeignKey(UserProfiles, on_delete=models.CASCADE)
    loan_applicant = models.TextField()
    group = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    loan_purpose = models.TextField()
    loan_amount = models.FloatField()
    interest_rate = models.FloatField()
    start_date = models.TextField()
    end_date = models.TextField()
    status = models.TextField()

    def __str__(self):
        return str(self.group)


class LoanDisbursement(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True, unique=True)
    member = models.ForeignKey(UserProfiles, on_delete=models.CASCADE)
    group = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    cycleId = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE)
    loan = models.IntegerField(default=None, blank=True, null=True)
    disbursement_amount = models.FloatField()
    disbursement_date = models.DateField()
    
    def __str__(self):
        return str(self.group)


class LoanPayments(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True, unique=True)
    member = models.ForeignKey(UserProfiles, on_delete=models.CASCADE)
    group = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    loan = models.IntegerField(default=None, blank=True, null=True)
    payment_amount = models.FloatField()
    payment_date = models.TextField()

    def __str__(self):
        return str(self.group)


class ShareOut(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True, unique=True)
    group = models.ForeignKey(GroupForm,on_delete=models.CASCADE)
    cycleId = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE)
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    share_value = models.FloatField()

    def __str__(self):
        return str(self.group)


class ReversedTransactions(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True, unique=True)
    group = models.ForeignKey(GroupForm,on_delete=models.CASCADE)
    savings_account = models.IntegerField(default=None, blank=True, null=True)
    logged_in_users = models.ForeignKey(Users, on_delete=models.CASCADE)
    reversed_amount = models.FloatField()
    date = models.DateField(auto_now=True, blank=True)
    purpose = models.TextField()
    reversed_data = models.TextField()
    
    def __str__(self):
        return str(self.group)

from django.db import models

# Create your models here.
class GroupProfile(models.Model):
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
    group = models.ForeignKey(GroupProfile, on_delete=models.CASCADE, db_column='group', default=None, null=True)
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
        return f"ConstitutionTable for Group ID: {self.group}  - Has Constitution: {self.hasConstitution}"

class Users(models.Model):
    unique_code = models.TextField()
    fname = models.TextField()
    lname = models.TextField()
    email = models.TextField(default=None, blank=True, null=True)
    phone = models.TextField()
    sex = models.TextField()
    country = models.TextField()
    date_of_birth = models.TextField()
    image = models.TextField(default=None, blank=True, null=True)
    district = models.TextField()
    subCounty = models.TextField()
    village = models.TextField()
    number_of_dependents = models.TextField()
    family_information = models.TextField()
    next_of_kin_name = models.TextField()
    next_of_kin_has_phone_number = models.IntegerField(default=None, blank=True, null=True)
    next_of_kin_phone_number = models.TextField(default=None, blank=True, null=True)
    pwd_type = models.TextField(default=None, blank=True, null=True)
    
    def __str__(self):
        return f"{self.fname} {self.lname}"

class GroupMembers(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE,db_column='user' , default=None, null=True)
    group = models.ForeignKey(GroupProfile, on_delete=models.CASCADE, db_column='group', default=None, null=True)

    def __str__(self):
        return f"GroupMember {self.user_id} for Group ID: {self.group}"

class CycleSchedules(models.Model):
    group = models.ForeignKey(GroupProfile, on_delete=models.CASCADE, db_column='group', default=None, null=True)
    meeting_duration = models.TextField()
    number_of_meetings = models.IntegerField()
    meeting_frequency = models.TextField()
    day_of_week = models.TextField()
    start_date = models.TextField()
    share_out_date = models.TextField()
    
    def __str__(self):
        return f"CycleSchedules for Group ID: {self.group}"
    

class Positions(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return self.name
    
class AssignedPositions(models.Model):
    position = models.IntegerField(default=None, blank=True, null=True)
    member = models.ForeignKey(GroupMembers, on_delete=models.CASCADE, db_column='member', default=None, null=True)
    group = models.ForeignKey(GroupProfile, on_delete=models.CASCADE, db_column='group', default=None, null=True)
    
    def __str__(self):
        return self.position

class GroupForm(models.Model):
    group = models.ForeignKey(GroupProfile, on_delete=models.CASCADE, db_column='group', default=None, null=True)
    logged_in_users = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='logged_in_users', default=None, null=True)
    constitution = models.ForeignKey(ConstitutionTable, on_delete=models.CASCADE, db_column='constitution', default=None, null=True)
    cycle_schedule = models.ForeignKey(CycleSchedules, on_delete=models.CASCADE, db_column='cycle_schedule', default=None, null=True)
    group_member = models.ForeignKey(GroupMembers, on_delete=models.CASCADE, db_column='group_member', default=None, null=True)
    assigned_position = models.ForeignKey(AssignedPositions, on_delete=models.CASCADE, db_column='assigned_position', default=None, null=True)
    
    def __str__(self):
        return self.group
    
class SavingsAccount(models.Model):
    logged_in_users = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='logged_in_users', default=None, null=True)
    date = models.TextField()
    purpose = models.TextField()
    amount = models.FloatField()
    
    group = models.ForeignKey(GroupForm, on_delete=models.CASCADE, db_column='group', default=None, null=True)

    def __str__(self):
        return self.group

class GroupFees(models.Model):
    member = models.ForeignKey(GroupMembers, on_delete=models.CASCADE, db_column='member', default=None, null=True)
    group = models.ForeignKey(GroupForm, on_delete=models.CASCADE, db_column='group', blank=True, default=None, null=True)
    registration_fee = models.FloatField()
    
    def __str__(self):
        return self.member

class CycleMeeting(models.Model):
    date = models.TextField()
    time = models.TextField()
    endTime = models.TextField()
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
    totalLoanFund = models.IntegerField()
    totalSocialFund = models.IntegerField()
    socialFundContributions = models.TextField()
    sharePurchases = models.TextField()
    
    group = models.ForeignKey(GroupForm, on_delete=models.CASCADE, db_column='group', default=None, null=True)
    
    def __str__(self):
        return self.group
    
class Meeting(models.Model):
    date = models.TextField()
    time = models.TextField()
    endTime = models.TextField()
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
    
    group = models.ForeignKey(GroupForm, on_delete=models.CASCADE, db_column='group', default=None, null=True)
    cycle = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE,  db_column='cycle', default=None, null=True)
    
    def __str__(self):
        return self.group
    
    
class MemberShares(models.Model):
    logged_in_users = models.IntegerField()
    date = models.TextField()
    sharePurchases = models.TextField()
    
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, db_column='meeting', default=None, null=True)
    users = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='users', default=None, null=True)
    group = models.ForeignKey(GroupForm, on_delete=models.CASCADE, db_column='group', default=None, null=True)
    cycle = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE,  db_column='cycle', default=None, null=True)
    
    def __str__(self):
        return self.group
    
class WelfareAccount(models.Model):
    logged_in_users = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='logged_in_users', default=None, null=True)
    amount = models.FloatField()
    group = models.ForeignKey(GroupForm, on_delete=models.CASCADE, db_column='group', default=None, null=True)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, db_column='meeting', default=None, null=True)
    cycle = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE,  db_column='cycle', default=None, null=True)
    
    def __str__(self):
        return self.group

class ActiveCycleMeeting(models.Model):
    
    group = models.ForeignKey(GroupProfile, on_delete=models.CASCADE, db_column='group', default=None,  null=True)
    cycleMeetingID = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE, db_column='cycleMeetingID', default=None, null=True)
    
    def __str__(self):
        return self.group

class Shares(models.Model):
    sharePurchases = models.TextField()
    
    meetingId = models.ForeignKey(Meeting, on_delete=models.CASCADE, db_column='meetingId', default=None, null=True)
    cycle = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE,  db_column='cycle', default=None, null=True)
    group = models.ForeignKey(GroupForm, on_delete=models.CASCADE, db_column='group', default=None, null=True)
    
    def __str__(self):
        return self.group


class Social(models.Model):
    socialFund = models.TextField()
    
    meetingId = models.ForeignKey(Meeting, on_delete=models.CASCADE, db_column='meetingId', default=None, null=True)
    
    def __str__(self):
        return self.meetingId

class GroupLink(models.Model):
    group = models.ForeignKey(GroupProfile, on_delete=models.CASCADE, db_column='group', default=None, null=True)
    group_name = models.TextField()
    group_image_path = models.TextField()
    constitution = models.ForeignKey(ConstitutionTable, on_delete=models.CASCADE, db_column='constitution', default=None, null=True)
    cycle_schedule = models.ForeignKey(CycleSchedules, on_delete=models.CASCADE, db_column='cycle_schedule', default=None, null=True)
    group_members = models.ForeignKey(GroupMembers, on_delete=models.CASCADE, db_column='group_members', default=None, null=True)
    assigned_positions = models.ForeignKey(AssignedPositions, on_delete=models.CASCADE, db_column='assigned_positions', default=None, null=True)
    
    def __str__(self):
        return self.group_name

class LoanApplications(models.Model):
    group = models.ForeignKey(GroupForm, on_delete=models.CASCADE, db_column='group', default=None, null=True)
    cycle = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE,  db_column='cycle', default=None, null=True)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, db_column='meeting', default=None, null=True)
    submission_date = models.TextField()
    loan_applicant = models.TextField()
    group_member = models.ForeignKey(GroupMembers, on_delete=models.CASCADE, db_column='group_member', default=None, null=True)
    amount_needed = models.FloatField()
    loan_purpose = models.TextField()
    repayment_date = models.TextField()
    
    def __str__(self):
        return self.group


class SocialFundApplications(models.Model):
    group = models.ForeignKey(GroupForm, on_delete=models.CASCADE, db_column='group', default=None, null=True)
    cycle = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE,  db_column='cycle', default=None, null=True)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, db_column='meeting', default=None, null=True)
    submission_date = models.TextField()
    applicant = models.TextField()
    group_member = models.ForeignKey(GroupMembers, on_delete=models.CASCADE, db_column='group_member', default=None, null=True)
    amount_needed = models.FloatField()
    social_purpose = models.TextField()
    repayment_date = models.TextField()
    
    def __str__(self):
        return self.group


class CycleStartMeeting(models.Model):
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
    group = models.ForeignKey(GroupForm, on_delete=models.CASCADE, db_column='group', default=None, null=True)
    cycle = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE,  db_column='cycle', default=None, null=True)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE,  db_column='meeting', default=None, null=True)
    member = models.ForeignKey(GroupMembers, on_delete=models.CASCADE, db_column='member', default=None, null=True)
    payment_amount = models.FloatField()
    payment_date = models.TextField()
    
    def __str__(self):
        return self.group
    

class Fines(models.Model):
    memberId = models.ForeignKey(GroupMembers, on_delete=models.CASCADE, db_column='memberId')
    amount = models.IntegerField()
    reason = models.TextField()
    groupId = models.ForeignKey(GroupForm, on_delete=models.CASCADE, db_column='groupId')
    cycleId = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE, db_column='cycleId', default=None, null=True)
    meetingId = models.ForeignKey(Meeting, on_delete=models.CASCADE, db_column='meetingId', default=None, null=True)
    savingsAccountId = models.ForeignKey(SavingsAccount, on_delete=models.CASCADE, db_column='savingsAccountId')
    
    def __str__(self):
        return self.groupId


class GroupCycleStatus(models.Model):
    group = models.ForeignKey(GroupProfile, on_delete=models.CASCADE, db_column='group', default=None, null=True)
    cycleId = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE, db_column='cycleId', default=None, null=True)
    is_cycle_started = models.BooleanField(default=False)
    
    def __str__(self):
        return self.group

class Loans(models.Model):
    member = models.ForeignKey(GroupMembers, on_delete=models.CASCADE, db_column='member', default=None, null=True)
    loan_applicant = models.TextField()
    group = models.ForeignKey(GroupForm, on_delete=models.CASCADE, db_column='group', default=None, null=True)
    loan_purpose = models.TextField()
    loan_amount = models.FloatField()
    interest_rate = models.FloatField()
    start_date = models.TextField()
    end_date = models.TextField()
    status = models.TextField()
    
    def __str__(self):
        return self.group


class LoanDisbursement(models.Model):
    member = models.ForeignKey(GroupMembers, on_delete=models.CASCADE, db_column='member', default=None, null=True)
    group = models.ForeignKey(GroupForm, on_delete=models.CASCADE, db_column='group', default=None, null=True)
    cycleId = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE, db_column='cycleId', default=None, null=True)
    loan = models.ForeignKey(Loans, on_delete=models.CASCADE, db_column='loan', default=None, null=True)
    disbursement_amount = models.FloatField()
    disbursement_date = models.DateField()
    
    def __str__(self):
        return self.group


class LoanPayments(models.Model):
    member = models.ForeignKey(GroupMembers, on_delete=models.CASCADE, db_column='member', default=None, null=True)
    group = models.ForeignKey(GroupForm, on_delete=models.CASCADE, db_column='group', default=None, null=True)
    loan = models.ForeignKey(Loans, on_delete=models.CASCADE, db_column='loan', default=None, null=True)
    payment_amount = models.FloatField()
    payment_date = models.TextField()
    def __str__(self):
        return self.group


class ShareOut(models.Model):
    group = models.ForeignKey(GroupProfile, on_delete=models.CASCADE, db_column='group', default=None, null=True)
    cycleId = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE, db_column='cycleId', default=None, null=True)
    users = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='users', default=None, null=True)
    share_value = models.FloatField()
    def __str__(self):
        return self.group


class ReversedTransactions(models.Model):
    group = models.ForeignKey(GroupProfile, on_delete=models.CASCADE, db_column='group', default=None, null=True)
    savings_account = models.ForeignKey(SavingsAccount, on_delete=models.CASCADE, db_column='savings_account', default=None, null=True)
    logged_in_users = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='logged_in_users', default=None, null=True)
    reversed_amount = models.FloatField()
    date = models.TextField()
    purpose = models.TextField()
    reversed_data = models.TextField()
    
    def __str__(self):
        return self.group

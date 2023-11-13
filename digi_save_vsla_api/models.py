from django.db import models

# Create your models here.
class GroupProfile(models.Model):
    profile_id = models.IntegerField(default=None, blank=True, null=True)
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
    sync_flag = models.IntegerField(default=1)

    def __str__(self):
        return self.groupName
    
class ConstitutionTable(models.Model):
    constitution_id = models.IntegerField(default=None, blank=True, null=True)
    group_id = models.IntegerField(default=None, blank=True, null=True)
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
    sync_flag = models.IntegerField(default=1)

    def __str__(self):
        return f"ConstitutionTable for Group ID: {self.group_id}  - Has Constitution: {self.hasConstitution}"

class Users(models.Model):
    users_id = models.IntegerField(default=None, blank=True, null=True)
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
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.fname} {self.lname}"

class GroupMembers(models.Model):
    member_id = models.IntegerField(default=None, blank=True, null=True)
    user_id = models.IntegerField(default=None, blank=True, null=True)
    group_id = models.IntegerField(default=None, blank=True, null=True)
    sync_flag = models.IntegerField(default=1)

    def __str__(self):
        return f"GroupMember {self.user_id} for Group ID: {self.group_id}"

class CycleSchedules(models.Model):
    schedule_id = models.IntegerField(default=None, blank=True, null=True)
    group_id = models.IntegerField(default=None, blank=True, null=True)
    meeting_duration = models.TextField()
    number_of_meetings = models.IntegerField()
    meeting_frequency = models.TextField()
    day_of_week = models.TextField()
    start_date = models.TextField()
    share_out_date = models.TextField()
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return f"CycleSchedules for Group ID: {self.group_id}"
    

class Positions(models.Model):
    name = models.TextField()
    position_id = models.IntegerField(default=None, blank=True, null=True)
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return self.name
    
class AssignedPositions(models.Model):
    assign_id = models.IntegerField(default=None, blank=True, null=True)
    position_id = models.IntegerField(default=None, blank=True, null=True)
    member_id = models.IntegerField(default=None, blank=True, null=True)
    group_id = models.IntegerField(default=None, blank=True, null=True)
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
     return f"Assigned position for Group Id{self.position_id}"


class GroupForm(models.Model):
    group_id = models.IntegerField(default=None, blank=True, null=True)
    group_profile_id = models.IntegerField(default=None, blank=True, null=True)
    group_id = models.IntegerField(default=None, blank=True, null=True)
    logged_in_users_id = models.IntegerField(default=None, blank=True, null=True)
    constitution_id = models.IntegerField(default=None, blank=True, null=True)
    cycle_schedule_id = models.IntegerField(default=None, blank=True, null=True)
    group_member_id = models.IntegerField(default=None, blank=True, null=True)
    assigned_position_id = models.IntegerField(default=None, blank=True, null=True)
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return f"Group Id: {self.group_id}"
    
class SavingsAccount(models.Model):
    logged_in_users_id = models.IntegerField(default=None, blank=True, null=True)
    date = models.TextField()
    purpose = models.TextField()
    amount = models.FloatField()
    sync_flag = models.IntegerField(default=1)
    
    group = models.IntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return str(self.group)

class GroupFees(models.Model):
    fee_id = models.IntegerField(default=None, blank=True, null=True)
    member = models.IntegerField(default=None, blank=True, null=True)
    group_id = models.IntegerField(default=None, blank=True, null=True)
    registration_fee = models.FloatField()
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.member)

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
    sync_flag = models.IntegerField(default=1)
    
    group_id = models.IntegerField(default=None, blank=True, null=True)
    
    def __str__(self):
        return str(self.group_id)
    
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
    sync_flag = models.IntegerField(default=1)
    
    group_id = models.IntegerField(default=None, blank=True, null=True)
    cycle_id = models.IntegerField(default=None, blank=True, null=True)
    
    def __str__(self):
        return str(self.group_id)
    
    
class MemberShares(models.Model):
    logged_in_users_id = models.IntegerField()
    date = models.TextField()
    sharePurchases = models.TextField()
    
    meeting = models.IntegerField(default=None, blank=True, null=True)
    users = models.IntegerField(default=None, blank=True, null=True)
    group_id = models.IntegerField(default=None, blank=True, null=True)
    cycle_id = models.IntegerField(default=None, blank=True, null=True)
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.group_id)
    
class WelfareAccount(models.Model):
    logged_in_users_id = models.IntegerField(default=None, blank=True, null=True)
    amount = models.FloatField()
    group_id = models.IntegerField(default=None, blank=True, null=True)
    meeting_id = models.IntegerField(default=None, blank=True, null=True)
    cycle_id = models.IntegerField(default=None, blank=True, null=True)
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.group_id)

class ActiveCycleMeeting(models.Model):
    
    group_id = models.IntegerField(default=None, blank=True, null=True)
    cycleMeetingID = models.IntegerField(default=None, blank=True, null=True)
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.group_id)

class Shares(models.Model):
    sharePurchases = models.TextField()
    
    meetingId = models.IntegerField(default=None, blank=True, null=True)
    cycle_id = models.IntegerField(default=None, blank=True, null=True)
    group_id = models.IntegerField(default=None, blank=True, null=True)
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.group_id)


class Social(models.Model):
    socialFund = models.TextField()
    sync_flag = models.IntegerField(default=1)
    group_id = models.IntegerField(default=None, blank=True, null=True)
    meetingId = models.IntegerField(default=None, blank=True, null=True)
    
    def __str__(self):
        return str(self.meetingId)

class LoanApplications(models.Model):
    group_id = models.IntegerField(default=None, blank=True, null=True)
    cycle_id = models.IntegerField(default=None, blank=True, null=True)
    meeting_id = models.IntegerField(default=None, blank=True, null=True)
    submission_date = models.TextField()
    loan_applicant = models.TextField()
    group_member = models.IntegerField(default=None, blank=True, null=True)
    amount_needed = models.FloatField()
    loan_purpose = models.TextField()
    repayment_date = models.TextField()
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.group_id)


class SocialFundApplications(models.Model):
    group_id = models.IntegerField(default=None, blank=True, null=True)
    cycle_id = models.IntegerField(default=None, blank=True, null=True)
    meeting_id = models.IntegerField(default=None, blank=True, null=True)
    submission_date = models.TextField()
    applicant = models.TextField()
    group_member = models.IntegerField(default=None, blank=True, null=True)
    amount_needed = models.FloatField()
    social_purpose = models.TextField()
    repayment_date = models.TextField()
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.group_id)


class CycleStartMeeting(models.Model):
    group = models.IntegerField(default=None, blank=True, null=True)
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
    sync_flag = models.IntegerField(default=1)


class PaymentInfo(models.Model):
    group = models.IntegerField(default=None, blank=True, null=True)
    cycle_id = models.IntegerField(default=None, blank=True, null=True)
    meeting_id = models.IntegerField(default=None, blank=True, null=True)
    member_id = models.IntegerField(default=None, blank=True, null=True)
    payment_amount = models.FloatField()
    payment_date = models.TextField()
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.group)
    

class Fines(models.Model):
    memberId = models.IntegerField(default=None, blank=True, null=True)
    amount = models.IntegerField()
    reason = models.TextField()
    groupId = models.IntegerField(default=None, blank=True, null=True)
    cycleId = models.IntegerField(default=None, blank=True, null=True)
    meetingId = models.IntegerField(default=None, blank=True, null=True)
    savingsAccountId = models.IntegerField(default=None, blank=True, null=True)
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.groupId)


class GroupCycleStatus(models.Model):
    group = models.IntegerField(default=None, blank=True, null=True)
    cycleId = models.IntegerField(default=None, blank=True, null=True)
    is_cycle_started = models.BooleanField(default=False)
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.group)

class Loans(models.Model):
    member = models.IntegerField(default=None, blank=True, null=True)
    loan_applicant = models.TextField()
    group = models.IntegerField(default=None, blank=True, null=True)
    loan_purpose = models.TextField()
    loan_amount = models.FloatField()
    interest_rate = models.FloatField()
    start_date = models.TextField()
    end_date = models.TextField()
    status = models.TextField()
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.group)


class LoanDisbursement(models.Model):
    member = models.IntegerField(default=None, blank=True, null=True)
    group = models.IntegerField(default=None, blank=True, null=True)
    cycleId = models.IntegerField(default=None, blank=True, null=True)
    loan = models.IntegerField(default=None, blank=True, null=True)
    disbursement_amount = models.FloatField()
    disbursement_date = models.DateField()
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.group)


class LoanPayments(models.Model):
    member = models.IntegerField(default=None, blank=True, null=True)
    group = models.IntegerField(default=None, blank=True, null=True)
    loan = models.IntegerField(default=None, blank=True, null=True)
    payment_amount = models.FloatField()
    payment_date = models.TextField()
    sync_flag = models.IntegerField(default=1)
    def __str__(self):
        return str(self.group)


class ShareOut(models.Model):
    group = models.IntegerField(default=None, blank=True, null=True)
    cycleId = models.IntegerField(default=None, blank=True, null=True)
    users = models.IntegerField(default=None, blank=True, null=True)
    share_value = models.FloatField()
    sync_flag = models.IntegerField(default=1)
    def __str__(self):
        return str(self.group)


class ReversedTransactions(models.Model):
    group = models.IntegerField(default=None, blank=True, null=True)
    savings_account = models.IntegerField(default=None, blank=True, null=True)
    logged_in_users = models.IntegerField(default=None, blank=True, null=True)
    reversed_amount = models.FloatField()
    date = models.TextField()
    purpose = models.TextField()
    reversed_data = models.TextField()
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.group)

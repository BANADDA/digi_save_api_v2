from django.contrib import admin
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError('The phone field must be set')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(phone, password, **extra_fields)

class Users(AbstractBaseUser, PermissionsMixin):
    unique_code = models.TextField(unique=True)
    fname = models.TextField(unique=True)
    lname = models.TextField()
    email = models.EmailField()  
    phone = models.TextField(unique=True)  
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
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    REQUIRED_FIELDS = ['unique_code', 'lname', 'phone']  
    USERNAME_FIELD = 'fname'  

    objects = CustomUserManager()

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class ConcreteUser(Users):
    class Meta:
        verbose_name = 'Concrete User'
        verbose_name_plural = 'Concrete Users'

class ConcreteUserAdmin(admin.ModelAdmin):
    # Define how you want the concrete user model to be represented in the admin
    list_display = ('fname', 'lname', 'email', 'phone', 'is_staff', 'is_active')
    search_fields = ('fname', 'lname', 'email', 'phone')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('unique_code', 'fname', 'lname', 'email', 'phone', 'sex', 'country', 'date_of_birth', 'image', 'district', 'subCounty', 'village', 'number_of_dependents', 'family_information', 'next_of_kin_name', 'next_of_kin_has_phone_number', 'next_of_kin_phone_number', 'pwd_type')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('unique_code', 'fname', 'lname', 'email', 'phone', 'sex', 'country', 'date_of_birth', 'image', 'district', 'subCounty', 'village', 'number_of_dependents', 'family_information', 'next_of_kin_name', 'next_of_kin_has_phone_number', 'next_of_kin_phone_number', 'pwd_type', 'password1', 'password2'),
        }),
    )

# Register the concrete user model in the admin
admin.site.register(ConcreteUser, ConcreteUserAdmin)

    
    # def __str__(self):
    #     return f"{self.fname} {self.lname}"

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

    def __str__(self):
        return f"ConstitutionTable for Group ID: {self.group_id}  - Has Constitution: {self.hasConstitution}"


class GroupMembers(models.Model):
    user_id = models.IntegerField(default=None, blank=True, null=True)
    group_id = models.IntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return f"GroupMember {self.user_id} for Group ID: {self.group_id}"

class CycleSchedules(models.Model):
    group_id = models.IntegerField(default=None, blank=True, null=True)
    meeting_duration = models.TextField()
    number_of_meetings = models.IntegerField()
    meeting_frequency = models.TextField()
    day_of_week = models.TextField()
    start_date = models.TextField()
    share_out_date = models.TextField()
    
    def __str__(self):
        return f"CycleSchedules for Group ID: {self.group_id}"
    

class Positions(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return self.name
    
class AssignedPositions(models.Model):
    position_name = models.TextField(default=None, blank=True, null=True)
    member_id = models.IntegerField(default=None, blank=True, null=True)
    group_id = models.IntegerField(default=None, blank=True, null=True)
    
    def __str__(self):
     return f"Assigned position for Group Id{self.group_id}"


class GroupForm(models.Model):
    group_profile_id = models.IntegerField(default=None, blank=True, null=True)
    group_id = models.IntegerField(default=None, blank=True, null=True)
    logged_in_users_id = models.IntegerField(default=None, blank=True, null=True)
    constitution_id = models.IntegerField(default=None, blank=True, null=True)
    cycle_schedule_id = models.IntegerField(default=None, blank=True, null=True)
    group_member_id = models.IntegerField(default=None, blank=True, null=True)
    assigned_position_id = models.IntegerField(default=None, blank=True, null=True)
    
    def __str__(self):
        return f"Group Id: {self.group_id}"
    
class SavingsAccount(models.Model):
    logged_in_users_id = models.IntegerField(default=None, blank=True, null=True)
    date = models.TextField()
    purpose = models.TextField()
    amount = models.FloatField()
    
    group = models.IntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return str(self.group)

class GroupFees(models.Model):
    member = models.IntegerField(default=None, blank=True, null=True)
    group_id = models.IntegerField(default=None, blank=True, null=True)
    registration_fee = models.FloatField()
    
    def __str__(self):
        return str(self.member)

class CycleMeeting(models.Model):
    date = models.TextField(default=None, blank=True, null=True)
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
    
    def __str__(self):
        return str(self.group_id)
    
class WelfareAccount(models.Model):
    logged_in_users_id = models.IntegerField(default=None, blank=True, null=True)
    amount = models.FloatField()
    group_id = models.IntegerField(default=None, blank=True, null=True)
    meeting_id = models.IntegerField(default=None, blank=True, null=True)
    cycle_id = models.IntegerField(default=None, blank=True, null=True)
    
    def __str__(self):
        return str(self.group_id)

class ActiveCycleMeeting(models.Model):
    
    group_id = models.IntegerField(default=None, blank=True, null=True)
    cycleMeetingID = models.IntegerField(default=None, blank=True, null=True)
    
    def __str__(self):
        return str(self.group_id)

class Shares(models.Model):
    sharePurchases = models.TextField()
    
    meetingId = models.IntegerField(default=None, blank=True, null=True)
    cycle_id = models.IntegerField(default=None, blank=True, null=True)
    group_id = models.IntegerField(default=None, blank=True, null=True)
    
    def __str__(self):
        return str(self.group_id)


class Social(models.Model):
    socialFund = models.TextField()
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


class PaymentInfo(models.Model):
    group = models.IntegerField(default=None, blank=True, null=True)
    cycle_id = models.IntegerField(default=None, blank=True, null=True)
    meeting_id = models.IntegerField(default=None, blank=True, null=True)
    member_id = models.IntegerField(default=None, blank=True, null=True)
    payment_amount = models.FloatField()
    payment_date = models.TextField()
    
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
    
    def __str__(self):
        return str(self.groupId)


class GroupCycleStatus(models.Model):
    group = models.IntegerField(default=None, blank=True, null=True)
    cycleId = models.IntegerField(default=None, blank=True, null=True)
    is_cycle_started = models.BooleanField(default=False)
    
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

    def __str__(self):
        return str(self.group)


class LoanDisbursement(models.Model):
    member = models.IntegerField(default=None, blank=True, null=True)
    group = models.IntegerField(default=None, blank=True, null=True)
    cycleId = models.IntegerField(default=None, blank=True, null=True)
    loan = models.IntegerField(default=None, blank=True, null=True)
    disbursement_amount = models.FloatField()
    disbursement_date = models.DateField()
    
    def __str__(self):
        return str(self.group)


class LoanPayments(models.Model):
    member = models.IntegerField(default=None, blank=True, null=True)
    group = models.IntegerField(default=None, blank=True, null=True)
    loan = models.IntegerField(default=None, blank=True, null=True)
    payment_amount = models.FloatField()
    payment_date = models.TextField()

    def __str__(self):
        return str(self.group)


class ShareOut(models.Model):
    group = models.IntegerField(default=None, blank=True, null=True)
    cycleId = models.IntegerField(default=None, blank=True, null=True)
    users = models.IntegerField(default=None, blank=True, null=True)
    share_value = models.FloatField()

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
    
    def __str__(self):
        return str(self.group)

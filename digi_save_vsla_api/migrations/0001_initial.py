# Generated by Django 5.0 on 2023-12-04 21:12

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConstitutionTable',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('hasConstitution', models.IntegerField(blank=True, default=None, null=True)),
                ('constitutionFiles', models.BinaryField(blank=True, default=None, null=True)),
                ('usesGroupShares', models.BooleanField(blank=True, default=None, null=True)),
                ('shareValue', models.FloatField(blank=True, default=None, null=True)),
                ('maxSharesPerMember', models.IntegerField(blank=True, default=None, null=True)),
                ('minSharesRequired', models.IntegerField(blank=True, default=None, null=True)),
                ('frequencyOfContributions', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('offersLoans', models.BooleanField(blank=True, default=None, null=True)),
                ('maxLoanAmount', models.FloatField(blank=True, default=None, null=True)),
                ('interestRate', models.FloatField(blank=True, default=None, null=True)),
                ('interestMethod', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('loanTerms', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('registrationFee', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('selectedCollateralRequirements', models.CharField(blank=True, default=None, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default=None, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CycleMeeting',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField(auto_now=True)),
                ('time', models.TextField(blank=True, default=None, null=True)),
                ('endTime', models.TextField(blank=True, default=None, null=True)),
                ('location', models.TextField(blank=True, default=None, null=True)),
                ('facilitator', models.TextField(blank=True, default=None, null=True)),
                ('meetingPurpose', models.TextField(blank=True, default=None, null=True)),
                ('latitude', models.FloatField(blank=True, default=None, null=True)),
                ('longitude', models.FloatField(blank=True, default=None, null=True)),
                ('address', models.TextField(blank=True, default=None, null=True)),
                ('objectives', models.TextField(blank=True, default=None, null=True)),
                ('attendanceData', models.TextField(blank=True, default=None, null=True)),
                ('representativeData', models.TextField(blank=True, default=None, null=True)),
                ('proposals', models.TextField(blank=True, default=None, null=True)),
                ('totalLoanFund', models.IntegerField(blank=True, default=None, null=True)),
                ('totalSocialFund', models.IntegerField(blank=True, default=None, null=True)),
                ('socialFundContributions', models.TextField(blank=True, default=None, null=True)),
                ('sharePurchases', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CycleSchedules',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('meeting_duration', models.TextField()),
                ('number_of_meetings', models.IntegerField()),
                ('meeting_frequency', models.TextField()),
                ('day_of_week', models.TextField()),
                ('start_date', models.DateField(auto_now=True)),
                ('share_out_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GroupProfile',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('groupName', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('countryOfOrigin', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('meetingLocation', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('groupStatus', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('groupLogoPath', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('partnerID', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('workingWithPartner', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('isWorkingWithPartner', models.IntegerField(blank=True, default=None, null=True)),
                ('numberOfCycles', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('numberOfMeetings', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('loanFund', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('socialFund', models.CharField(blank=True, default=None, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('unique_code', models.CharField(max_length=100)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('sex', models.CharField(max_length=10)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default=None, max_length=255)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.country')),
            ],
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default=None, max_length=255)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.district')),
            ],
        ),
        migrations.CreateModel(
            name='GroupForm',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('group_profile_id', models.IntegerField(blank=True, default=None, null=True)),
                ('constitution_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.constitutiontable')),
                ('cycle_schedule_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.cycleschedules')),
                ('logged_in_users_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.groupprofile')),
                ('assigned_position_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.positions')),
            ],
        ),
        migrations.CreateModel(
            name='GroupCycleStatus',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('is_cycle_started', models.BooleanField(default=False)),
                ('cycleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.cyclemeeting')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.groupform')),
            ],
        ),
        migrations.CreateModel(
            name='CycleStartMeeting',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date', models.TextField()),
                ('time', models.TextField()),
                ('location', models.TextField()),
                ('facilitator', models.TextField()),
                ('meeting_purpose', models.TextField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('address', models.TextField()),
                ('objectives', models.TextField()),
                ('attendance_data', models.TextField()),
                ('representative_data', models.TextField()),
                ('proposals', models.TextField()),
                ('end_time', models.TextField()),
                ('assigned_funds', models.TextField()),
                ('social_fund_bag', models.TextField()),
                ('social_fund_contributions', models.TextField()),
                ('share_purchases', models.TextField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.groupform')),
            ],
        ),
        migrations.AddField(
            model_name='cyclemeeting',
            name='group_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.groupform'),
        ),
        migrations.CreateModel(
            name='ActiveCycleMeeting',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('cycleMeetingID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.cyclemeeting')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.groupform')),
            ],
        ),
        migrations.AddField(
            model_name='cycleschedules',
            name='group_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.groupprofile'),
        ),
        migrations.AddField(
            model_name='constitutiontable',
            name='group_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.groupprofile'),
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField(auto_now=True)),
                ('time', models.TextField(blank=True, default=None, null=True)),
                ('endTime', models.TextField(blank=True, default=None, null=True)),
                ('location', models.TextField()),
                ('facilitator', models.TextField()),
                ('meetingPurpose', models.TextField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('address', models.TextField()),
                ('objectives', models.TextField()),
                ('attendanceData', models.TextField()),
                ('representativeData', models.TextField()),
                ('proposals', models.TextField()),
                ('socialFundContributions', models.TextField()),
                ('sharePurchases', models.TextField()),
                ('totalLoanFund', models.IntegerField()),
                ('totalSocialFund', models.IntegerField()),
                ('cycle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.cyclemeeting')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.groupform')),
            ],
        ),
        migrations.CreateModel(
            name='ReversedTransactions',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('savings_account', models.IntegerField(blank=True, default=None, null=True)),
                ('reversed_amount', models.FloatField()),
                ('date', models.DateField(auto_now=True)),
                ('purpose', models.TextField()),
                ('reversed_data', models.TextField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.groupform')),
                ('logged_in_users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SavingsAccount',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField(verbose_name=datetime.date(2023, 12, 4))),
                ('purpose', models.TextField()),
                ('amount', models.FloatField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.groupform')),
                ('logged_in_users_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShareOut',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('share_value', models.FloatField()),
                ('cycleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.cyclemeeting')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.groupform')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shares',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('sharePurchases', models.TextField()),
                ('cycle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.cyclemeeting')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.groupform')),
                ('meetingId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.meeting')),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('socialFund', models.TextField()),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.groupform')),
                ('meetingId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.meeting')),
            ],
        ),
        migrations.CreateModel(
            name='SocialFundApplications',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('submission_date', models.DateField(auto_now=True)),
                ('applicant', models.TextField()),
                ('group_member', models.IntegerField(blank=True, default=None, null=True)),
                ('amount_needed', models.FloatField()),
                ('social_purpose', models.TextField()),
                ('repayment_date', models.DateField(auto_now=True)),
                ('cycle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.cyclemeeting')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.groupform')),
                ('meeting_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.meeting')),
            ],
        ),
        migrations.CreateModel(
            name='Subcounty',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default=None, max_length=255)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.county')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfiles',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_of_birth', models.DateField(auto_now=True, null=True)),
                ('image', models.TextField(blank=True, default=None, null=True)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('sex', models.CharField(max_length=10)),
                ('number_of_dependents', models.IntegerField(default=0)),
                ('family_information', models.TextField()),
                ('next_of_kin_name', models.CharField(max_length=100)),
                ('next_of_kin_has_phone_number', models.BooleanField(default=False)),
                ('next_of_kin_phone_number', models.CharField(blank=True, default=None, max_length=15, null=True)),
                ('pwd_type', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.country')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.district')),
                ('subCounty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.subcounty')),
                ('user_id', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_profile_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentInfo',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('meeting_id', models.IntegerField(blank=True, default=None, null=True)),
                ('payment_amount', models.FloatField()),
                ('payment_date', models.TextField()),
                ('cycle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.cyclemeeting')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.groupform')),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.userprofiles')),
            ],
        ),
        migrations.CreateModel(
            name='MemberShares',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date', models.TextField()),
                ('sharePurchases', models.TextField()),
                ('cycle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.cyclemeeting')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.groupform')),
                ('logged_in_users_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logged_in_users_id', to=settings.AUTH_USER_MODEL)),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.meeting')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_member', to='digi_save_vsla_api.userprofiles')),
            ],
        ),
        migrations.CreateModel(
            name='Loans',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('loan_applicant', models.TextField()),
                ('loan_purpose', models.TextField()),
                ('loan_amount', models.FloatField()),
                ('interest_rate', models.FloatField()),
                ('start_date', models.TextField()),
                ('end_date', models.TextField()),
                ('status', models.TextField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.groupform')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.userprofiles')),
            ],
        ),
        migrations.CreateModel(
            name='LoanPayments',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('loan', models.IntegerField(blank=True, default=None, null=True)),
                ('payment_amount', models.FloatField()),
                ('payment_date', models.TextField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.groupform')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.userprofiles')),
            ],
        ),
        migrations.CreateModel(
            name='LoanDisbursement',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('loan', models.IntegerField(blank=True, default=None, null=True)),
                ('disbursement_amount', models.FloatField()),
                ('disbursement_date', models.DateField()),
                ('cycleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.cyclemeeting')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.groupform')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.userprofiles')),
            ],
        ),
        migrations.CreateModel(
            name='LoanApplications',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('submission_date', models.DateField(auto_now=True)),
                ('loan_applicant', models.TextField()),
                ('amount_needed', models.FloatField()),
                ('loan_purpose', models.TextField()),
                ('repayment_date', models.DateField(auto_now=True)),
                ('cycle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.cyclemeeting')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.groupform')),
                ('meeting_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.meeting')),
                ('group_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.userprofiles')),
            ],
        ),
        migrations.CreateModel(
            name='GroupMembers',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.groupprofile')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.userprofiles')),
            ],
        ),
        migrations.AddField(
            model_name='groupform',
            name='group_member_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.userprofiles'),
        ),
        migrations.CreateModel(
            name='GroupFees',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('registration_fee', models.FloatField()),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.groupform')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.userprofiles')),
            ],
        ),
        migrations.CreateModel(
            name='Fines',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('amount', models.IntegerField()),
                ('reason', models.TextField()),
                ('cycleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.cyclemeeting')),
                ('groupId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.groupform')),
                ('meetingId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.meeting')),
                ('savingsAccountId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.savingsaccount')),
                ('memberId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.userprofiles')),
            ],
        ),
        migrations.CreateModel(
            name='AssignedPositions',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('position_name', models.TextField(blank=True, default=None, null=True)),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.groupprofile')),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.userprofiles')),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default=None, max_length=255)),
                ('sub_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.subcounty')),
            ],
        ),
        migrations.AddField(
            model_name='userprofiles',
            name='village',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.village'),
        ),
        migrations.CreateModel(
            name='WelfareAccount',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('amount', models.FloatField()),
                ('cycle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.cyclemeeting')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.groupform')),
                ('logged_in_users_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('meeting_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='digi_save_vsla_api.meeting')),
            ],
        ),
    ]

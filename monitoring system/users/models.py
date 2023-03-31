from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Overriding the Default Django Auth User and adding One More Field (user_type)
class CustomUser(AbstractUser):
    user_type_data = ((1, "Admin"), (3, "User"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    gender = models.CharField(max_length=50, verbose_name="Gender")
    profile_pic = models.FileField()
    address = models.CharField(max_length=50, verbose_name="Address")

    #Added tables
    first_name = models.CharField(max_length=30, verbose_name="First Name")
    middle_name = models.CharField(max_length=20, verbose_name="Middle Name")
    last_name = models.CharField(max_length=20, verbose_name="Last Name")
    job = models.CharField(max_length=50, verbose_name="Job")
    username = models.CharField(max_length=16, verbose_name="Username")
    house_list = (
        ('Select your house type', 'Select your house type'),
        ('Private House','Private House'),
        ('Cottage','Cottage')
    )
    house_type = models.CharField(max_length=25, verbose_name="House Type", choices=house_list)
    def __str__(self):
        return self.username
    
    collegeChoices = [
        ('Select your college/department', 'Select your college/department'),
        ('COE', 'College of Engineering'),
        ('CON', 'College of Nursing'),
        ('CISC', 'College of Information Sciences and Computing'),
        ('CBM', 'College of Business Management'),
        ('CAS', 'College of Arts and Sciences'),
        ('CFES', 'College of Forestry and Environmental Science'),
        ('COA', 'College of Agriculture'),
        ('COED', 'College of Education'),
        ('CVM', 'College of Veterinary Medicine'),
        ('Other', 'Other Office'),
        ('Dugangan pa', 'Dugangan pa'),
    ]
    college = models.CharField(max_length=50, verbose_name="College/Department", choices=collegeChoices)
    def __str__(self):
        return self.username
    office = models.CharField(max_length=30, verbose_name="Office")

    maritalStatus = (
        ('Select your marital status', 'Select your marital status'),
        ('Single','Single'),
        ('Married','Married'),
        ('Widowed','Widowed'),
    )
    marital_status = models.CharField(max_length=30, verbose_name="Marital Status", choices=maritalStatus)
    def __str__(self):
        return self.username
    
    salaryGradeChoices = [
        ('Select your current salary', 'Select your current salary'),
        ('below 15,000 php', 'below 15,000 php'),
        ('15,001 - 20,000 php', '15,000 - 20,000 php'),
        ('20,001 - 30,000 php', '20,001 - 30,000 php'),
        ('30,001 - 40,000 php', '30,001 - 40,000 php'),
        ('40,001 - 50,000 php', '40,001 - 50,000 php'),
        ('50,001 - 60,000 php', '50,001 - 60,000 php'),
        ('60,001 - 70,000 php', '60,001 - 70,000 php'),
        ('70,001 - 80,000 php', '70,001 - 80,000 php'),
        ('80,001 - 90,000 php', '80,001 - 90,000 php'),
        ('90,001 - 100,000 php', '90,001 - 100,000 php'),
        ('More than 100,001+php', 'More than 100,000 php'),
    ]
    salary = models.CharField(max_length=30, verbose_name="Monthly Salary", choices=salaryGradeChoices)
    def __str__(self):
        return self.username
    phone_number = models.CharField(verbose_name="Phone Number", max_length=11)
    country = models.CharField(verbose_name="Country", max_length=20)
    nationality = models.CharField(verbose_name="Nationality", max_length=20)
    hometown = models.CharField(verbose_name="Hometown", max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

#Creating Django Signals

# It's like trigger in database. It will run only when Data is Added in CustomUser model

@receiver(post_save, sender=CustomUser)
# Now Creating a Function which will automatically insert data in Superadmin or Users
def create_user_profile(sender, instance, created, **kwargs):
    # if Created is true (Means Data Inserted)
    if created:
        # Check the user_type and insert the data in respective tables
        if instance.user_type == 1:
            Admin.objects.create(admin=instance)
        if instance.user_type == 3:
            Users.objects.create(admin=instance, address="", profile_pic="", gender="")
    

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.admin.save()
    if instance.user_type == 2:
        instance.staffs.save()
    if instance.user_type == 3:
        instance.users.save()
    



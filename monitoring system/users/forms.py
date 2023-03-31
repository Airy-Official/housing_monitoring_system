from django import forms 
from django.forms import Form

class DateInput(forms.DateInput):
    input_type = "date"

class AddUserForm(forms.Form):
    profile_pic = forms.FileField(label="Profile Pic", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", required=True, widget=forms.TextInput(attrs={"class":"form-control", 'placeholder': 'Enter your first name','autocomplete': "off"}))
    middle_name = forms.CharField(label="Middle Name", required=True, widget=forms.TextInput(attrs={"class":"form-control", 'placeholder': 'Enter your middle name','autocomplete': "off"}))
    last_name = forms.CharField(label="Last Name", required=True, widget=forms.TextInput(attrs={"class":"form-control", 'placeholder': 'Enter your last name','autocomplete': "off"}))
    username = forms.CharField(label="Username", required=True, min_length=8, max_length=16 , widget=forms.TextInput(attrs={"class":"form-control", 'placeholder': 'Enter your username | ex. Jose Rizal | J_Rizal2023','autocomplete': "off"}))
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(attrs={"class":"form-control", 'placeholder': 'Enter your active email','autocomplete': "off"}))

    house_list = (
        ('Select your house type', 'Select your house type'),
        ('Private House','Private House'),
        ('Cottage','Cottage')
    )
    house_type = forms.ChoiceField(label="House Type", required=True, choices=house_list, widget=forms.Select(attrs={"class":"form-control"}))
    
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
    college = forms.ChoiceField(label="College/Department", required=True, choices=collegeChoices, widget=forms.Select(attrs={"class":"form-control"}))
    office = forms.CharField(label="Office", required=True, widget=forms.TextInput(attrs={"class":"form-control", 'placeholder': 'Enter your assigned office','autocomplete': "off"}))
    job = forms.CharField(label="Job", required=True, widget=forms.TextInput(attrs={"class":"form-control", 'placeholder': 'Enter your current job position','autocomplete': "off"}))
    
    gender_list = (
        ('Select your gender','Select your gender'),
        ('Male','Male'),
        ('Female','Female')
    )
    gender = forms.ChoiceField(label="Gender", required=True, choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    maritalStatus = (
        ('Select your marital status', 'Selects your marital status'),
        ('Single','Single'),
        ('Married','Married'),
        ('Widowed','Widowed'),
    )
    marital_status = forms.ChoiceField(label="Marital Status", required=True, choices=maritalStatus, widget=forms.Select(attrs={"class":"form-control"}))

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
    salary = forms.ChoiceField(label="Monthly Salary", required=True, choices=salaryGradeChoices, widget=forms.Select(attrs={"class":"form-control"}))
    phone_number = forms.CharField(label="Phone Number", required=True,min_length=11, max_length=11, widget=forms.TextInput(attrs={"class":"form-control", 'placeholder': 'Enter your active phone number','autocomplete': "off"}))
    country = forms.CharField(label="Country", required=True, widget=forms.TextInput(attrs={"class":"form-control", 'placeholder': 'Enter your country','autocomplete': "off"}))
    nationality = forms.CharField(label="Nationality", required=True, widget=forms.TextInput(attrs={"class":"form-control", 'placeholder': 'Enter your nationality','autocomplete': "off"}))
    hometown = forms.CharField(label="Hometown", required=True, widget=forms.TextInput(attrs={"class":"form-control", 'placeholder': 'Enter your hometown','autocomplete': "off"}))
    address = forms.CharField(label="Address", required=True, widget=forms.TextInput(attrs={"class":"form-control", 'placeholder': 'Enter your current address','autocomplete': "off"}))
    password = forms.CharField(label="Password", required=True, min_length=8, max_length=16 ,widget=forms.PasswordInput(attrs={"class":"form-control", 'placeholder': 'Enter your desired password (8-16 chars)','autocomplete': "off"}))

class EditUserForm(forms.Form):
    profile_pic = forms.FileField(label="Profile Pic", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", required=False, widget=forms.TextInput(attrs={"class":"form-control", 'placeholder': 'Enter your first name','autocomplete': "off"}))
    middle_name = forms.CharField(label="Middle Name", required=False, widget=forms.TextInput(attrs={"class":"form-control", 'placeholder': 'Enter your middle name','autocomplete': "off"}))
    last_name = forms.CharField(label="Last Name", required=False, widget=forms.TextInput(attrs={"class":"form-control", 'placeholder': 'Enter your last name','autocomplete': "off"}))
    username = forms.CharField(label="Username", required=False, widget=forms.TextInput(attrs={"class":"form-control", 'placeholder': 'Enter your desired username','autocomplete': "off"}))
    email = forms.EmailField(label="Email", required=False, widget=forms.EmailInput(attrs={"class":"form-control", 'placeholder': 'Enter your active email','autocomplete': "off"}))
    
    house_list = (
        ('Select your house type', 'Select your house type'),
        ('Private House','Private House'),
        ('Cottage','Cottage')
    )
    house_type = forms.ChoiceField(label="House Type", required=False, choices=house_list, widget=forms.Select(attrs={"class":"form-control"}))
    
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
    college = forms.ChoiceField(label="College/Department", required=False, choices=collegeChoices, widget=forms.Select(attrs={"class":"form-control"}))
    office = forms.CharField(label="Office", required=False, widget=forms.TextInput(attrs={"class":"form-control", 'placeholder': 'Enter your assigned office','autocomplete': "off"}))
    job = forms.CharField(label="Job", required=False, widget=forms.TextInput(attrs={"class":"form-control", 'placeholder': 'Enter your current job position','autocomplete': "off"}))
    
    gender_list = (
        ('Select your gender','Select your gender'),
        ('Male','Male'),
        ('Female','Female')
    )
    gender = forms.ChoiceField(label="Gender", required=False, choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    maritalStatus = (
        ('Select your marital status', 'Selects your marital status'),
        ('Single','Single'),
        ('Married','Married'),
        ('Widowed','Widowed'),
    )
    marital_status = forms.ChoiceField(label="Marital Status", required=False, choices=maritalStatus, widget=forms.Select(attrs={"class":"form-control"}))

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
    salary = forms.ChoiceField(label="Monthly Salary", required=False, choices=salaryGradeChoices, widget=forms.Select(attrs={"class":"form-control"}))
    phone_number = forms.CharField(label="Phone Number", required=False, min_length=11 ,max_length=11, widget=forms.TextInput(attrs={"class":"form-control", 'placeholder': 'Enter your active phone number','autocomplete': "off"}))
    country = forms.CharField(label="Country", required=False, widget=forms.TextInput(attrs={"class":"form-control", 'placeholder': 'Enter your country','autocomplete': "off"}))
    nationality = forms.CharField(label="Nationality", required=False, widget=forms.TextInput(attrs={"class":"form-control", 'placeholder': 'Enter your nationality','autocomplete': "off"}))
    hometown = forms.CharField(label="Hometown", required=False, widget=forms.TextInput(attrs={"class":"form-control", 'placeholder': 'Enter your hometown','autocomplete': "off"}))
    address = forms.CharField(label="Address", required=False, widget=forms.TextInput(attrs={"class":"form-control", 'placeholder': 'Enter your current address','autocomplete': "off"}))
    password = forms.CharField(label="Password", required=False , min_length=8, max_length=16 ,widget=forms.PasswordInput(attrs={"class":"form-control", 'placeholder': 'Fill only if you want to change Password (8-16 chars)','autocomplete': "off"}))
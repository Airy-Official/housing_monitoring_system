from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

from users.models import CustomUser, Users
from .forms import AddUserForm, EditUserForm

def visit_user_profile(request):

    return render(request, "admin_template/visit_user_profile.html")

def admin_home(request):
    all_user_count = Users.objects.all().count()
    users = Users.objects.order_by('-id')[:5]
    context={
        "all_user_count": all_user_count,
        "users": users,
    }
    return render(request, "admin_template/home_content.html", context)

def add_user(request):
    users = Users.objects.order_by('-id')[:5]
    form = AddUserForm()
    context = {
        "users": users,
        "form": form,
    }
    return render(request, 'admin_template/add_user_template.html', context)

def add_user_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('add_user')
    else:
        form = AddUserForm(request.POST, request.FILES)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            address = form.cleaned_data['address']
            gender = form.cleaned_data['gender']
            job = form.cleaned_data['job']
            middle_name = form.cleaned_data['middle_name']
            house_type = form.cleaned_data['house_type']
            college = form.cleaned_data['college']
            office = form.cleaned_data['office']
            marital_status = form.cleaned_data['marital_status']
            salary = form.cleaned_data['salary']
            phone_number = form.cleaned_data['phone_number']
            country = form.cleaned_data['country']
            nationality = form.cleaned_data['nationality']
            hometown = form.cleaned_data['hometown']
            # Getting Profile Pic first
            # First Check whether the file is selected or not
            # Upload only if file is selected
            if len(request.FILES) != 0:
                profile_pic = request.FILES['profile_pic']
                fs = FileSystemStorage()
                filename = fs.save(profile_pic.name, profile_pic)
                profile_pic_url = fs.url(filename)
            else:
                profile_pic_url = None
            try:
                user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=3)
                user.users.address = address
                user.users.job = job
                # user.users.first_name = first_name
                user.users.middle_name = middle_name
                # user.users.last_name = last_name
                user.users.house_type = house_type
                user.users.college = college
                user.users.office = office
                user.users.marital_status = marital_status
                user.users.salary = salary
                user.users.phone_number = phone_number
                user.users.country = country
                user.users.nationality = nationality
                user.users.hometown = hometown
                user.users.gender = gender
                user.users.profile_pic = profile_pic_url
                user.save()
                messages.success(request, "User Added Successfully!")
                return redirect('add_user')
            except:
                messages.error(request, "Failed to Add User!")
                return redirect('add_user')
        else:
            return redirect('add_user')


def manage_user(request):
    users = Users.objects.all()
    context = {
        "users": users
    }
    return render(request, 'admin_template/manage_user_template.html', context)


def edit_user(request, user_id):
    # Adding User ID into Session Variable
    request.session['user_id'] = user_id

    user = Users.objects.get(admin=user_id)
    form = EditUserForm()
    # Filling the form with Data from Database
    form.fields['profile_pic'].initial = user.profile_pic
    form.fields['email'].initial = user.admin.email
    form.fields['username'].initial = user.admin.username
    form.fields['first_name'].initial = user.admin.first_name
    form.fields['last_name'].initial = user.admin.last_name
    form.fields['address'].initial = user.address
    form.fields['gender'].initial = user.gender
    form.fields['job'].initial = user.job
    form.fields['middle_name'].initial = user.middle_name
    form.fields['house_type'].initial = user.house_type
    form.fields['college'].initial = user.college
    form.fields['office'].initial = user.office
    form.fields['marital_status'].initial = user.marital_status
    form.fields['salary'].initial = user.salary
    form.fields['phone_number'].initial = user.phone_number
    form.fields['country'].initial = user.country
    form.fields['nationality'].initial = user.nationality
    form.fields['hometown'].initial = user.hometown
    context = {
        "id": user_id,
        "username": user.admin.username,
        "profile_pic": user.profile_pic,
        "job": user.job,
        "first_name": user.admin.first_name,
        "last_name": user.admin.last_name,
        "middle_name": user.middle_name,
        "form": form
    }
    return render(request, "admin_template/edit_user_template.html", context)

def edit_user_save(request):
    if request.method != "POST":
        return HttpResponse("Invalid Method!")
    else:
        user_id = request.session.get('user_id')
        if user_id == None:
            return redirect('/manage_user')

        form = EditUserForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            address = form.cleaned_data['address']
            gender = form.cleaned_data['gender']
            job = form.cleaned_data['job']
            middle_name = form.cleaned_data['middle_name']
            house_type = form.cleaned_data['house_type']
            college = form.cleaned_data['college']
            office = form.cleaned_data['office']
            marital_status = form.cleaned_data['marital_status']
            salary = form.cleaned_data['salary']
            phone_number = form.cleaned_data['phone_number']
            country = form.cleaned_data['country']
            nationality = form.cleaned_data['nationality']
            hometown = form.cleaned_data['hometown']
            # Getting Profile Pic first
            # First Check whether the file is selected or not
            # Upload only if file is selected
            if len(request.FILES) != 0:
                profile_pic = request.FILES['profile_pic']
                fs = FileSystemStorage()
                filename = fs.save(profile_pic.name, profile_pic)
                profile_pic_url = fs.url(filename)
            else:
                profile_pic_url = None

            try:
                # First Update into Custom User Model
                user = CustomUser.objects.get(id=user_id)
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.username = username
                user.save()

                # Then Update Users Table
                user_model = Users.objects.get(admin=user_id)
                user_model.address = address

                user_model.job = job
                user_model.middle_name = middle_name
                user_model.house_type = house_type
                user_model.college = college
                user_model.office = office
                user_model.marital_status = marital_status
                user_model.salary = salary
                user_model.phone_number = phone_number
                user_model.country = country
                user_model.nationality = nationality
                user_model.hometown = hometown
                user_model.gender = gender
                if profile_pic_url != None:
                    user_model.profile_pic = profile_pic_url
                user_model.save()
                # Delete user_id SESSION after the data is updated
                del request.session['user_id']

                messages.success(request, "User Updated Successfully!")
                return redirect('/edit_user/'+user_id)
            except:
                messages.success(request, "Failed to Update User.")
                return redirect('/edit_user/'+user_id)
        else:
            return redirect('/edit_user/'+user_id)


def delete_user(request, user_id):
    user = user.objects.get(admin=user_id)
    try:
        user.delete()
        messages.success(request, "User Deleted Successfully.")
        return redirect('manage_user')
    except:
        messages.error(request, "Failed to Delete User.")
        return redirect('manage_user')

@csrf_exempt
def check_email_exist(request):
    email = request.POST.get("email")
    user_obj = CustomUser.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


@csrf_exempt
def check_username_exist(request):
    username = request.POST.get("username")
    user_obj = CustomUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

def admin_profile(request):
    user = CustomUser.objects.get(id=request.user.id)

    context={
        "user": user
    }
    return render(request, 'admin_template/admin_profile.html', context)


def admin_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('admin_profile')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect('admin_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('admin_profile')
        
def staff_profile(request):
    pass


def user_profile(request):
    pass




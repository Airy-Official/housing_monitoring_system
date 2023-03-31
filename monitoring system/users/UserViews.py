from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage #To upload Profile Picture
from django.urls import reverse
import datetime # To Parse input DateTime into Python Date Time Object

from users.models import CustomUser, Users

def user_home(request):
    return render(request, "user_template/user_home_template.html")

def user_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    # user = Users.objects.get(admin=user)

    context={
        "user": user,
        # "user": user
    }
    return render(request, 'user_template/user_profile.html', context)


def user_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('user_profile')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        address = request.POST.get('address')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()

            user = Users.objects.get(admin=customuser.id)
            user.address = address
            user.save()
            
            messages.success(request, "Profile Updated Successfully")
            return redirect('user_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('user_profile')
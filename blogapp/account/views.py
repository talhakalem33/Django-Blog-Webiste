from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import UserJob
from blog.models import Blog

# Create your views here.
def register_request(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        firstname = firstname.replace(" ", "")
        lastname = lastname.replace(" ", "")
        username = firstname.lower() + "_"+ lastname.lower()

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "account/register.html", {"error" : "Aynı isime sahip başka bir kullanıcı var"})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "account/register.html", {"error" : "Aynı emaile sahip başka bir kullanıcı var"})
                else:
                    user =  User.objects.create_user(username=username,email=email, first_name=firstname, last_name=lastname, password=password)
                    user.is_staff = True
                    group = Group.objects.get(name="yazar")
                    user.groups.set([group])
                    user.save()

                    userjob = UserJob(username=username, job="yazar")
                    userjob.save()
                    
                    authenticated_user = authenticate(username=username, password=password)
                    if authenticated_user:
                        login(request, authenticated_user)

                    return redirect(reverse('admin:login')) 
                
        else: 
            return render(request, "account/register.html", {"error" : "Şifre eşleşmiyor"})

    return render(request, "account/register.html")

def editorregister_request(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        firstname = firstname.replace(" ", "")
        lastname = lastname.replace(" ", "")
        username = firstname.lower() + "_"+ lastname.lower()

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "account/editorregister.html", {"error" : "Aynı isime sahip başka bir kullanıcı var"})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "account/editorregister.html", {"error" : "Aynı emaile sahip başka bir kullanıcı var"})
                else:
                    user =  User.objects.create_user(username=username,email=email, first_name=firstname, last_name=lastname, password=password)
                    user.is_staff = False
                    group = Group.objects.get(name="editor")
                    user.groups.set([group])
                    user.save()

                    userjob = UserJob(username=username, job="editor")
                    userjob.save()
                    
                    authenticated_user = authenticate(username=username, password=password)
                    if authenticated_user:
                        login(request, authenticated_user)

                    return redirect(reverse('admin:login')) 
                
        else: 
            return render(request, "account/editorregister.html", {"error" : "Şifre eşleşmiyor"})

    return render(request, "account/editorregister.html")


@login_required
def myaccount(request):
    user = request.user
    try:
        user_job = UserJob.objects.get(username=user.username)
        job = user_job.job
    except UserJob.DoesNotExist:
        job = "Unknown"

    return render(request, "account/myaccount.html", {"user": user, "job": job})

def inactiveblogpage(request):
    user = request.user
    user_job = UserJob.objects.get(username=user.username)
    job = user_job.job

    if job == "editor":
        inactiveblogs = Blog.objects.filter(isactive=False)
        context = {'inactiveblogs' : inactiveblogs}

        return render(request, "account/unactiveblogs.html", context)
    else:
        return redirect("home")

def logout_request(request):
    return redirect("home")
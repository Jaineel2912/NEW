from django.shortcuts import render,HttpResponse,HttpResponseRedirect,reverse,get_object_or_404
from django.contrib.auth import authenticate, login as dj_login
from  .forms import AddBlogForms
from .models import Category,Tag

# Create your views here.
def base(request):
    return render(request,"base.html")

def index(request):
    category_display=Category.objects.all()
    tag_display=Tag.objects.all()
    print(category_display.query)


    context={
        "category_display":category_display,
        "tag_display":tag_display
    }




    return render(request,"index.html",context)


def alltags(request,slug):
    tag=Tag.objects.get(slug=slug)
    context={
        "tag":tag,
    }
    return render(request,"see_all_tag.html",context)

def login(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                dj_login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("your account is not active")
        else:
            return HttpResponse("Invalid account.")
    else:
        return render(request,"login.html")

def addblog(request):
    if request.method=="POST":
        form=AddBlogForms(data=request.POST)
        if form.is_valid():
            form.save()

    else:
        form=AddBlogForms()

    context={
        'form':form
    }

    return render(request,'addblog.html',context)

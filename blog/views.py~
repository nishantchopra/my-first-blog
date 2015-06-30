from .forms import UserForm
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from .forms import loginForm
from django.shortcuts import redirect,get_object_or_404
from django.contrib.auth import authenticate,logout
from custom_user.models import AuthUser, UserActivationProfile
from django.contrib.auth.admin import UserAdmin
from django.template.context_processors import csrf
from django.core.mail import send_mail
import uuid,datetime
from blog.forms import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext


from custom_user.forms import RegistrationForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    return render(request, 'blog/post_list1.html', {'posts': posts})



def post_list1(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list1.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def login(request,name):
    if request.method=="POST":
        form = loginForm(request.POST)
        if form.is_valid():
            u=request.POST['username'];
            p=request.POST['password'];
            user=authenticate(username=u,password=p)
            if user:
                return redirect('blog.views.post_list')
    else:
        form=loginForm()
    return render(request, 'blog/log_in.html', {'form':form})




def logoutview(request):
    logout(request)
 
    posts=Post.objects.all();
    return render(request,'blog/post_list.html',{'posts':posts})

#def register(request):
#    registered=False
#    if request.method=='POST':
#        user_form=UserForm(data=request.POST)
#        if user_form.is_valid():
#            user=user_form.save()
#            user.save()
#            return render(request, 'blog/post_list.html',{})
#        else:
#            print ("hg4qfdawsq")
#    else:
#        user_form=UserForm()
#    return render(request, 'blog/register.html',{'user_form':user_form,'registered':registered})
                
    
@csrf_protect
def register(request):
    args={}
    args.update(csrf(request))
    variables=None
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active=False
            user.save()
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            email_subject="Account confirmation"
            activation_key=str(uuid.uuid4())
            email_body="hey %s, thanks for signing up. to activate your account, click this link within 24 haurs http://127.0.0.1:8000/accounts/confirm/%s" % (username,activation_key)
            key_expires=datetime.datetime.today() + datetime.timedelta(1)
            user=AuthUser.objects.get(username=username)
            new_profile=UserActivationProfile(user=user, activation_key=activation_key, key_expires=key_expires)
            new_profile.save()
    
            send_mail(email_subject, email_body,'nishantchopra31@gmail.com',[email],fail_silently=False)
           
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    return render(request,'blog/register.html',{'form':form})


def register_confirm(request, activation_key):
    user_profile=get_object_or_404(UserActivationProfile, activation_key=activation_key)
    user=user_profile.user

    if user.is_active:
        return render(request,'blog/post_list.html',{})

        if user_profile.key_expires<timezone.now():
            return render(request,'blog/expires.html',{})
    user.is_active=True
    user.save()
    return render(request,'blog/confirm.html')


def register_success(request):
    return render_to_response(
        'blog/success.html',
    )

    

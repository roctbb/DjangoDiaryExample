from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from myapp.models import Post


def index(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    if request.method == "GET":
        posts = Post.objects.filter(user=request.user).all()
        return render(request, 'index.html', {'posts': posts})
    else:
        post = Post()
        post.text = request.POST.get('text')
        post.user = request.user
        post.save()

        return redirect('/')

def login_user(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('login')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is None:
            return redirect('/login')
        else:
            login(request, user)
            return redirect('/')

def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        user = User()
        user.email = request.POST.get('email')
        user.username = request.POST.get('login')
        user.set_password(request.POST.get('password'))
        user.save()

        login(request, user)

        return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/login')

def delete_post(request, post_id):
    if not request.user.is_authenticated:
        return redirect('/login')
    post = get_object_or_404(Post, pk=post_id)
    if post.user == request.user:
        post.delete()

    return redirect('/')
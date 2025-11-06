from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post,Comment

def index(request):

    posts = Post.objects.all().order_by('-id')


    if request.method == "POST":
        post_id = request.POST.get("post_id")
        message = request.POST.get("message")
        if post_id and message:
            post = Post.objects.get(id=post_id)
            Comment.objects.create(
                post=post,
                user=request.user,
                message=message
            )
            return redirect("home")

    ctx = {"posts": posts}
    return render(request, "index.html", ctx)










def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            print("Post saqlandi:", post.title)
            return redirect("home")
        else:
            print("Form xatoliklari:", form.errors)
    else:
        form = PostForm()

    return render(request, "add-post.html", {"form": form})



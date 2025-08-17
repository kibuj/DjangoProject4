from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostCreateForm, PostEditForm
from .models import Post


@login_required
def post_create(request):
    if request.method == "POST":
        form = PostCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            redirect('index')
    else:
        form = PostCreateForm(data=request.GET)
    return render(request, "posts/post_create.html", {"form": form})

@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug, user=request.user)

    if request.method == "POST":
        if request.user == post.user:
            form = PostEditForm(instance=post, data=request.POST, files=request.FILES)
            if form.is_valid():
                form.save()
                return redirect('index')
    else:
        form = PostEditForm(instance=post)

    return render(request, "posts/post_edit.html", {"form": form, "post": post})



def feed(request):
    posts = Post.objects.all()
    return render(request, "posts/feed.html", {"posts": posts})
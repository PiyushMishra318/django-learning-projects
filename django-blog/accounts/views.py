from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from accounts.forms import CommentForm, PostForm, ProfileSearchForm, RegistrationForm
from accounts.models import Comment, Post, UserProfile


class LoginPage(LoginView):
    template_name = "login.html"


class LogoutPage(LogoutView):
    template_name = "logout.html"


def login_redirect(request):
    if request.user.is_authenticated:
        return redirect("home")
    return redirect("login")


@login_required
def home(request):
    posts = Post.objects.select_related("author", "author__profile").prefetch_related(
        "comments__author",
        "comments__author__profile",
    )
    return render(
        request,
        "index.html",
        {"posts": posts, "post_form": PostForm(), "comment_form": CommentForm()},
    )


@login_required
def update(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(author=request.user, body=form.cleaned_data["body"])
    return redirect("home")


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                post=post,
                author=request.user,
                text=form.cleaned_data["text"],
            )
    return redirect("home")


@login_required
def search_profile(request):
    profile = None
    error = None
    form = ProfileSearchForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        query = form.cleaned_data["username"]
        profile = (
            UserProfile.objects.select_related("user")
            .filter(Q(display_name__iexact=query) | Q(user__username__iexact=query))
            .first()
        )
        if profile is None:
            error = "Profile not found"
    return render(request, "search.html", {"form": form, "profile": profile, "error": error})


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegistrationForm()
    return render(request, "reg_form.html", {"form": form})

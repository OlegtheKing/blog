from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import (LoginRequiredMixin,  # a tool to add login_required functionality for our view classes
    UserPassesTestMixin )  # tool for matching users
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView  # class-based views
from .models import Post
from django.contrib.auth.models import User


def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "blogapp/home.html", context)


class PostListView(ListView):  # django tries to predict some of common features
    model = Post
    template_name = "blogapp/home.html"
    context_object_name = "posts"  # by default it's objectslist
    ordering = ["-date_posted"]  # going from newest to oldest posts
    paginate_by = 5  # pagination (breaking list into many pages)


class UserPostListView(ListView):  # django tries to predict some of common features
    model = Post
    template_name = "blogapp/user_posts.html"
    context_object_name = "posts"  # by default it's objectslist
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_posted")


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):  # added login req
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user  # set the author to current logged in user
        return super().form_valid(form)  # running parent valid method + overridden


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # with that only user who created post can modify it
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()  # getting post obj
        if self.request.user == post.author:  # if logged user equal to that who created post
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"  # redirect after successful post deletion

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()  # getting post obj
        if self.request.user == post.author:  # if logged user equal to that who created post
            return True
        return False


def about(request):
    return render(request, "blogapp/about.html", {"title": "About"})



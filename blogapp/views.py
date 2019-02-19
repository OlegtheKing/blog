from django.shortcuts import render

posts = [
    {
        "author": "Oleg",
        "title": "Post 1",
        "content": "Content"
    }
]

def home(request):
    context = {
        "posts": posts
    }
    return render(request, "blogapp/home.html", context)


def about(request):
    return render(request, "blogapp/about.html", {"title": "About"})

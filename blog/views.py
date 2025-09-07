from django.shortcuts import render, get_object_or_404, redirect
from .models import Posts, Comments
from add.models import Category
from django.core.paginator import Paginator


def blog(request):
    all_posts = Posts.objects.all().order_by("-id")
    featured_posts = Posts.objects.filter(show_on_slider=True)
    latest_posts = Posts.objects.order_by("-id")[:15]

    paginator = Paginator(all_posts, 2)
    page = request.GET.get("page")
    paged_posts = paginator.get_page(page)

    data = {
        "all_posts": paged_posts,
        "featured_posts": featured_posts,
        "latest_posts": latest_posts,
    }

    return render(request, "blog/blog.html", data)


def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    category_posts = Posts.objects.filter(category=category)
    featured_posts = Posts.objects.filter(show_on_slider=True)
    latest_posts = Posts.objects.order_by("-id")[:15]

    paginator = Paginator(category_posts, 2)
    page = request.GET.get("page")
    paged_posts = paginator.get_page(page)

    data = {
        "category": category,
        "category_posts": paged_posts,
        "featured_posts": featured_posts,
        "latest_posts": latest_posts,
    }

    return render(request, "blog/category.html", data)


def post_details(request, category_slug, post_slug):
    post = get_object_or_404(Posts, category__slug=category_slug, slug=post_slug)
    featured_posts = Posts.objects.filter(show_on_slider=True)
    latest_posts = Posts.objects.order_by("-id")[:15]
    comments = Comments.objects.filter(post=post, approved=True).order_by("-timestamp")

    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        comment = request.POST["comment"]

        post_comment = Comments(
            first_name=first_name,
            last_name=last_name,
            email=email,
            comment=comment,
            post=post,
        )
        post_comment.save()

        return redirect("/category/" + category_slug + "/" + post_slug)

    data = {
        "post": post,
        "featured_posts": featured_posts,
        "latest_posts": latest_posts,
        "comments": comments,
    }
    return render(request, "blog/single_post.html", data)

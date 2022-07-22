from django.db.models import Q, Count
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from blog.models import Post, Category, Tag


class PostList(ListView):
    model = Post
    paginate_by = 10 # pagination
    template_name = 'blog/post_list.html'
    queryset = Post.objects.order_by('created_at')

    def get_queryset(self):
        name = self.request.GET.get('q', '')
        object_list = Post.objects.filter(
            Q(title__icontains=name) |
            Q(description_one__icontains=name) |
            Q(description_two__icontains=name)
        )
        return object_list


class PostDetail(DetailView):
    model = Post

    def get_object(self):
        post = super().get_object()
        post.post_views += 1
        post.save()
        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().annotate(post_count=Count('post_category'))
        context["tags"] = Tag.objects.all()
        context["recent_posts"] = Post.objects.all()[:3]
        return context


class PostByCategory(ListView):
    model = Post

    def get_queryset(self):
        slug = self.kwargs['slug']
        object_list = Post.objects.filter(
            Q(category__name__icontains=slug)
        )
        return object_list
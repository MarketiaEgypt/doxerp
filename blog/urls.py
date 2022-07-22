from django.urls import path
from blog import views
from blog.views import PostList, PostDetail, PostByCategory

app_name = 'blog'

urlpatterns = [
  path("post_list/", PostList.as_view(), name="post_list"),
  path("<slug:slug>/", PostDetail.as_view(), name="post_detail"),

  path("category/<str:slug>/", PostByCategory.as_view(), name="post_by_category"),
]
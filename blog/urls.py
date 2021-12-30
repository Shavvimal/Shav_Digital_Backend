from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, BlogPostFeaturedView, BlogPostCategoryView, BlogPostCategoryChapterView

urlpatterns = [
    path('', BlogPostListView.as_view()),
    path('post', BlogPostFeaturedView.as_view()),
    path('category', BlogPostCategoryView.as_view()),
    path('categorychapter', BlogPostCategoryChapterView.as_view()),
    path('<slug>', BlogPostDetailView.as_view()),
]

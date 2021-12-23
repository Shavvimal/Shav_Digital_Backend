from django.urls import path
from .views import ContactPostListView, ContactPostEndView

urlpatterns = [
    path('', ContactPostListView.as_view()),
    path('post', ContactPostEndView.as_view()),
]

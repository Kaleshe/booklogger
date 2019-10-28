from appNewest import views
from django.urls import path

urlpatterns = [
    path('', views.bookThis, name='newestBooks'),
]

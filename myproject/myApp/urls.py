from django.urls import path
from . import views
urlpatterns =[
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('education/', views.education, name='education'),
    path('work_experience/', views.work_experience, name='work_experience'),
    path('social_media/', views.social_media, name='social_media'),
]

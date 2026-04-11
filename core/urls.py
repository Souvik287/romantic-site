from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),

    path('question/', views.question, name='question'),

    path('taken/', views.taken, name='taken'),

    path('not-taken/', views.not_taken, name='not_taken'),

    path('see-you-soon/', views.see_you_soon, name='see_you_soon'),

    path('adjust-meeting/', views.adjust_meeting, name='adjust_meeting'),

    path('calendar-picker/', views.calendar_picker, name='calendar_picker'),
    
  path("music-player/", views.music_player, name="music_player"),


]
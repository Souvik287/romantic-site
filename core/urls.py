from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),

    path('question/', views.question, name='question'),

    path('taken/', views.taken, name='taken'),

    path('meetup-interest/', views.meetup_interest, name='meetup_interest'),

    path('not-taken/', views.not_taken, name='not_taken'),

    path('respectful-goodbye/', views.respectful_goodbye, name='respectful_goodbye'),

    path('see-you-soon/', views.see_you_soon, name='see_you_soon'),

    path('adjust-meeting/', views.adjust_meeting, name='adjust_meeting'),

    path('calendar-picker/', views.calendar_picker, name='calendar_picker'),

    path('meeting-confirmed/', views.meeting_confirmed, name='meeting_confirmed'),

]
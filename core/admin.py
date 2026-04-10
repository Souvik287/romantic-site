from django.contrib import admin

from .models import MeetingInfo


@admin.register(MeetingInfo)
class MeetingInfoAdmin(admin.ModelAdmin):
    """Admin configuration for MeetingInfo records."""

    list_display = ('meeting_time', 'meeting_location', 'instagram_link')

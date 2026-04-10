from django.db import models


class MeetingInfo(models.Model):
    """
    Stores display information for a meetup: when, where, and social link.
    """

    # Human-readable meeting schedule text (e.g. "Saturdays 10am–12pm").
    meeting_time = models.CharField(max_length=255)
    # Venue or address string shown to visitors.
    meeting_location = models.CharField(max_length=255)
    # Full Instagram profile or post URL.
    instagram_link = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Meeting info'
        verbose_name_plural = 'Meeting info'

    def __str__(self):
        return f'{self.meeting_time} @ {self.meeting_location}'

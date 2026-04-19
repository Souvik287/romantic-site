import logging

from django.shortcuts import render, redirect
logger = logging.getLogger(__name__)


def index(request):
    return render(request, "index.html")


def question(request):
    return render(request, "question.html")


def meetup_interest(request):
    return render(request, "meetup_interest.html")


def respectful_goodbye(request):
    return render(request, "respectful_goodbye.html")


def taken(request):
    return render(request, "taken.html")


def not_taken(request):
    return render(request, "not_taken.html")


def see_you_soon(request):
    return render(request, "see_you_soon.html")


def adjust_meeting(request):
    return render(request, "adjust_meeting.html")


def meeting_confirmed(request):
    """After calendar POST only; same romantic ending as see-you-soon."""
    if not request.session.pop("play_celebration_music", False):
        return redirect("calendar_picker")
    meeting_reminder = request.session.pop("meeting_reminder", None)
    return render(
        request,
        "see_you_soon.html",
        {"meeting_reminder": meeting_reminder},
    )


def calendar_picker(request):

    if request.method == "POST":

        date = request.POST.get("meeting_date")
        time = request.POST.get("meeting_time")
        place = (request.POST.get("meeting_place") or "").strip()

        if not date or not time or not place:
            return render(
                request,
                "calendar_picker.html",
                {"form_error": "Please fill in date, time, and meeting place."},
            )

        request.session["meeting_reminder"] = {
            "date": str(date),
            "time": str(time),
            "place": str(place),
        }
        request.session["play_celebration_music"] = True
        return redirect("meeting_confirmed")

    return render(request, "calendar_picker.html")

import logging

from django.shortcuts import render, redirect
from django.core.mail import send_mail


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

    send_mail(
        subject="Website response update",
        message="She clicked YES (already has a boyfriend).",
        from_email="smboss126@gmail.com",
        recipient_list=["smboss126@gmail.com"],
        fail_silently=True,
    )

    return render(request, "taken.html")


def not_taken(request):
    return render(request, "not_taken.html")


def see_you_soon(request):

    send_mail(
        subject="Meeting confirmation",
        message="She accepted your suggested meeting time.",
        from_email="smboss126@gmail.com",
        recipient_list=["smboss126@gmail.com"],
        fail_silently=True,
    )

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

        body = (
            "She submitted a meeting suggestion from the calendar page.\n\n"
            f"Date: {date}\n"
            f"Time: {time}\n"
            f"Location / place: {place}\n"
        )

        try:
            send_mail(
                subject="Meeting suggestion — date, time & place",
                message=body,
                from_email="smboss126@gmail.com",
                recipient_list=["smboss126@gmail.com"],
                fail_silently=False,
            )
        except Exception:
            logger.exception(
                "Calendar form: send_mail failed. Check Gmail app password and "
                "EMAIL_HOST / EMAIL_PORT in settings.py."
            )

        request.session["meeting_reminder"] = {
            "date": str(date),
            "time": str(time),
            "place": str(place),
        }
        request.session["play_celebration_music"] = True
        return redirect("meeting_confirmed")

    return render(request, "calendar_picker.html")

from django.shortcuts import render
from django.core.mail import send_mail


def index(request):
    return render(request, "index.html")


def question(request):
    return render(request, "question.html")


def taken(request):

    send_mail(
        subject="Website response update",
        message="She clicked YES (already has a boyfriend).",
        from_email="smboss126@gmail.com",
        recipient_list=["smboss126@gmail.com"],
        fail_silently=False,
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
        fail_silently=False,
    )

    return render(request, "see_you_soon.html")


def adjust_meeting(request):
    return render(request, "adjust_meeting.html")


def calendar_picker(request):

    if request.method == "POST":

        date = request.POST.get("meeting_date")
        time = request.POST.get("meeting_time")

        send_mail(
            subject="She suggested a meeting time",
            message=f"Selected date: {date}\nSelected time: {time}",
            from_email="smboss126@gmail.com",
            recipient_list=["smboss126@gmail.com"],
            fail_silently=False,
        )

        return render(request, "see_you_soon.html")

    return render(request, "calendar_picker.html")
def music_player(request):
    return render(request, "music_player.html")
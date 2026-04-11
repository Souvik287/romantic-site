from django.conf import settings


def emailjs_public_key(request):
    return {
        "EMAILJS_PUBLIC_KEY": getattr(
            settings,
            "EMAILJS_PUBLIC_KEY",
            "YOUR_PUBLIC_KEY",
        ),
    }

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

monthly_challenges = {
    "january": "Read for 30 minutes every day for a month.",
    "february": "Walk for 20 minutes every day for a month.",
    "march": "Learn Django for 30 minutes every day for a month.",
    "april": "Learn Django for 30 minutes every day for a month.",
    "may": "Learn Django for 30 minutes every day for a month.",
    "june": "Learn Django for 30 minutes every day for a month.",
    "july": "Learn Django for 30 minutes every day for a month.",
    "august": "Learn Django for 30 minutes every day for a month.",
    "september": "Learn Django for 30 minutes every day for a month.",
    "october": "Learn Django for 30 minutes every day for a month.",
    "november": "Learn Django for 30 minutes every day for a month.",
    "december": "take a break and relax for a month.",
}


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/monthly_challenges.html", {
            "month": month,
            "challenge_text": challenge_text
        })
    except:
        return HttpResponse("This month is not supported!")


def index(request):
    return render(request, "challenges/index.html")

from django.http import HttpResponse, Http404, HttpResponseRedirect
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


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())

    # 1. Handle invalid month numbers so the site doesn't crash
    if month < 1 or month > len(months):
        return HttpResponse("This month is not supported!")
        # Or use raise Http404()

    # 2. Get the month name (e.g., "january")
    redirect_month = months[month - 1]

    # 3. Get the actual challenge text using that name
    challenge_text = monthly_challenges[redirect_month]

    return render(request, "challenges/monthly_challenges.html", {
        "month": redirect_month,
        "challenge_text": challenge_text
    })


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

from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.shortcuts import render
from django.template.loader import render_to_string

monthly_challenges_dict = {
    'january': 'Eat not meat for the entire month!',
    'february': 'Walk for at least 20 minutes every day!',
    'march': 'Practice Django for at least 20 minutes a day!',
    'april': 'Eat not meat for the entire month!',
    'may': 'Walk for at least 20 minutes every day!',
    'june': 'Practice Django for at least 20 minutes a day!',
    'july': 'Walk for at least 20 minutes every day!',
    'august': 'Practice Django for at least 20 minutes a day!',
    'september': 'Eat not meat for the entire month!',
    'october': 'Walk for at least 20 minutes every day!',
    'november': 'Practice Django for at least 20 minutes a day!',
    'december': None,
}


def index(request):
    months = list(monthly_challenges_dict.keys())
    return render(request, 'challenges/index.html', {"months": months})


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges_dict.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid month!')

    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_dict[month]
        return render(request, 'challenges/challenge.html', {
            "text": challenge_text,
            "month": month.lower()
        })
    except:
        raise Http404('Invalid month!')
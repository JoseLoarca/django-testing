from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

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
    'december': 'Eat not meat for the entire month!',
}


def index(request):
    list_items = ''
    months = list(monthly_challenges_dict.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month-challenge', args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    response_data = f'<ul>{list_items}</ul>'
    return HttpResponse(response_data)


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
        response_data = f'<h1>{challenge_text}</h1>'
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('<h1>Month not supported!</h1>')

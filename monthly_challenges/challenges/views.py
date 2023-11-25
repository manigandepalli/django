from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
month_actions_dict = {'jan':"no nonveg",
                      'feb':"drink good amount of water",
                      'mar': "eat properly"}
def monthly_challenges(request, month):
    challenge_text = month_actions_dict.get(month,'')
    if challenge_text:
        return HttpResponse(challenge_text)
    else:
        return HttpResponseNotFound("given url is not found")


'''Here I am writing view logic for the redirect url'''
def month_challenge_by_number(request, month):
    months = list(month_actions_dict.keys())
    try:
        redirect_month = months[month]
        redirect_path = reverse("month-challenge", args =[redirect_month]) #/challenge/jan
    except:
        return HttpResponseNotFound("Redirect month is not found for the given url")
    return HttpResponseRedirect(redirect_path)





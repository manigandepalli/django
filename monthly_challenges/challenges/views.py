from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

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

def month_number(request, month):
    return HttpResponse(month)





# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from pytz import timezone
from meal import *
import datetime, json  # datetime 모듈 import

def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons': ['오늘', '내일']
    })


@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']

    if datacontent == '오늘':

        meal = get_diet(2, "2018.06.05", 1)

        return JsonResponse({
            'message': {
                'text': meal
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['오늘', '내일']
            }

        })

    elif datacontent == "내일":
        
        answer = get_diet(2, "2018.06.08", 3)
        return JsonResponse(
            {
                'message': {
                    'text': answer
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['오늘', '내일']
                }
            }
        )

    else:
        return JsonResponse(
            {
                'message': {
                    'text': '버튼이 아닙니다.'
                },
                'keyboard':{
                    'type': 'buttons',
                    'buttons': ['오늘', '내일']
                }
            }
        )





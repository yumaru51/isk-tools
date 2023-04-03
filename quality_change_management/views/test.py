from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render


def test(request):
    print('test')
    print('test2')
    return HttpResponse('hello world')

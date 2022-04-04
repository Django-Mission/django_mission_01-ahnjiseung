from http.client import HTTPResponse
from django import http
from django.shortcuts import render
from django.http import HttpResponse
import random
from django.views.decorators.csrf import csrf_exempt

# lotto 과제확인 첫 페이지
def index(request):
    return render(request, "index.html")

# lotto basic 과제
@csrf_exempt
def lotto_basic(request):
    if request.method == "GET":
        return render(request, 'lotto_basic.html')
    elif request.method == "POST":
        lotto_num = list(range(1,46))
        result = random.sample(lotto_num, k=6)
        return render(request, 'lotto_basic.html', {"result": result})

# lotto challenge 과제 - 게임 수 선택
def lotto_challenge(request):
    return render(request, "lotto_challenge.html")
    
# lotto challenge - 결과
def lotto_result(request):
    game_count = int(request.GET["game_count"])
    lotto_num = list(range(1,46))
    result = [random.sample(lotto_num, k=6) for i in range(game_count)]
    return render(request, "lotto_result.html", {"result":result, "game_count":game_count})
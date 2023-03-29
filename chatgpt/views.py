from django.shortcuts import render
from .api import chatfast
# Create your views here.


def index(request):
    res = request.GET.get('res', '')  # GET 파라미터에서 res 값을 가져옴

    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        res = chatfast(user_input)  # chatfast() 함수 호출

        # chatgpt_main.html 페이지를 GET 방식으로 호출하면서 GET 파라미터로 res 값을 전달
        return render(request, 'chatgpt/index.html', {'res': res})

    # chatgpt_main.html 페이지 렌더링
    return render(request, 'chatgpt/index.html', {'res': res})
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django import forms
import django_excel as excel

import json
import requests

from django.utils import timezone
from .models import Post
from .models import TrackList
from .models import BsubList
from .models import AsubList
from .models import User
from .models import Sheet1


import datetime
# Create your views here.

class UploadFileForm(forms.Form):
    file = forms.FileField()

def keyboard(request):
    return JsonResponse(
        {
            "type" : "buttons",
            "buttons" : ["공지사항","전체 트랙 보기","소프트웨어융합대학 사이트"]
        }
    )

@csrf_exempt
def message(request):
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content'] #버튼 항목중 무엇을 눌렀는가

    if return_str == "전체 트랙 보기":
        return JsonResponse({
            "message": {
                "text": '트랙을 선택하세요'
            },
            "keyboard": {
                "type": "buttons",
                "buttons": ["HCI & 비쥬얼컴퓨팅", "멀티미디어", "사물인터넷", "시스템응용", "인공지능", "가상현실", "정보보호", "데이터사이언스", "SW교육", "사이버국방",
                            "처음으로"]
            }
        })

    elif return_str == "HCI & 비쥬얼컴퓨팅":
        return JsonResponse({
            "message": {
                "text": "test"
            },
            "keyboard": {
                "type": "buttons",
                "buttons": ["HCI & 비쥬얼컴퓨팅", "멀티미디어", "사물인터넷", "시스템응용", "인공지능", "가상현실", "정보보호", "데이터사이언스", "SW교육", "사이버국방",
                            "처음으로"]
            }
        })

    elif return_str == "멀티미디어":
        return JsonResponse({
            "message": {
                "text": "test"
            },
            "keyboard": {
                "type": "buttons",
                "buttons": ["HCI & 비쥬얼컴퓨팅", "멀티미디어", "사물인터넷", "시스템응용", "인공지능", "가상현실", "정보보호", "데이터사이언스", "SW교육", "사이버국방",
                            "처음으로"]
            }
        })

    elif return_str == "사물인터넷":
        return JsonResponse({
            "message": {
                "text": "test"
            },
            "keyboard": {
                "type": "buttons",
                "buttons": ["HCI & 비쥬얼컴퓨팅", "멀티미디어", "사물인터넷", "시스템응용", "인공지능", "가상현실", "정보보호", "데이터사이언스", "SW교육", "사이버국방",
                            "처음으로"]
            }
        })

    elif return_str == "시스템응용":
        return JsonResponse({
            "message": {
                "text": "test"
            },
            "keyboard": {
                "type": "buttons",
                "buttons": ["HCI & 비쥬얼컴퓨팅", "멀티미디어", "사물인터넷", "시스템응용", "인공지능", "가상현실", "정보보호", "데이터사이언스", "SW교육", "사이버국방",
                            "처음으로"]
            }
        })

    elif return_str == "인공지능":
        return JsonResponse({
            "message": {
                "text": "test"
            },
            "keyboard": {
                "type": "buttons",
                "buttons": ["HCI & 비쥬얼컴퓨팅", "멀티미디어", "사물인터넷", "시스템응용", "인공지능", "가상현실", "정보보호", "데이터사이언스", "SW교육", "사이버국방",
                            "처음으로"]
            }
        })

    elif return_str == "가상현실":
        return JsonResponse({
            "message": {
                "text": "test"
            },
            "keyboard": {
                "type": "buttons",
                "buttons": ["HCI & 비쥬얼컴퓨팅", "멀티미디어", "사물인터넷", "시스템응용", "인공지능", "가상현실", "정보보호", "데이터사이언스", "SW교육", "사이버국방",
                            "처음으로"]
            }
        })

    elif return_str == "정보보호":
        return JsonResponse({
            "message": {
                "text": "test"
            },
            "keyboard": {
                "type": "buttons",
                "buttons": ["HCI & 비쥬얼컴퓨팅", "멀티미디어", "사물인터넷", "시스템응용", "인공지능", "가상현실", "정보보호", "데이터사이언스", "SW교육", "사이버국방",
                            "처음으로"]
            }
        })

    elif return_str == "데이터사이언스":
        return JsonResponse({
            "message": {
                "text": "test"
            },
            "keyboard": {
                "type": "buttons",
                "buttons": ["HCI & 비쥬얼컴퓨팅", "멀티미디어", "사물인터넷", "시스템응용", "인공지능", "가상현실", "정보보호", "데이터사이언스", "SW교육", "사이버국방",
                            "처음으로"]
            }
        })

    elif return_str == "SW교육":
        return JsonResponse({
            "message": {
                "text": "test"
            },
            "keyboard": {
                "type": "buttons",
                "buttons": ["HCI & 비쥬얼컴퓨팅", "멀티미디어", "사물인터넷", "시스템응용", "인공지능", "가상현실", "정보보호", "데이터사이언스", "SW교육", "사이버국방",
                            "처음으로"]
            }
        })

    elif return_str == "사이버국방":
        return JsonResponse({
            "message": {
                "text": "test"
            },
            "keyboard": {
                "type": "buttons",
                "buttons": ["HCI & 비쥬얼컴퓨팅", "멀티미디어", "사물인터넷", "시스템응용", "인공지능", "가상현실", "정보보호", "데이터사이언스", "SW교육", "사이버국방",
                            "처음으로"]
            }
        })

    #############################################################기타 버튼
    elif return_str == "처음으로":
        return JsonResponse({
            "message": {
                "text": "버튼을 선택하세요."
            },
            "keyboard": {
                "type": "buttons",
                "buttons": ["자신의 트랙 조회", "전체 트랙 보기", "소프트웨어융합대학 사이트"]
            }
        })

    elif return_str == "소프트웨어융합대학 사이트":
        return JsonResponse({
            "message": {
                "text": "소프트웨어 융합대학 홈페이지",
                "message_button": {
                    "label": "홈페이지 바로가기",
                    "url": "http://www.sejong.ac.kr/college/software.html?menu_id=1.12"
                }
            },
            "keyboard": {
                "type": "buttons",
                "buttons": ["자신의 트랙 조회", "전체 트랙 보기", "소프트웨어융합대학 사이트"]
            }
        })

def import_data(request):
    Sheet1.objects.all().delete()

    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)

        if form.is_valid():


            request.FILES['file'].save_book_to_database(
                models=[Sheet1],
                initializers=[None],
                mapdicts=[{'년도': 'number',
                           '학기': 'dummy',
                           '학수번호':'dummy',
                           '교과목명': 'subject',
                           '이수구분': 'dummy',
                           '교직영역': 'dummy',
                           '선택영역': 'dummy',
                           '학점': 'dummy',
                           '평가방식': 'dummy',
                           '등급': 'dummy',
                           '평점': 'dummy',
                           '개설학과코드': 'dummy'}]
            )
            return redirect('resultTrack')
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(
        request,
        'home/upload_form.html',
        {
            'form': form,
            'title': 'Import excel data into database example',
            'header': 'Please upload sample-data.xls:'
        })


def handson_table(request):
    return excel.make_response_from_tables(
        [Sheet1], 'handsontable.html')

def post_list(request):
    return render(request, 'home/main.html')


def allTrack(request):
    tracklists = TrackList.objects.all()
    bsublists=BsubList.objects.all()
    asublists=AsubList.objects.all()

    posts = Post.objects.filter(published_date__lte=timezone.now())

    context= { 'posts' : posts , 'tracklists':tracklists, 'bsublists':bsublists,'asublists':asublists}
    return render(request,'home/allTrack.html',context)

def resultTrack(request):

    users=User.objects.all()
    usersubs=Sheet1.objects.all()
    tracklists = TrackList.objects.all()
    bsublists=BsubList.objects.all()
    asublists=AsubList.objects.all()

    usersubs.update(number = request.user.get_username())  # 일괄 update 요청

    context={'users':users,
             'usersubs':usersubs,
             'tracklists':tracklists,
             'bsublists':bsublists,
             'asublists':asublists,
             }

    return render(request, 'home/resultTrack.html',context)



def test(request):
    return render(request,'home/test.html')

def notice(request):
    posts = Post.objects.all().order_by('-created_date') #날짜 역순
    context = {'posts':posts }
    return render(request,'home/notice.html',context)
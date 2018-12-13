from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django import forms
import django_excel as excel
from bs4 import BeautifulSoup
import urllib.request
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

    elif return_str == "HCI&비쥬얼컴퓨팅":
        return JsonResponse({
            "message": {
                "text": all_track(0)
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
                "text": all_track(1)
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
                "text": all_track(2)
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
                "text": all_track(3)
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
                "text": all_track(4)
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
                "text": all_track(5)
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
                "text": all_track(6)
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
                "text": all_track(7)
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
                "text": all_track(8)
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
                "text": all_track(9)
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
                "buttons": ["공지사항", "전체 트랙 보기", "소프트웨어융합대학 사이트"]
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
                "buttons": ["공지사항", "전체 트랙 보기", "소프트웨어융합대학 사이트"]
            }
        })

    elif return_str == "공지사항":
        return JsonResponse({
            "message": {
                "text": "세종대학교 공지사항\n\n" + notice(),

                "message_button": {
                    "label": "세종대학교 공지 바로가기",
                    "url": "http://board.sejong.ac.kr/boardlist.do?bbsConfigFK=333"
                }
            },
			"keyboard": {
				"type": "buttons",
				"buttons": ["공지사항", "전체 트랙 보기", "소프트웨어융합대학 사이트"]
			}
        })

def trackread():
    global tname
    global tbase
    global tuse

    treq = urllib.request.Request("http://ec2-18-216-35-115.us-east-2.compute.amazonaws.com:8000/allTrack",
                                  headers={'User-Agent': 'Mozilla/5.0'})

    tresponse = urllib.request.urlopen(treq)
    ttext = tresponse.read().decode("utf8")
    tsoup = BeautifulSoup(ttext, 'html.parser')

    tname = tsoup.find_all('td', {'class': 'tname'})
    tbase = tsoup.find_all('td', {'class': 'tbase'})
    tuse = tsoup.find_all('td', {'class': 'tuse'})

    for n in tname:
        i = tname.index(n)
        tname[i] = n.get_text().replace(" ", "")

    for n in tbase:
        i = tbase.index(n)
        tbase[i] = n.get_text().replace(" ", "")

    for n in tuse:
        i = tuse.index(n)
        tuse[i] = n.get_text().replace(" ", "")


##전체 트랙값 스트링 반환 함수##
def all_track(track):
    global tnum
    global tuse
    global tbase

    trackread()

    all = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # all에다가 문자열을 추가
    for i in range(0, len(tname)):
        all[i] = str(i + 1) + '.' + str(tname[i]) + '\n\n*기초교과*\n' + str(tbase[i]) + '\n\n*응용교과*\n' + str(tuse[i])

    list = all[track].split(",")

    abc = ""
    for i in range(0, len(list)):
        abc = abc + list[i] + "\n"

    return abc  # 해당 인덱스의 트랙 반환


def notice():
    req = urllib.request.Request("http://board.sejong.ac.kr/boardlist.do?bbsConfigFK=333",
                                 headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    text = response.read().decode("utf8")

    soup = BeautifulSoup(text, 'html.parser')

    all_infor = soup.find_all('tbody')

    subject = all_infor[0].find_all('td', {'class': "subject"})
    writer = all_infor[0].find_all('td', {'class': "writer"})
    date = all_infor[0].find_all('td', {'class': "date"})

    s_str = []
    w_str = []
    d_str = []
    for i in range(0, 5):
        n = subject[i].get_text().replace("\r", "").replace("\t", "").replace("\n", "")
        s_str.append(n)
        m = writer[i].get_text().replace("\r", "").replace("\t", "")
        w_str.append(m)
        l = date[i].get_text().replace("\r", "").replace("\t", "")
        d_str.append(l)

    iflist = ""

    num = ["(1) ", "(2) ", "(3) ", "(4) ", "(5) "]
    for i in range(0, len(s_str)):
        iflist += num[i] + s_str[i] + "\n" + w_str[i] + "\n" + d_str[i] + "\n\n"

    return iflist
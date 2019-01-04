# 세종대학교 소프트웨어융합대학 트랙관리 프로그램

창의학기제를 통해 제작된 세종대학교 트랙관리 프로그램입니다 현재는 소프트웨어융합대학 학생들만 이용가능 합니다.


### 개발자
* 전자정보통신공학과 17학번 강동민 @riyenas0925
* 바이오산업자원공학과 17학번 이경은 @2kyung19
* 컴퓨터공학과 17학번 이동엽 @moveside
* 지능기전공학부 17학번 황동윤 @karajan1962

### 개발기간
    2018-09-06 ~ 진행중

### 개발환경
>
    Language: Python 3.6  
    Framework: Django 1.11.0, AdminLTE 2  
    Library: BeautifulSoup, urllib, json, datetime, requests  
    Database: sqllite  
    Control System: Git 2.15.1.2, SourceTree 2.3.5  
    Web Server: Amazon Web Service Linux t2.micro  

## AWS Django 서버 구축하기

> 인스턴스 생성과 접속은 아래글 https://programmers.co.kr/learn/courses/6/lessons/629을 참고 하였습니다.

1. Git, Django, bs4 설치
>
    $ sudo apt-get update
    $ sudo apt-get install git
    $ sudo apt-get install python3-pip
    $ sudo pip3 install django
    $ sudo pip3 install bs4

2. Git에서 리포지토리 가져오기
>
    $ git clone <git 주소>
    $ manage.py가 있는 디렉토리로 이동
    $ python3 manage.py runserver 0.0.0.0:8000

3. 브라우저 접속
>
    브라우저에서 EC2 - Running instances - Public DNS뒤에 :8000붙인 주소로 접속

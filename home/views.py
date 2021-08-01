from django.shortcuts import render
import pandas as pd
import csv
import sqlite3
# from ssapp.models import Stock

# Create your views here.

from django.http import HttpResponse

def green_home(request):
    result={}
    return render(request, 'green_home.html', context=result)

def projects(request):
    result={}
    # result= dict()
    # conn = sqlite3('db.sqlite3')
    # con.row_factory=sqlite3.Row
    # curs= conn.cursor()
    # 
    # curs.execute('select Title, Genre, Nation, Director , Actor from result_data')
    # data= curs.fetchall()
    # for row in data:
    #     print(row['Title'],':',row['Genre'],':',row['Nation'])
    # result['movie_rows'] = data
    # 
    # curs.execute('select * from result_data')
    # result['input']= curs.fetchall()
    # for row in result['input']:
    #     print(row['Title'],':',row['Genre'],':',row['Nation'])        
    return render(request, 'projects.html', result)



def scrapping(request):
    result = {}
    return render(request, 'scrapping.html', context=result)

def machine(request):
    xArray = [0.46,0.39,0.38,0.35,0.32,0.31,0.29,0.29,0.28,0.27];
    yArray = ['이스케이프 룸 2: 노 웨이 아웃','미드나이트','명탐정 코난: 비색의 탄환','꽃다발 같은 사랑을 했다',
              '라야와 마지막 드래곤','보스 베이비 2','루카','오필리아','컨저링 3: 악마가 시켰다','랑종'];
    result = {'x_array':xArray, 'y_array':yArray}
    return render(request, 'machine.html', context=result)


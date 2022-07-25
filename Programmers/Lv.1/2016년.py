# datetime은 데이터분석에도 자주 사용했었던 라이브러리
from datetime import date

def solution(a, b):
    return date(2016,a,b).strftime('%a').upper()
#제작자-정해준(ADMIN@NONAVER.COM)
#해당 프로그램의 저작권은 GPL v3를 적용중입니다.
print('크롤링 프로그램 시작중...')
print('사용중 문제나 어려움이 있을시, 스크린샷 첨부해서 admin@nonaver.com으로 메일 주시면 도와드리겠습니다.')

#-----------------------아래부터 프로그램 시작-----------------------------
##-------프로그램 초기화,모듈 로딩--------
print('프로그램 초기화중....')
try:
	import selenium
	import os
	from selenium import webdriver
	username=os.environ.get('USERNAME')
	driver = webdriver.Chrome(executable_path="C:/Users/%s/NCBP/programdata/chromedriver.exe" % username)
	driver.implicitly_wait(1)
	import time
	driver.get("http://naver.com")
except:
	print('프로그램 초기화에 실패했습니다')
	print('selenium, chromedriver설치여부와 위치를 확인해 주세요')
	
##--------초기화,모듈로딩 끝----------------

##-------크롤링 사이트 로그인요청/사이트 지정----------------
print('현재 접속된 네이버 홈페이지에서 로그인해 주세요!')
time.sleep(5)
print('https://cafe.naver.com/skyplanet와 같이 카페 주소를 입력하세요.')
print('주소 뒤쪽에 슬래시 있으면 안됩니다. 없애주세요!')
cafedir = input()
start = input('저장을 시작할 게시글 번호를 입력하고 엔터키 누르세요: ')
end = input('저장을 끝낼 게시글 번호를 입력하고 엔터키 누르세요: ')
start=int(start)
end=int(end)
print('카페 설정이 완료되었습니다.')



sleeptime=input('딜레이를 몇 초나 줄지 입력하세요: ')
print('알림:사용자이름은 %s 입니다' % username)
print('컴퓨터 설정이 완료되었습니다.')




#본격 크롤링 시작.
tno=start
while tno <=end:
    no=cafedir + "/"+ str(tno)
    driver.get(no)
    time.sleep(int(sleeptime))
    try:
        alert = driver.switch_to.alert
        alert.accept()
        print("%d번 게시글은 존재하지 않음" % tno)
        tno = tno +1
    except:
	#아래 driver.switch_to_frame 구문은 네이버 카페의 iframe방식 컨텐츠 로딩에 의한것으로, 네이버카페 이외 사이트 크롤링시 제거하셔야 합니다.
        driver.switch_to_frame('cafe_main')
        html = driver.page_source.encode('utf-8')
        html= html.decode('utf-8')
        f = open('C:/Users/%s/NCBP/CAFE/%d.html' % (username, int(tno)) , 'w' , encoding='UTF-8')
        html = html.replace(u'<iframe title="답변쓰기에디터"' , u'w')
        f.write(html)
        f.close()
        print("%d번 게시글 저장완료." % int(tno))
        os.system('start cmd /c start /d "C:/Program Files/wkhtmltopdf/bin/" /b wkhtmltopdf.exe --encoding UTF-8 C:/Users/%s/NCBP/CAFE/%d.html C:/Users/%s/NCBP/CAFE/%d.pdf' % (username,tno,username,tno))
        print("%d번 게시글 변환요청 완료." % int(tno))
        tno = tno +1

print('크롤링이 완료되었습니다')
os.system('start C:/Users/%s/NCBP/CAFE' % (username))
print('크롤링 결과를 확인하세요. %d번 게시글 부터 %d번 게시글까지 크롤링되었습니다.' % (start,end))
print('존재하지 않는 게시글은 저장되지 않았습니다.')



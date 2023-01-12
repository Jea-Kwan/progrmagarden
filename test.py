#class
#변수
#class
#데이터수신
#API불러오기

import win32com.client
import pythoncom

'''
사용될 변수 모아놓은 클래스 
'''

class Object:
    로그인완료 = False
    해외선물_계좌번호 = None

'''
로그인 및 연결 상태에 대한 정보를 반환받게 정의해주는 이벤트

'''
class XASessionEvent(Object):
    def OnLogin(self, szCode, szMsg):
        print("로그인 %s, %s" % (szCode,szMsg))

        if szCode == "0000":
            Object.로그인완료 = True
        else:
            Object.로그인완료 = False

    def OnDisconnect(self):
        print("disconnect")


class XingApi_Class(Object):
    def __init__(self):
##### XASession COM 객체를 생성한다. ("API이벤트이름", 콜백클래스) ####
        self.XASession_object = win32com.clien.DispatchWithEvents("XA_Session.XASession", XASessionEvent)
    #################
    ######### 로그인 상태에서 xing 서버와 접속 중이면 끊음. ##
    self.login_status_check()
    ##############

    ### xing 실서버, 모의서버 구분해서 연결하기 ("hts. 실서버, demo. 모의서버", "포트넘버") ###
    self.server_connect()


    # 로그인 상태함수
    def login_status_check(self):
        print("로그인상태함수")


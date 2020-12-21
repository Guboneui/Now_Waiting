from time import sleep
import guest
from home import Home
from collections import Counter
import sys

class Store(Home):

    def printstorepage(self):
        print("사장님용 페이지에 입장하셨습니다.")

    def selectstoremenu(self):
        print("1.웨이팅 호출하기  |  2.현재 웨이팅 팀 확인하기  |  3.계산하기  |  4.쿠폰 발송하기  ||  5.당일 장사 끝(clear)  ||  6.웨이팅 등록하러가기(고객용)  ||  7.앱 종료")
        selectNum = input("원하는 번호를 입력하세요.")

        if (selectNum == "1"):
            self.callWaiting()

        elif (selectNum == "2"):
            self.checkNowWaiting()

        elif (selectNum == "3"):
            print("계산 및 쿠폰 확인 화면으로 이동합니다.")
            self.calculator()

        elif (selectNum == "4"):
            print("단골 고객 쿠폰 제공 화면으로 이동합니다.")
            self.vipCoupon()

        elif (selectNum == "5"):
            print("고생하셨습니다.")
            self.clear()

        elif (selectNum == "6"):
            print("Loading...")
            sleep(0.5)
            change = guest.Guest()
            print(change.show2())

        elif (selectNum == "7"):
            print("=============")
            print("앱을 종료합니다.")
            print("=============")
            sys.exit()

        else:
            print("잘못된 번호입니다.")
            self.selectstoremenu()

    def callWaiting(self):
        callNum = input("고객 호출 화면입니다. 호출 하시겠습니까? (y/n) : ")
        if len(Home.guestList) != 0:
            if callNum == "y":
                print("대기 1순위 고객님 호출했습니다.")
                del Home.guestList[0]
            else :
                print("호출을 취소합니다")
        elif len(Home.guestList) == 0:
            print("더이상 호출할 팀이 없습니다.")

    def checkNowWaiting(self):
        print("현재 웨이팅 팀 수를 보여드립니다")
        print("Loading")
        sleep(1.2)
        print("현재 웨이팅 팀 수는 %d 입니다" %(len(Home.guestList)))

    def calculator(self):
        guest_phone = input("고객님의 핸드폰번호를 입력해 주세요: ")
        Home.copyGuestCoupon = []
        aaa = 0
        for i in range(len(Home.guestCoupon)):
            Home.copyGuestCoupon.append(Home.guestCoupon[i][0])
        if guest_phone in Home.guestList and guest_phone in Home.copyGuestCoupon:
            aaa = Home.copyGuestCoupon.index(guest_phone)
            print("%s 쿠폰을 가지고 계시네요." %(Home.guestCoupon[aaa][1]))
        elif guest_phone in Home.guestList and guest_phone not in Home.copyGuestCoupon:
            print("별도의 쿠폰을 발급받지 않으셨네요.. 그대로 진행됩니다.")
        elif guest_phone not in Home.guestList:
            print("등록되지 않은 번호입니다.")





    def vipCoupon(self):
        k = int(input("방문 수 상위 몇분한테 쿠폰을 발행하실 껀가요? : "))
        kk = Counter(Home.allList).most_common(k)
        print("상위 %d 분에게 쿠폰을 발행합니다." %(k))
        for num, count in kk:
            print("%d번 방문하신 %s고객님입니다." %(count, num))

    def clear(self):
        print("오늘은 총 %d명 방문하였습니다." % (len(Home.guestList)))
        if len(Home.guestList) > 0:
            Home.guestList = []
        else :
            pass

        Home.guestCoupon = []
        Home.todayguest = []
        Home.copyGuestCoupon = []

    def show1(self):
        while(True):
            self.printstorepage()
            self.selectstoremenu()
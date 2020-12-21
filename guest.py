from time import sleep
import random
import store
from home import Home


class Guest(Home):

    def printguestpage(self):
        print("고객용 페이지에 입장하셨습니다.")

    def selectguestmenu(self):
        print("1.웨이팅 등록하기  |  2.실시간 웨이팅 확인하기  |  3.웨이팅 취소하기  |  4.오늘의 쿠폰 뽑기  |  5.관리자페이지로 이동하기(사장님용)")
        selectNum = input("원하는 메뉴 번호를 입력하세요.")

        if (selectNum == "1"):
            print("웨이팅 등록 페이지로 이동합니다. 웨이팅 등록 후 오늘의 쿠폰 뽑기를 꼭 실행시켜 주세요")
            sleep(0.5)
            self.goWaiting()

        elif (selectNum == "2"):
            print("실시간 웨이팅 확인 페이지로 이동합니다.")
            sleep(0.5)
            self.nowWaiting()

        elif (selectNum == "3"):
            print("웨이팅 취소 페이지로 이동합니다.")
            sleep(0.5)
            self.undoWaiting()

        elif (selectNum == "4"):
            print("쿠폰 뽑기 페이지로 이동합니다. 해당 페이지는 웨이팅 등록 후 이용 가능하십니다.")
            sleep(0.5)
            self.myCoupon()

        elif (selectNum == "5"):
            print("관리자용 페이지로 이동합니다")
            sleep(0.5)
            change = store.Store()
            print(change.show1())

        else:
            print("잘못된 번호입니다.")
            self.selectguestmenu()

    def goWaiting(self):
        phoneNum = input("010-0000-0000 형식으로 핸드폰 번호를 입력해 주세요.")
        if phoneNum in Home.guestList:
            print("이미 웨이팅이 등록된 번호입니다.")
        else:
            Home.guestList.append(phoneNum)
            print("등록된 웨이팅은 %d번 입니다" %(len(Guest.guestList)))
        Home.allList.append(phoneNum)

    def nowWaiting(self):
        checkNum = input("웨이팅 확인을 위해서 핸드폰 번호를 눌러주세요(010-0000-0000)")
        if checkNum in Home.guestList:
            k = Home.guestList.index(checkNum) + 1
            print("현재 웨이팅 번호는 %d입니다" %(k))
        else :
            print("웨이팅이 등록되지 않은 번호입니다. 다시 확인해 주세요.")
            self.goWaiting()

    def undoWaiting(self):
        undoNum = input(("웨이팅을 취소하실 번호를 입력해 주세요: "))
        Home.guestList.remove(undoNum)
        for i in range(len(Home.guestCoupon)):
            if Home.guestCoupon[i][0] == undoNum:
                Home.guestCoupon[i] = 0
        Home.guestCoupon.remove(0)
        sleep(2)
        print("웨이팅이 취소되었습니다.")

    def myCoupon(self):
        check_PhoneNum = input("쿠폰 뽑기를 위해 본인 확인을 진행합니다. 핸드폰 번호를 입력해 주세요 : ")
        if check_PhoneNum in Home.guestList and check_PhoneNum not in Home.todayguest:
            addlist = []
            print("확인 되셨습니다. 쿠폰 뽑기를 진행합니다....")
            randomnum = random.randrange(0, len(Home.coupon))
            sleep(0.5), print("3...")
            sleep(0.5), print("2...")
            sleep(0.5), print("1...")
            sleep(0.5), print(Home.coupon[randomnum])
            addlist.append(check_PhoneNum)
            addlist.append(Home.coupon[randomnum])
            Home.guestCoupon.append(addlist)
            Home.todayguest.append(check_PhoneNum)
            print(Home.guestCoupon)

        else:
            print("잘못된 입력값 또는 이미 쿠폰을 발급 받으신 번호입니다.")

    def show2(self):
        while(True):
            self.printguestpage()
            self.selectguestmenu()
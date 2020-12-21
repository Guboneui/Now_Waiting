import guest
import store

#클래스 호출

k = input("매장 점주님이 신가요? Y/N")
if k.lower() == "y":
    kkk = store.Store()
    print(kkk.show1())

elif k.lower() == "n":
    kkk = guest.Guest()
    print(kkk.show2())
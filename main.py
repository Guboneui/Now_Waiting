#클래스 호출
import guest
import store

k = input("매장 점주님이 신가요? Y/N")
if k.lower() == "y":
    kkk = store.Store()
    print(kkk.showStore())

elif k.lower() == "n":
    kkk = guest.Guest()
    print(kkk.showGuest())


class Home:
    coupon = ["1000원 할인쿠폰", "2000원 할인쿠폰", "3000원 할인쿠폰", "음료 공짜", "꽝"]
    guestCoupon = []        # ["핸드폰 번호", "발급받은 쿠폰"] 저장해서 2차원 배열로 생성
    guestList = []          # 당일 방문하는 고객들 담는 리스트 / clear 통해서 영업 종료시 초기화
    allList = []            # guestList 와 동일하게 저장되지만 초기화 되지 않음, 값 중복 가능. => Counter 통해서 고객 방문 횟수 확인 가능
    todayguest = []         # 쿠폰 중복 방지 용
    copyGuestCoupon = []    # 계산을 위한 복사용 리스트
from tkinter import *

root = Tk() #창을 띄울건데, 걔를 root라고 하겠다.
root.title("나도 GUI") # 창 타이틀
root.geometry("640x480")

#라디오버튼 > 여러개중 택1

#설명을 위한 label. label값 바꿀 일 없으면 뒤에 바로 pack 붙여도 됨
Label(root, text="버거를 선택하세요.").pack()

# 라디오 버튼은 택1이니 항목이 그룹으로 묶여야됨
# > 체크박스는 각 박스마다 var하나씩 썼지만, 얘는 변수 하나로 공유
burger_var=IntVar() # 뭔진 몰라도 일단 int가 들어와야해
btn_burger1= Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger2= Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
btn_burger2.select() # 디폴트 값 설정
btn_burger3= Radiobutton(root, text="치킨버거", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

# 혹시 다른 항목도 라디오 버튼으로 받고싶다면?
Label(root, text="음료를 선택하세요.").pack()

drink_var= StringVar()
btn_drink1 =Radiobutton(root, text="콜라", value="콜라", variable=drink_var )
btn_drink1.select() # 디폴트 값 설정
btn_drink2 =Radiobutton(root, text="사이다", value="사이다", variable=drink_var )
btn_drink3 =Radiobutton(root, text="환타", value="환타", variable=drink_var )

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()


def btncmd():
    print(burger_var.get()) #선택된 항목의 값(value)
    print(drink_var.get())
btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()

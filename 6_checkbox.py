from tkinter import *

root = Tk() #창을 띄울건데, 걔를 root라고 하겠다.
root.title("나도 GUI") # 창 타이틀
root.geometry("640x480")

#체크박스

#chkvar에 int 형으로 값을 저장
chkvar = IntVar()
#variable = 체크박스에서 체크했을때 값, 체크 풀었을때 값을 어떤 변수에 젖아해서 가져올수있따.
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# chkbox.select() #자동 선택 처리
# chkbox.deselect() #선택 해제 처리. 디폴트가 해제긴 하지만 체크돼있는걸 어느순간 풀어줄 수 있게됨
chkbox.pack()

chkvar2=IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지않기",variable=chkvar2)
chkbox2.pack()

def btncmd():
    #체크박스가 체크 됐는지 안됐는지 체크. 0이면 해제 1은 체크
    print(chkvar.get())
    print(chkvar2.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()

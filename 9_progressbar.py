import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk() #창을 띄울건데, 걔를 root라고 하겠다.
root.title("나도 GUI") # 창 타이틀
root.geometry("640x480")

# 진행상태 표기. 이것도 ttk에 있음

#maximum=최대 100퍼
# determinate = 왼쪽에서 오른쪽으로 차오
# indeterminate = 왼쪽 오른쪽 왔다갔다함름
# progressbar=ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10) # 10ms마다 움직임.
# progressbar.pack()

# def btncmd():
#     progressbar.stop() # 바 멈추면서 사라짐
# btn = Button(root, text="선택", command=btncmd)
# btn.pack()

p_var2=DoubleVar()
progressbar2= ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1,101):
        time.sleep(0.01) #0.01초 대기

        p_var2.set(i) #프로그레스바의 값 설정
        progressbar2.update() #for문 끝날때마다 바 위치 업데이트
        print(p_var2.get()) # 터미널에 현재 퍼센트 출력

btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()

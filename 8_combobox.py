import tkinter.ttk as ttk
from tkinter import *

root = Tk() #창을 띄울건데, 걔를 root라고 하겠다.
root.title("나도 GUI") # 창 타이틀
root.geometry("640x480")

# 드롭다운 메뉴/택1.
# 콤보박스는 그냥 tkinter말고 다른 데 있음 (맨윗줄)

# 1~31의 숫자가 n일 형태로 표기
values = [str(i) + "일" for i in range (1,32)] 
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
# 처음으로 보여줄 값 설정
combobox.set("카드 결제일") 

# 드롭다운에서 텍스트를 고쳐서 넣을 수 있음. 
# > 못하게 막아보기 (state)
readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
# 텍스트 못고치게 돼서 디플트로 임의의 값 넣을 수 없음. 
# > 인덱스로 해서 가장 처음 보여줄 값 설정
readonly_combobox.current(0)
readonly_combobox.pack()

def btncmd():
    print(combobox.get()) # 선택된 값 표기. 값 그대로 표기. 
    print(readonly_combobox.get())
btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()

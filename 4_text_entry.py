from tkinter import *

root = Tk() #창을 띄울건데, 걔를 root라고 하겠다.
root.title("나도 GUI") # 창 타이틀
root.geometry("640x480")

txt=Text(root, width=30, height=5) #텍스트 위젯 생성
txt.pack()

txt.insert(END, "글자를 입력하세요")

e=Entry(root, width=30) # 텍스트 위젯인데, 엔터 불가. 짧은거 받을때
e.pack()
e.insert(0,"한줄만!")

def btncmd():
    print(txt.get("1.0", END))
     # txt에 입력하는 모든 내용을 출력.
    # 1.0 >> 첫번째줄 0번째 위치부터 출력해라
    # 위치만 인덱스처럼 0번째로 시작하고 줄은 아닌가봄 

    print(e.get()) 
    #엔트리는 저거만 쓰면 다 가저옴, 위치 지정 불가

    #내용 삭제 > 입력창에서 지움
    txt.delete("1.0",END)
    e.delete(0,END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()

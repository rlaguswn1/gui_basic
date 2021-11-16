from tkinter import *

root = Tk()
root.title("나도 GUI") # 창 타이틀
root.geometry("640x480")

btn1=Button(root, text="버튼1")
btn1.pack() # 이거 넣어야 버튼 보임

btn2=Button(root, padx=5, pady=10, text="버튼22222222") #x여백, y여백 > 크기 유동적
btn2.pack()

btn3=Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4=Button(root, width=10, height=5, text="버튼4") #가로세로 크기 고정
btn4.pack()

btn5=Button(root, fg="red", bg="yellow", text="버튼5") #요소색, 배경색 정도 되는듯
btn5.pack()

# photo라는 변수에 이미지를 넣어놓고 걔를 버튼에서 불러서 보여주는 형식
# file= 뒤는 사진 경로인데, 같은 폴더 내에 있을때 폴더명부터 쓰면 오류남. 파일명만
photo=PhotoImage(file="image.png")
btn6=Button(root,image=photo) #사진 넣는거
btn6.pack()

def btncmd():
    print("버튼이 클릭되었당")

btn7=Button(root,text="동작하는 버튼", command=btncmd) # command= 버튼 클릭시 그 뒤를 실행시키는데, btncmd라는 함수는 "버튼이 클릭되었당"을 출력하는애 > 터미널창에 출력됨
btn7.pack()

root.mainloop()

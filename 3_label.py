from tkinter import *
click=""
root = Tk()
root.title("나도 GUI") # 창 타이틀
root.geometry("640x480")

#label: 글자나 이미지를 보여주지만, 어떤 동작을 넣어줄 수 있는 것은 아님

label1=Label(root, text="안녕하세요") #화면에 글자 출력
label1.pack()

photo=PhotoImage(file="image.png")
label2=Label(root, image=photo) # 화면에 이미지 출력. 
label2.pack()

def change():
    label1.config(text="또만나요")
    global photo2    
    # garbage collection이라는 애가 불필요한 메모리 공간을 지우고 다님
    # photo2는 이 함수가 끝나면 사용되지 않아서 불필요하다고 판단(실제로 쓰이는 데가 없다고 판단하는거 같음)
    # 전역변수(global)로 선언해야 안없어짐
    # (이게 끝나도 남아있어야하는 애구나 > 지우면 안되겠다)   

    photo2=PhotoImage(file="image2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=lambda: change())
btn.pack()

root.mainloop()

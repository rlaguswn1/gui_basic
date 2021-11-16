from tkinter import *

root = Tk() #창을 띄울건데, 걔를 root라고 하겠다.
root.title("나도 GUI") # 창 타이틀
root.geometry("640x480")

# 목록 띄우는 위젯

# selectmode는 extended외에도 많이 있으니 필요에 따라 바꿔 쓰자
# height > 리스트 몇개 보여줄건지인데 0이면 다보여줌. 짤렸을때 키보드로 내리면 더 보이긴 함
listbox = Listbox(root, selectmode="extended", height=0)
# 리스트 박스 내 내용들
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
#숫자 대신 END > 자동으로 마지막에 가서 붙음
listbox.insert(END, "포도")
listbox.insert(END, "토마토")
listbox.pack()

def btncmd():
    # 처음은 0부터 시작, 마지막걸 지우려면 END로 쓸 수 있음
    # listbox.delete(END) 

    #개수 확인
    # print("요소 몇개?", listbox.size())

    # 항목 확인 get에 시작 인덱스, 끝 인덱스
    # print("1~3번째 항목: ", listbox.get(0,2))

    # 선택된 항목 확인. 몇번째 항목 찍었는지 인덱스로 출력
    print("선택된 항목:", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()

from tkinter import *

root = Tk()
root.title("GUI")

# 버튼 위젯 생성
btn1 = Button(root, text="버튼1") #(어디에 넣을건지, 속성)
# 메인 윈도우에 포함시킴
btn1.pack()
# 버튼에 padding 값 주기
btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()
btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

# 버튼 크기 설정 (고정)
btn4 = Button(root, width=10, height=3, text="버튼4")
btn4.pack()

# 버튼 색
btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

# 이미지 불러오기
photo = PhotoImage(file="gui_basic/img.png")
# 이미지로 버튼 생성
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("사용자가 버튼을 클릭했습니다")

# 버튼에 동작 넣기
btn7 = Button(root, text="동작", command=btncmd)
btn7.pack()

root.mainloop()
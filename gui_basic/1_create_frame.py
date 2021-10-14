from tkinter import *

# root == 메인윈도우
root = Tk()
# 타이틀 설정
root.title("GUI")

# 창 크기
# root.geometry("640x480") # 가로 * 세로
root.geometry("640x480+1000+300") # 가로 * 세로 + x좌표 + y좌표

# 창 크기 변경 
root.resizable(False, False) # x(너비), y(높이) 값 변경 불가

# 무한루프
root.mainloop()
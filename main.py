import tkinter as tk
from tkinter.messagebox import Message
from datetime import datetime
import matplotlib as mat
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from PIL import Image, ImageTk
import math

mat.rcParams['font.family'] = 'Hancom Gothic' # 한글 폰트
mat.rcParams['axes.unicode_minus'] = False



def birth2date():
    try:
        return int(entry_byear.get()) * 365 + int(entry_bmonth.get()) * 30 + int(entry_bdate.get())
    except:
        Message(parent=None, title="날짜 오류", message="정수값을 입력해주세요.").show()

def check2date():
    try:
        return int(entry_checkhours.get()) * 60 + int(entry_checkminutes.get())
    except:
        Message(parent=None, title="시간 오류", message="정수값을 입력해주세요.").show()

def date2today():
    entry_checkhours.delete(0, "end")
    entry_checkminutes.delete(0, "end")
    entry_checkhours.insert(0, datetime.now().hour)
    entry_checkminutes.insert(0, datetime.now().minute)


# 그래프 그리기
def plot_graph():
    fig_size_x = 4
    fig_size_y = 4

    result_multuply_label.config(text=f'')

    # 첫번째 그래프
    diff = abs(birth2date() - check2date()) + 7

    x_max, x_min = diff + 15, diff - 15
    x = np.linspace(x_min, x_max, int((x_max - x_min) * 20))

    intel_formula = "50 * np.sin(2 * math.pi * x / 33) + 50"

    y3 =  eval(intel_formula)
    y3_min, y3_max = min(y3), max(y3)

    fig = Figure(figsize=(fig_size_x, fig_size_y), dpi=100)
    ax = fig.add_subplot(111)

    # 그래프 제목
    fig.suptitle("지능 지수", fontsize=15)

    ax.plot(x, y3, 'r', label='지성 지수')
    ax.set_xlabel('날짜 (측정 날짜를 기준으로 일수 차이)')
    ax.xaxis.set_label_coords(0.5, -0.1)
    ax.set_ylabel('지능 지수')

    x_value = diff

    y3_value = eval(intel_formula.replace("x", str(x_value)))

    ax.plot(x_value, y3_value, 'ro')
    ax.annotate(f'(0, {y3_value:.1f})', xy=(x_value, y3_value),
                xytext=(x_value + 0.2, y3_value + 0.2), fontsize=10)

    # 상태 판단 함수
    def current_status(val, upper_lim, lower_lim):
        if val < lower_lim:
            return '저조 ▼'
        elif lower_lim <= val <= upper_lim:
            return '불안정 ↯'
        else:
            return '고조 ▲'

    # 라벨 업데이트
    intel_label.config(text=f'지성 지수: {round(y3_value, 1)} ({current_status(y3_value, 75, 25)})')

    real_xval_num = np.linspace(x_min, x_max, num=31) # x축 실제 값
    display_x_value = np.linspace(-15, 15, num=31) # x축 표기용
    display_x_value_r = [] # 소수점 제거 리스트
    for i in display_x_value:
        display_x_value_r.append(round(i))
    ax.set_xticks(real_xval_num)
    ax.set_xticklabels(display_x_value_r)
    ax.tick_params(axis='x',
                   labelsize=10,
                   length=5,
                   width=1,
                   rotation=90)

    ax.hlines(y3_value, x_min, x_max, color='grey', linestyle='--', linewidth=1)

    ax.vlines(x_value, y3_min, y3_max, color='grey', linestyle='--', linewidth=1)

    ax.legend(loc='upper right') # 오른쪽 위 범례 표시


    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().place(x=60, y=100)


    #두번째 그래프
    diff_2 = abs(check2date())

    x_max_2, x_min_2 = diff_2 + 12, diff_2 - 12
    x_2 = np.linspace(x_min_2, x_max_2, int((x_max_2 - x_min_2) * 20))

    time_formula_2 = "-3/10 * np.sin(math.pi * x_2 / 12) + 7/10"

    y3_2 = eval(time_formula_2)
    y3_min_2, y3_max_2 = min(y3_2), max(y3_2)

    fig_2 = Figure(figsize=(fig_size_x, fig_size_y), dpi=100)
    ax_2 = fig_2.add_subplot(111)

    # 그래프 제목
    fig_2.suptitle("일일 지능 지수", fontsize=15)

    ax_2.plot(x_2, y3_2, 'g', label='시간 계산')
    ax_2.set_xlabel('시각 (측정 시각을 기준으로 시간 차이)')
    ax_2.xaxis.set_label_coords(0.5, -0.1)
    ax_2.set_ylabel('지능 지수')

    x_value_2 = diff_2

    # x_2 범위 내에서 x_value_2의 위치 찾기
    idx = np.abs(x_2 - x_value_2).argmin()
    x_value_2_adjusted = x_2[idx]

    y3_value_2 = eval(time_formula_2.replace("x_2", str(x_value_2_adjusted)))

    ax_2.plot(x_value_2_adjusted, y3_value_2, 'go')

    # y3_value_2 = eval(time_formula_2.replace("x", str(x_value_2)))
    #
    # ax_2.plot(x_value_2, y3_value_2, 'go')
    ax_2.annotate(f'(0, {y3_value_2:.3f})', xy=(x_value_2, y3_value_2),
                xytext=(x_value_2, y3_value_2), fontsize=10)

    real_xval_num_2 = np.linspace(x_min_2, x_max_2, num=24)  # x축 실제 값
    display_x_value_2 = np.linspace(-12, 12, num=24)  # x축 표기용
    display_x_value_r_2 = []  # 소수점 제거 리스트
    for i in display_x_value_2:
        display_x_value_r_2.append(round(i))
    ax_2.set_xticks(real_xval_num_2)
    ax_2.set_xticklabels(display_x_value_r_2)
    ax_2.tick_params(axis='x',
                   labelsize=10,
                   length=5,
                   width=1,
                   rotation=90)

    ax_2.hlines(y3_value_2, x_min_2, x_max_2, color='grey', linestyle='--', linewidth=1)

    ax_2.vlines(x_value_2, y3_min_2, y3_max_2, color='grey', linestyle='--', linewidth=1)

    ax_2.legend(loc='upper right')  # 오른쪽 위 범례 표시

    canvas_2 = FigureCanvasTkAgg(fig_2, master=window)
    canvas_2.draw()
    canvas_2.get_tk_widget().place(x=550, y=100)

    result_multuply_label.config(text=f'{round(y3_value, 3)} x {round(y3_value_2, 3)}\n'
                                      f'= {round(y3_value * y3_value_2, 3)}')


# UI 만들기
window = tk.Tk()
window.title("지능 컨디션 계산기 (Programmed by 30313 한건희)")
window.geometry("1000x650")

intel_img_orig = Image.open("equation_images/intel_formula.png")
time_img_orig = Image.open("equation_images/time_formula.png")

time_img_resized = time_img_orig.resize((250, 50))

intel_img = ImageTk.PhotoImage(intel_img_orig)
time_img = ImageTk.PhotoImage(time_img_resized)

intel_img_label = tk.Label(image=intel_img)
intel_img_label.image = intel_img
intel_img_label.place(x=130, y=520)

intel_info_label = tk.Label(window, text="지성 지수 수식", font=('Hancom Gothic', 12))
intel_info_label.place(x=180, y=590)

time_img_label = tk.Label(image=time_img)
time_img_label.image = time_img
time_img_label.place(x=630, y=520)

time_info_label = tk.Label(window, text="시간 계산 수식", font=('Hancom Gothic', 12))
time_info_label.place(x=700, y=590)

result_multuply_label = tk.Label(window, text="", font=('Hancom Gothic', 15))
result_multuply_label.place(x=420, y=520)

result_multuply_info_label = tk.Label(window, text="지능 지수 X 일일 지능 지수", font=('Hancom Gothic', 12))
result_multuply_info_label.place(x=400, y=590)


# 입력 필드 추가
entry_byear = tk.Entry(window)
entry_byear.insert(0, "측정할 년도(4자리)")
entry_byear.place(x=10, y=10)

entry_bmonth = tk.Entry(window)
entry_bmonth.insert(0, "측정할 달(1자리 혹은 2자리)")
entry_bmonth.place(x=160, y=10)

entry_bdate = tk.Entry(window)
entry_bdate.insert(0, "측정할 일(1자리 혹은 2자리)")
entry_bdate.place(x=310, y=10)

entry_checkhours = tk.Entry(window)
entry_checkhours.insert(0, "측정할 시간(0 ~ 24)")
entry_checkhours.place(x=10, y=40)

entry_checkminutes = tk.Entry(window)
entry_checkminutes.insert(0, "측정할 분(0 ~ 59)")
entry_checkminutes.place(x=160, y=40)


# 버튼 추가
plot_button = tk.Button(window, text="그래프 그리기", command=plot_graph)
plot_button.place(x=460, y=10)

today_button = tk.Button(window, text="현재 시각으로", command=date2today)
today_button.place(x=460, y=40)

intel_label = tk.Label(window, text="지성 지수:", foreground='red', font=('Hancom Gothic', 15))
intel_label.place(x=700, y=40)

# UI 실행
window.mainloop()
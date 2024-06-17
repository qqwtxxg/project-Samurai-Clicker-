import time
import tkinter
from tkinter import *
from tkinter import ttk
import time
import threading

img_samurai = 0
img_samurai2 = 0
img_samurai3 = 0
img_samurai4 = 0
img_samurai5 = 0
img_samurai6 = 0
img_samurai7 = 0
img_samurai8 = 0
table_img = 0
table2_img = 0
"""очищаем экран, для перехода в игру"""
def start_game():
    global img_samurai
    global table_img
    global table2_img
    continue_btn7.destroy()
    canvas.delete('all')
    img_sector = canvas.create_image(0, 0, anchor='nw', image = g_sector)
    img_samurai = canvas.create_image(0, 0, anchor = 'nw', image = samurai)
    coin.place(x = 740/2 - 30, y = 800)
    helmet_btn.place(x = 110, y = 500)
    """ЗАМКИ ДЛЯ БРОНИ"""
    lock1_btn.place(x=180, y=501)
    lock2_btn.place(x = 250, y = 501)
    lock3_btn.place(x = 320, y = 501)
    lock4_btn.place(x = 390, y = 501)
    lock5_btn.place(x = 460, y = 501)
    lock6_btn.place(x = 530, y = 501)
    """ЗАМКИ ДЛЯ СКИЛЛОВ"""
    lock7_btn.place(x=180, y=650)
    lock8_btn.place(x = 250, y = 650)
    lock9_btn.place(x = 320, y = 650)
    lock10_btn.place(x = 390, y = 650)
    lock11_btn.place(x = 460, y = 650)
    lock12_btn.place(x = 530, y = 650)
    """ЦЕННИКИ"""
    helmet_price.place(x = 120, y = 580)
    skill1_price.place(x = 120, y = 730)

    skill1_btn.place(x = 110, y = 650)

    score_img = canvas.create_image(10, 10, anchor='nw', image=score)
    score_label.place(x = 50, y = 25)
    table_img = canvas.create_image(60, 450, anchor = 'nw', image = table)
    table2_img = canvas.create_image(60, 600, anchor='nw', image=table2)
    timer_img = canvas.create_image(546, 818, anchor='nw', image=timer_table)
    buff_timer()


def akira_message1():
    play.destroy()
    end.destroy()
    img_message1 = canvas.create_image(0, 0, anchor='nw', image=start_message1)
    continue_btn1.place(x = 300, y = 570)

def akira_message2():
    canvas.delete('all')
    continue_btn1.destroy()
    img_message2 = canvas.create_image(0, 0, anchor='nw', image=start_message2)
    continue_btn2.place(x = 300, y = 570)

def kioshi_message1():
    canvas.delete('all')
    continue_btn2.destroy()
    img_message2 = canvas.create_image(0, 0, anchor='nw', image=start_message3)
    continue_btn3.place(x = 300, y = 570)

def rules_one():
    canvas.delete('all')
    continue_btn3.destroy()
    img_message3 = canvas.create_image(0, 0, anchor='nw', image=rules1)
    continue_btn4.place(x = 300, y = 570)

def rules_two():
    canvas.delete('all')
    continue_btn4.destroy()
    img_message4 = canvas.create_image(0, 0, anchor='nw', image=rules2)
    continue_btn5.place(x = 300, y = 570)

def rules_three():
    canvas.delete('all')
    continue_btn5.destroy()
    img_message5 = canvas.create_image(0, 0, anchor='nw', image=rules3)
    continue_btn6.place(x = 300, y = 570)

def rules_four():
    canvas.delete('all')
    continue_btn6.destroy()
    img_message5 = canvas.create_image(0, 0, anchor='nw', image=rules4)
    continue_btn7.place(x = 300, y = 570)

current_number = 0

"""Функция, отвечающая за заработок денег и бафы к этому заработку"""
def update_score():
    global current_number
    current_number += 1
    if "helmet_btn" in globals() and not helmet_btn.winfo_exists():
        current_number += 1
    if 'body_btn' in globals() and not body_btn.winfo_exists():
        current_number += 3
    if 'legs_btn' in globals() and not legs_btn.winfo_exists():
        current_number += 5
    if 'arms_btn' in globals() and not arms_btn.winfo_exists():
        current_number += 5
    if 'boots_btn' in globals() and not boots_btn.winfo_exists():
        current_number += 5
    if 'katana_btn' in globals() and not katana_btn.winfo_exists():
        current_number += 5
    if 'heal_btn' in globals() and not heal_btn.winfo_exists():
        current_number += 5
    if not buff_button_active.winfo_ismapped():
        current_number += 9
        if not active_buff_label.winfo_ismapped():
            current_number -= 9

    score_label.config(text = str(current_number))

points2 = 0
def add_points(points):
    global current_number
    global points2
    current_number += points2
    score_label.config(text = str(current_number))
    if current_number < points:
        return
    window.after(1000, lambda: add_points(points))



def buff_timer(): #Ведущий таймер, до активации бафа
    if "end2" in globals() and not end2.winfo_exists():
        return
    buff_button_afk.place(x=450, y=810)
    buff_label.place(x=560, y=830)
    buff_current_number = int(buff_label["text"])
    buff_new_number = buff_current_number + 1
    buff_label["text"] = str(buff_new_number)
    buff_label.update()
    if int(buff_label["text"]) < 60:
        window.after(1000, buff_timer)
    if buff_label["text"] == '60':
        buff_button_afk.place_forget()
        buff_label.place_forget()
        buff_button_active.place(x = 450, y = 810)
        buff_label["text"] = "0"


def call_function():
    buff_timer()

"""Функция, отвечающая за покупку шлема"""
def buy_helmet(points):
    global img_samurai
    global current_number
    global img_samurai2
    if current_number >= points:
        helmet_btn.destroy()
        current_number -= points
        score_label.config(text = str(current_number))
        lock1_btn.destroy()
        body_btn.place(x=180, y=501)
        helmet_price.destroy()
        body_price.place(x = 190, y = 580)
        canvas.delete(img_samurai)
        img_samurai2 = canvas.create_image(0, 0, anchor='nw', image=samurai2)
        score_img = canvas.create_image(10, 10, anchor='nw', image=score)

"""Функция, отвечающая за покупку брони"""
def buy_body(points):
    global current_number
    global img_samurai3
    global img_samurai2
    if current_number >= points:
        body_btn.destroy()
        current_number -= points
        score_label.config(text = str(current_number))
        lock2_btn.destroy()
        legs_btn.place(x = 250, y = 501)
        body_price.destroy()
        legs_price.place(x = 260, y = 580)
        canvas.delete(img_samurai2)
        img_samurai3 = canvas.create_image(0, 0, anchor='nw', image=samurai3)
        score_img = canvas.create_image(10, 10, anchor='nw', image=score)

"""Функция, отвечающая за покупку ног"""
def buy_legs(points):
    global current_number
    global img_samurai3
    global img_samurai4
    if current_number >= points:
        legs_btn.destroy()
        current_number -= points
        score_label.config(text = str(current_number))
        lock3_btn.destroy()
        arms_btn.place(x=320, y=501)
        legs_price.destroy()
        arms_price.place(x = 330, y = 580)
        canvas.delete(img_samurai3)
        img_samurai4 = canvas.create_image(0, 0, anchor='nw', image=samurai4)
        score_img = canvas.create_image(10, 10, anchor='nw', image=score)

"""Функция, отвечающая за покупку рук"""
def buy_arms(points):
    global img_samurai4
    global img_samurai5
    global current_number
    if current_number >= points:
        arms_btn.destroy()
        current_number -= points
        score_label.config(text = str(current_number))
        lock4_btn.destroy()
        boots_btn.place(x = 390, y = 501)
        arms_price.destroy()
        boots_price.place(x = 400, y = 580)
        canvas.delete(img_samurai4)
        img_samurai5 = canvas.create_image(0, 0, anchor='nw', image=samurai5)
        score_img = canvas.create_image(10, 10, anchor='nw', image=score)

"""Функция, отвечающая за покупку ботинков"""
def buy_boots(points):
    global img_samurai6
    global img_samurai5
    global current_number
    if current_number >= points:
        boots_btn.destroy()
        current_number -= points
        score_label.config(text = str(current_number))
        lock5_btn.destroy()
        katana_btn.place(x = 460, y = 501)
        boots_price.destroy()
        katana_price.place(x = 470, y = 580)
        canvas.delete(img_samurai5)
        img_samurai3 = canvas.create_image(0, 0, anchor='nw', image=samurai6)
        score_img = canvas.create_image(10, 10, anchor='nw', image=score)

"""Функция, отвечающая за покупку катаны"""
def buy_katana(points):
    global img_samurai6
    global img_samurai7
    global current_number
    if current_number >= points:
        katana_btn.destroy()
        current_number -= points
        score_label.config(text = str(current_number))
        lock6_btn.destroy()
        heal_btn.place(x = 530, y = 501)
        katana_price.destroy()
        heal_price.place(x = 540, y = 580)
        canvas.delete(img_samurai6)
        img_samurai7 = canvas.create_image(0, 0, anchor='nw', image=samurai7)
        score_img = canvas.create_image(10, 10, anchor='nw', image=score)

"""Функция, отвечающая за покупку аптечки"""
def buy_heal(points):
    global img_samurai7
    global img_samurai8
    global current_number
    if current_number >= points:
        heal_btn.destroy()
        current_number -= points
        score_label.config(text = str(current_number))
        heal_price.destroy()
        canvas.delete(img_samurai7)
        img_samurai8 = canvas.create_image(0, 0, anchor='nw', image=samurai8)
        score_img = canvas.create_image(10, 10, anchor='nw', image=score)
        if 'heal_btn' in globals() and not heal_btn.winfo_exists() and "skill7_btn" in globals() and not skill7_btn.winfo_exists():
                delete_tables()
                end2.place(x=270, y=650)
def delete_tables():
    canvas.delete(table_img)
    canvas.delete(table2_img)

def buy_skill1(points):
    global current_number
    global points2
    if current_number >= points:
        skill1_btn.destroy()
        current_number -= points
        score_label.config(text = str(current_number))
        points2 = 1
        add_points(1)
        in_sec.place(x = 140, y = 830)
        in_sec.config(text=f'in second +{points2}')
        colvo_table_img = canvas.create_image(125, 816, anchor='nw', image=colvo_table)
        lock7_btn.destroy()
        skill2_btn.place(x = 180, y = 650)
        skill1_price.destroy()
        skill2_price.place(x = 190, y = 730)

def buy_skill2(points):
    global current_number
    global points2
    if current_number >= points:
        skill2_btn.destroy()
        current_number -= points
        score_label.config(text = str(current_number))
        points2 = 5
        in_sec.config(text = f'in second + {points2}')
        lock8_btn.destroy()
        skill3_btn.place(x=250, y=650)
        skill2_price.destroy()
        skill3_price.place(x = 260, y = 730)

def buy_skill3(points):
    global current_number
    global points2
    if current_number >= points:
        skill3_btn.destroy()
        current_number -= points
        score_label.config(text = str(current_number))
        points2 = 10
        in_sec.config(text=f'in second +{points2}')
        lock9_btn.destroy()
        skill4_btn.place(x=320, y=650)
        skill3_price.destroy()
        skill4_price.place(x = 330, y = 730)

def buy_skill4(points):
    global current_number
    global points2
    if current_number >= points:
        skill4_btn.destroy()
        current_number -= points
        score_label.config(text = str(current_number))
        points2 = 15
        in_sec.config(text=f'in second +{points2}')
        lock10_btn.destroy()
        skill5_btn.place(x=390, y=650)
        skill4_price.destroy()
        skill5_price.place(x = 400, y = 730)

def buy_skill5(points):
    global current_number
    global points2
    if current_number >= points:
        skill5_btn.destroy()
        current_number -= points
        score_label.config(text = str(current_number))
        points2 = 20
        in_sec.config(text=f'in second +{points2}')
        lock11_btn.destroy()
        skill6_btn.place(x=460, y=650)
        skill5_price.destroy()
        skill6_price.place(x = 470, y = 730)

def buy_skill6(points):
    global current_number
    global points2
    if current_number >= points:
        skill6_btn.destroy()
        current_number -= points
        score_label.config(text = str(current_number))
        points2 = 25
        in_sec.config(text=f'in second +{points2}')
        lock12_btn.destroy()
        skill7_btn.place(x=530, y=650)
        skill6_price.destroy()
        skill7_price.place(x = 540, y = 730)

def buy_skill7(points):
    global current_number
    global points2
    if current_number >= points:
        skill7_btn.destroy()
        current_number -= points
        score_label.config(text = str(current_number))
        points2 = 30
        in_sec.config(text=f'in second +{points2}')
        skill7_price.destroy()
        if 'skill7_btn' in globals() and not skill7_btn.winfo_exists() and "heal_btn" in globals() and not heal_btn.winfo_exists():
                delete_tables()
                end2.place(x = 270, y = 650)


"""Временный баф на кол-во кликов"""
def get_buff():
    buff_button_active.place_forget()
    buff_button_on.place(x = 433, y = 792)
    active_buff_label.place(x=560, y=830)
    active_current_number = int(active_buff_label["text"])
    active_new_number = active_current_number - 1
    active_buff_label["text"] = str(active_new_number)
    active_buff_label.update()
    if int(active_buff_label["text"]) > 0:
        window.after(1000, get_buff)
    if active_buff_label["text"] == '0':
        active_buff_label.place_forget()
        buff_button_on.place_forget()
        buff_timer()
        active_buff_label["text"] = '15'

def end_akira():
    canvas.delete('all')
    end2.destroy()
    img_end1 = canvas.create_image(0, 0, anchor='nw', image=end_message1)
    continue_btn9.place(x = 300, y = 700)
    score_label.place_forget()
    score_label.place_forget()
    in_sec.place_forget()
    active_buff_label.place_forget()
    coin.destroy()
    buff_button_afk.destroy()
    buff_button_active.destroy()
    active_buff_label.place_forget()
    buff_label.place_forget()

def end_akira2():
    canvas.delete('all')
    continue_btn9.destroy()
    continue_btn10.place(x=300, y=700)
    img_end2 = canvas.create_image(0, 0, anchor='nw', image=end_message2)

def end_akira3():
    canvas.delete('all')
    continue_btn10.destroy()
    end_exit.place(x = 220, y = 700)
    img_end2 = canvas.create_image(0, 0, anchor='nw', image=end_message3)

window = Tk()
window.title('Samurai Clicker')
window.geometry('740x900+450+50')
window.resizable(width = False, height = False)
canvas = Canvas(window, width = 740, height = 900, highlightthickness = 0)
canvas.pack()


g_sector = PhotoImage(file ='images/Game_sector.png')
play_btn = PhotoImage(file ='images/btn_play.png')
exit_btn = PhotoImage(file ='images/btn_exit.png')
coin_btn = PhotoImage(file ='images/coin_btn.png')

"""КАРТИНКИ САМУРАЯ"""
samurai = PhotoImage(file ='images/samurai1.png')
samurai2 = PhotoImage(file ='images/samurai2.png')
samurai3 = PhotoImage(file ='images/samurai3.png')
samurai4 = PhotoImage(file ='images/samurai4.png')
samurai5 = PhotoImage(file ='images/samurai5.png')
samurai6 = PhotoImage(file ='images/samurai6.png')
samurai7 = PhotoImage(file ='images/samurai7.png')
samurai8 = PhotoImage(file ='images/samurai8.png')

"""ВСТУПИТЕЛЬНЫЕ СООБЩЕНИЯ"""
start_message1 = PhotoImage(file ='images/start_message1.png')
start_message2 = PhotoImage(file ='images/start_message2.png')
start_message3 = PhotoImage(file ='images/start_message3.png')
rules1 = PhotoImage(file ='images/rules1.png')
rules2 = PhotoImage(file ='images/rules2.png')
rules3 = PhotoImage(file ='images/rules3.png')
rules4 = PhotoImage(file ='images/rules4.png')
continue_img = PhotoImage(file ='images/continue_btn.png')

"""ЗАКЛЮЧИТЕЛЬНЫЕ СООБЩЕНИЯ"""
end_message1 = PhotoImage(file ='images/end_message1.png')
end_message2 = PhotoImage(file ='images/end_message2.png')
end_message3 = PhotoImage(file ='images/end_message3.png')

back = PhotoImage(file ='images/back.png')
score = PhotoImage(file ='images/score_btn.png')
table = PhotoImage(file ='images/table.png')
table2 = PhotoImage(file ='images/table.png')
helmet = PhotoImage(file ='images/helmet_btn.png')
body = PhotoImage(file ='images/body_btn.png')
legs = PhotoImage(file ='images/legs_btn.png')
arms = PhotoImage(file ='images/arms_btn.png')
boots = PhotoImage(file ='images/boots_btn.png')
katana = PhotoImage(file ='images/katana_btn.png')
heal = PhotoImage(file ='images/heal_btn.png')
afk_buff = PhotoImage(file ='images/afk_buff_btn.png')
active_buff = PhotoImage(file ='images/active_buff_btn.png')
switch_on_buff = PhotoImage(file ='images/switch_on_buff_btn.png')
timer_table = PhotoImage(file ='images/timer.png')
colvo_table = PhotoImage(file ='images/colvo_insec.png')
lock = PhotoImage(file ='images/lock_btn.png')
end1 = PhotoImage(file ='images/end_btn.png')

"""Файлы с фотками скиллов"""
skill1 = PhotoImage(file ='images/skill1.png')
skill2 = PhotoImage(file ='images/skill2.png')
skill3 = PhotoImage(file ='images/skill3.png')
skill4 = PhotoImage(file ='images/skill4.png')
skill5 = PhotoImage(file ='images/skill5.png')
skill6 = PhotoImage(file ='images/skill6.png')
skill7 = PhotoImage(file ='images/skill7.png')


img1 = canvas.create_image(0,0, anchor = 'nw', image = back)


play = Button(window, image=play_btn, highlightthickness = 0, bd = 0,
              bg = 'black', activebackground = 'black', command = akira_message1)
end = Button(window, image=exit_btn, highlightthickness = 0, bd = 0,
             bg = 'black', activebackground = 'black', command = window.quit)
coin = Button(window, image = coin_btn, highlightthickness = 0, bd = 0, bg = '#696a6a', activebackground = '#696a6a',
              command = update_score)
helmet_btn = Button(window, image = helmet, highlightthickness = 0, bd = 0, bg = '#663931', activebackground = '#663931',
              command = lambda: buy_helmet(500))
body_btn = Button(window, image = body, highlightthickness = 0, bd = 0, bg = '#663931', activebackground = '#663931',
              command = lambda: buy_body(1500))
legs_btn = Button(window, image = legs, highlightthickness = 0, bd = 0, bg = '#663931', activebackground = '#663931',
                  command = lambda: buy_legs(2500))
arms_btn = Button(window, image = arms, highlightthickness = 0, bd = 0, bg = '#663931', activebackground = '#663931',
                  command = lambda: buy_arms(3500))
boots_btn = Button(window, image = boots, highlightthickness = 0, bd = 0, bg = '#663931', activebackground = '#663931',
                  command = lambda: buy_boots(5000))
katana_btn = Button(window, image = katana, highlightthickness = 0, bd = 0, bg = '#663931', activebackground = '#663931',
                  command = lambda: buy_katana(7000))
heal_btn = Button(window, image = heal, highlightthickness = 0, bd = 0, bg = '#663931', activebackground = '#663931',
                  command = lambda: buy_heal(10000))
continue_btn1 = Button(window, image = continue_img, highlightthickness = 0, bd = 0, bg = 'black',
                       activebackground = 'black', command = akira_message2)
continue_btn2 = Button(window, image = continue_img, highlightthickness = 0, bd = 0, bg = 'black',
                       activebackground = 'black', command = kioshi_message1)
continue_btn3 = Button(window, image = continue_img, highlightthickness = 0, bd = 0, bg = 'black',
                       activebackground = 'black', command = rules_one)
continue_btn4 = Button(window, image = continue_img, highlightthickness = 0, bd = 0, bg = 'black',
                       activebackground = 'black', command = rules_two)
continue_btn5 = Button(window, image = continue_img, highlightthickness = 0, bd = 0, bg = 'black',
                       activebackground = 'black', command = rules_three)
continue_btn6 = Button(window, image = continue_img, highlightthickness = 0, bd = 0, bg = 'black',
                       activebackground = 'black', command = rules_four)
continue_btn7 = Button(window, image = continue_img, highlightthickness = 0, bd = 0, bg = 'black',
                       activebackground = 'black', command = start_game)
continue_btn8 = Button(window, image = continue_img, highlightthickness = 0, bd = 0, bg = 'black',
                       activebackground = 'black', command = start_game)
continue_btn9 = Button(window, image = continue_img, highlightthickness = 0, bd = 0, bg = 'black',
                       activebackground = 'black', command = end_akira2)
continue_btn10 = Button(window, image = continue_img, highlightthickness = 0, bd = 0, bg = 'black',
                       activebackground = 'black', command = end_akira3)
end2 = Button(window, image = end1, highlightthickness = 0, bd = 0, bg = '#696a6a',
                       activebackground = '#696a6a', command = end_akira)
end_exit = Button(window, image = exit_btn, highlightthickness = 0, bd = 0, bg = 'black',
                       activebackground = 'black', command = window.quit)

"""ЗАМКИ"""
lock1_btn = Button(window, image = lock, highlightthickness = 0, bd = 0, bg = '#663931', activebackground = '#663931')
lock2_btn = Button(window, image = lock, highlightthickness = 0, bd = 0, bg = '#663931', activebackground = '#663931')
lock3_btn = Button(window, image = lock, highlightthickness = 0, bd = 0, bg = '#663931', activebackground = '#663931')
lock4_btn = Button(window, image = lock, highlightthickness = 0, bd = 0, bg = '#663931', activebackground = '#663931')
lock5_btn = Button(window, image = lock, highlightthickness = 0, bd = 0, bg = '#663931', activebackground = '#663931')
lock6_btn = Button(window, image = lock, highlightthickness = 0, bd = 0, bg = '#663931', activebackground = '#663931')
lock7_btn = Button(window, image = lock, highlightthickness = 0, bd = 0, bg = '#663931', activebackground = '#663931')
lock8_btn = Button(window, image = lock, highlightthickness = 0, bd = 0, bg = '#663931', activebackground = '#663931')
lock9_btn = Button(window, image = lock, highlightthickness = 0, bd = 0, bg = '#663931', activebackground = '#663931')
lock10_btn = Button(window, image = lock, highlightthickness = 0, bd = 0, bg = '#663931', activebackground = '#663931')
lock11_btn = Button(window, image = lock, highlightthickness = 0, bd = 0, bg = '#663931', activebackground = '#663931')
lock12_btn = Button(window, image = lock, highlightthickness = 0, bd = 0, bg = '#663931', activebackground = '#663931')

"""СКИЛЛЫ"""
skill1_btn = Button(window, image = skill1, highlightthickness = 0, bd = 0, bg = '#663931', activebackground = '#663931',
                    command = lambda: buy_skill1(1000))
skill2_btn = Button(window, image = skill2, highlightthickness = 0, bd = 0, bg = '#663931', activebackground = '#663931',
                    command = lambda: buy_skill2(2000))
skill3_btn = Button(window, image = skill3, highlightthickness = 0, bd = 0, bg = '#663931', activebackground = '#663931',
                    command = lambda: buy_skill3(5000))
skill4_btn = Button(window, image = skill4, highlightthickness = 0, bd = 0, bg = '#663931', activebackground = '#663931',
                    command = lambda: buy_skill4(7000))
skill5_btn = Button(window, image = skill5, highlightthickness = 0, bd = 0, bg = '#663931', activebackground = '#663931',
                    command = lambda: buy_skill5(9000))
skill6_btn = Button(window, image = skill6, highlightthickness = 0, bd = 0, bg = '#663931', activebackground = '#663931',
                    command = lambda: buy_skill6(11000))
skill7_btn = Button(window, image = skill7, highlightthickness = 0, bd = 0, bg = '#663931', activebackground = '#663931',
                    command = lambda: buy_skill7(13000))

buff_button_afk = Button(window, image = afk_buff, highlightthickness = 0, bd = 0, bg = '#696a6a',
                         activebackground = '#696a6a')

buff_button_active = Button(window, image = active_buff, highlightthickness = 0, bd = 0, bg = '#696a6a',
                            activebackground = '#696a6a', command = get_buff)

buff_button_on = Button(window, image = switch_on_buff, highlightthickness = 0, bd = 0, bg = '#696a6a',
                        activebackground = '#696a6a')

score_label = tkinter.Label(window, font = ('Minecraft Rus', 20), text = '0', highlightthickness = 0, bd = 0,
                            bg = '#eec39a',
                            activebackground = '#eec39a')

buff_label = tkinter.Label(window, font = ('Minecraft Rus', 15), text = '0', highlightthickness = 0, bd = 0,
                            bg = '#eec39a',
                            activebackground = '#eec39a', fg = 'black')

in_sec = tkinter.Label(window, font = ('Minecraft Rus', 12), text = f'in second +{points2}', highlightthickness = 0, bd = 0,
                            bg = '#eec39a',
                            activebackground = '#eec39a', fg = 'black')

active_buff_label = tkinter.Label(window, font = ('Minecraft Rus', 15), text = '15', highlightthickness = 0, bd = 0,
                            bg = '#eec39a',
                            activebackground = '#696a6a', fg = 'black')

"""ЦЕННИКИ"""
helmet_price = tkinter.Label(window,font = ('Minecraft Rus', 12), text = "500$", highlightthickness = 0, bd = 0,
                            bg = '#696a6a',
                            activebackground = '#696a6a', fg = 'white')

skill1_price = tkinter.Label(window,font = ('Minecraft Rus', 12), text = "1000$", highlightthickness = 0, bd = 0,
                            bg = '#696a6a',
                            activebackground = '#696a6a', fg = 'white')

body_price = tkinter.Label(window,font = ('Minecraft Rus', 12), text = "1500$", highlightthickness = 0, bd = 0,
                            bg = '#696a6a',
                            activebackground = '#696a6a', fg = 'white')

skill2_price = tkinter.Label(window,font = ('Minecraft Rus', 12), text = "2000$", highlightthickness = 0, bd = 0,
                            bg = '#696a6a',
                            activebackground = '#696a6a', fg = 'white')

legs_price = tkinter.Label(window,font = ('Minecraft Rus', 12), text = "2500$", highlightthickness = 0, bd = 0,
                            bg = '#696a6a',
                            activebackground = '#696a6a', fg = 'white')

skill3_price = tkinter.Label(window,font = ('Minecraft Rus', 12), text = "5000$", highlightthickness = 0, bd = 0,
                            bg = '#696a6a',
                            activebackground = '#696a6a', fg = 'white')

arms_price = tkinter.Label(window,font = ('Minecraft Rus', 12), text = "3500$", highlightthickness = 0, bd = 0,
                            bg = '#696a6a',
                            activebackground = '#696a6a', fg = 'white')

skill4_price = tkinter.Label(window,font = ('Minecraft Rus', 12), text = "7000$", highlightthickness = 0, bd = 0,
                            bg = '#696a6a',
                            activebackground = '#696a6a', fg = 'white')

boots_price = tkinter.Label(window,font = ('Minecraft Rus', 12), text = "5000$", highlightthickness = 0, bd = 0,
                            bg = '#696a6a',
                            activebackground = '#696a6a', fg = 'white')

skill5_price = tkinter.Label(window,font = ('Minecraft Rus', 12), text = "9000$", highlightthickness = 0, bd = 0,
                            bg = '#696a6a',
                            activebackground = '#696a6a', fg = 'white')

katana_price = tkinter.Label(window,font = ('Minecraft Rus', 12), text = "7000$", highlightthickness = 0, bd = 0,
                            bg = '#696a6a',
                            activebackground = '#696a6a', fg = 'white')

skill6_price = tkinter.Label(window,font = ('Minecraft Rus', 12), text = "11000$", highlightthickness = 0, bd = 0,
                            bg = '#696a6a',
                            activebackground = '#696a6a', fg = 'white')

heal_price = tkinter.Label(window,font = ('Minecraft Rus', 12), text = "10000$", highlightthickness = 0, bd = 0,
                            bg = '#696a6a',
                            activebackground = '#696a6a', fg = 'white')

skill7_price = tkinter.Label(window,font = ('Minecraft Rus', 12), text = "13000$", highlightthickness = 0, bd = 0,
                            bg = '#696a6a',
                            activebackground = '#696a6a', fg = 'white')


play.place(x = 15, y = 620)
end.place(x = 410, y = 620)



window.mainloop()
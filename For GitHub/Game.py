import tkinter
from tkinter import *
from tkinter import ttk

"""очищаем экран, для перехода в игру"""
def start_game():
    canvas.delete('all')
    play.destroy()
    end.destroy()
    img_sector = canvas.create_image(0, 0, anchor='nw', image = g_sector)
    img_samurai = canvas.create_image(0, 0, anchor = 'nw', image = samurai)
    coin.place(x = 740/2 - 30, y = 800)
    helmet_btn.place(x = 110, y = 500)
    body_btn.place(x=180, y=502)
    score_img = canvas.create_image(10, 10, anchor='nw', image=score)
    score_label.place(x = 50, y = 25)
    table_img = canvas.create_image(60, 450, anchor = 'nw', image = table)
    table2_img = canvas.create_image(60, 600, anchor='nw', image=table2)


"""Функция, отвечающая за заработок денег и бафы к этому заработку"""
def update_score():
    current_number = int(score_label["text"])
    new_number = current_number + 1
    if "helmet_btn" in globals() and not helmet_btn.winfo_exists():
        new_number += 1
    if 'body_btn' in globals() and not body_btn.winfo_exists():
        new_number += 3

    score_label["text"] = str(new_number)


"""Функция, отвечающая за покупку шлема"""
def buy_helmet():
    if int(score_label["text"]) >= 10:
        helmet_btn.destroy()
        score_label["text"] = int(score_label["text"]) - 10
        helmet_check = helmet_btn.winfo_exists()


def buy_body():
    if int(score_label["text"]) >= 20:
        body_btn.destroy()
        score_label["text"] = int(score_label["text"]) - 10



window = Tk()
window.title('Samurai Clicker')
window.geometry('740x900+450+50')
window.resizable(width = False, height = False)
canvas = Canvas(window, width = 740, height = 900, highlightthickness = 0)
canvas.pack()


g_sector = PhotoImage(file = 'Game_sector.png')
play_btn = PhotoImage(file = 'btn_play.png')
exit_btn = PhotoImage(file = 'btn_exit.png')
coin_btn = PhotoImage(file = 'coin_btn.png')
samurai = PhotoImage(file = 'samurai.png')
back = PhotoImage(file = 'back.png')
score = PhotoImage(file = 'score_btn.png')
table = PhotoImage(file = 'table.png')
table2 = PhotoImage(file = 'table.png')
helmet = PhotoImage(file = 'helmet_btn.png')
body = PhotoImage(file = 'body_btn.png')

img1 = canvas.create_image(0,0, anchor = 'nw', image = back)


play = Button(window, image=play_btn, highlightthickness = 0, bd = 0,
              bg = 'black', activebackground = 'black', command = start_game)
end = Button(window, image=exit_btn, highlightthickness = 0, bd = 0,
             bg = 'black', activebackground = 'black', command = window.quit)
coin = Button(window, image = coin_btn, highlightthickness = 0, bd = 0, bg = '#696a6a', activebackground = '#696a6a',
              command = update_score)
helmet_btn = Button(window, image = helmet, highlightthickness = 0, bd = 0, bg = '#663931', activebackground = '#663931',
              command = buy_helmet)
body_btn = Button(window, image = body, highlightthickness = 0, bd = 0, bg = '#663931', activebackground = '#663931',
              command = buy_body)


score_label = tkinter.Label(window, font = ('Minecraft Rus', 20), text = '0', highlightthickness = 0, bd = 0,
                            bg = '#eec39a',
                            activebackground = '#eec39a')


play.place(x = 15, y = 620)
end.place(x = 410, y = 620)


window.mainloop()
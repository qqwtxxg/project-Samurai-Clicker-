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

img1 = canvas.create_image(0,0, anchor = 'nw', image = back)


play = Button(window, image=play_btn, highlightthickness = 0, bd = 0,
              bg = 'black', activebackground = 'black', command = start_game)
end = Button(window, image=exit_btn, highlightthickness = 0, bd = 0,
             bg = 'black', activebackground = 'black', command = window.quit)
coin = Button(window, image = coin_btn, highlightthickness = 0, bd = 0, bg = '#FFFdd3', activebackground = '#FFFdd3')

play.place(x = 15, y = 620)
end.place(x = 410, y = 620)


window.mainloop()
# @author azsy, 6/27/19 to 6/29/19
from tkinter import *

# btnclick is used to determine whether a button text will be 'X' or 'O'
btnclick = True

# all 9 buttons of the tic tac toe game will use the function when determing X or O
def buttons(button):            # parameter is a button since the button text will display X or O
    global btnclick             # uses global keyword since btnclick will change values in the function
    es["state"] = "disabled"    # as soon a player marks a button, the swap button will become disabled

    if button["text"] == " " and btnclick == True:
        l1["text"] = "Player O's Turn"
        button["text"] = "X"
        btnclick = False
        check_x()
        if l1["text"] != "Player X wins!!!":
            check_draw()

    elif button["text"] == " " and btnclick == False:
        l1["text"] = "Player X's Turn"
        button["text"] = "O"
        btnclick = True
        check_o()
        if l1["text"] != "Player O wins!!!":
            check_draw()

def check_x():
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":  #b1 b2 b3
        l1["text"] = "Player X wins!!!"
        d_b()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X": #b4 b5 b6
        l1["text"] = "Player X wins!!!"
        d_b()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X": #b7 b8 b9
        l1["text"] = "Player X wins!!!"
        d_b()
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X": #b1 b4 b7
        l1["text"] = "Player X wins!!!"
        d_b()
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X": #b2 b5 b8
        l1["text"] = "Player X wins!!!"
        d_b()
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X": #b3 b6 b9
        l1["text"] = "Player X wins!!!"
        d_b()
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        l1["text"] = "Player X wins!!!"
        d_b()
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        l1["text"] = "Player X wins!!!"
        d_b()

def check_o():
    if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":  #b1 b2 b3
        l1["text"] = "Player O wins!!!"
        d_b()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O": #b4 b5 b6
        l1["text"] = "Player O wins!!!"
        d_b()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O": #b7 b8 b9
        l1["text"] = "Player O wins!!!"
        d_b()
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O": #b1 b4 b7
        l1["text"] = "Player O wins!!!"
        d_b()
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O": #b2 b5 b8
        l1["text"] = "Player O wins!!!"
        d_b()
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O": #b3 b6 b9
        l1["text"] = "Player O wins!!!"
        d_b()
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        l1["text"] = "Player O wins!!!"
        d_b()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        l1["text"] = "Player O wins!!!"
        d_b()

def check_draw():
    count = 0
    for b in buttons_ttt:
        if b["text"] != " ":
            count += 1

    if count == 9 and (l1["text"] != "Player X wins!!!" or l1["text"] != "Player O wins!!!"):
        l1["text"] = "It's a draw..."

def d_b():
    for b in buttons_ttt:
        if b["text"] == " ":
            b["state"] = "disabled"

def exit_w():
    window.destroy()
    return

def restart_w():
    es["state"] = "active"

    for b in buttons_ttt:
        b["text"] = " "
        b["state"] = "active"

    global btnclick
    if btnclick == True:
        l1["text"] = "Player X's Turn"
    else:
        l1["text"] = "Player O's Turn"

def swap_w():

    global btnclick
    if btnclick == True:
        btnclick = False
        l1["text"] = "Player O's Turn"

    else:
        btnclick = True
        l1["text"] = "Player X's Turn"

window = Tk()
window.title("Tic Tac Toe")

def create_btn(txt, bg, fg, w, h, cm, x, y):
    if cm != None:
        btn = Button(window, text = txt, font = 'Helvetica 20 bold italic', command = cm, width = w, height = h, highlightbackground = bg, foreground = fg)
        btn.grid(row = x, column = y)

    else:
        btn = Label(window, text = txt, font = 'Helvetica 20 bold italic', width = w, height = h, background = bg, foreground = fg)
        btn.grid(row = x, column = y, rowspan = 3, columnspan = 6)

    return btn

b1 = create_btn(" ", '#333333', '#ffb8b8', 8, 4, lambda: buttons(b1), 0, 0)
b2 = create_btn(" ", '#333333', '#ffb8b8', 8, 4, lambda: buttons(b2), 0, 1)
b3 = create_btn(" ", '#333333', '#ffb8b8', 8, 4, lambda: buttons(b3), 0, 2)
b4 = create_btn(" ", '#333333', '#ffb8b8', 8, 4, lambda: buttons(b4), 1, 0)
b5 = create_btn(" ", '#333333', '#ffb8b8', 8, 4, lambda: buttons(b5), 1, 1)
b6 = create_btn(" ", '#333333', '#ffb8b8', 8, 4, lambda: buttons(b6), 1, 2)
b7 = create_btn(" ", '#333333', '#ffb8b8', 8, 4, lambda: buttons(b7), 2, 0)
b8 = create_btn(" ", '#333333', '#ffb8b8', 8, 4, lambda: buttons(b8), 2, 1)
b9 = create_btn(" ", '#333333', '#ffb8b8', 8, 4, lambda: buttons(b9), 2, 2)

# this will make exit, restart and swap buttons
ex = create_btn("Exit", '#ffffff', '#000000', 8, 2, exit_w, 3, 0)
er = create_btn("Restart", '#ffffff', '#000000', 8, 2, restart_w, 3, 1)
es = create_btn("Swap", '#ffffff', '#000000', 8, 2, swap_w, 3, 2)

# this will make the label in which will list current player's turn or who won the game
l1 = create_btn("Player X's Turn", '#333333', '#ffb8b8', 24, 2, None, 4, 0)

buttons_ttt = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
window.resizable(False, False)

window.mainloop()

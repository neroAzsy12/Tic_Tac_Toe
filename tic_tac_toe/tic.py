# tkinter and pillow will be needed
from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Tic Tac Toe")

# function that helps make the images needed for the game
def set_img_render(image):
    img = Image.open(image)
    img_render = ImageTk.PhotoImage(img)
    return img_render

# lines 15-25 are the images that used for the game
bg_render = set_img_render('ttt_imgs/bg_ttt.png')
x_render = set_img_render('ttt_imgs/xx_final.png')
o_render = set_img_render('ttt_imgs/oo_final.png')
ex_render = set_img_render('ttt_imgs/exit_btn2.png')
res_render = set_img_render('ttt_imgs/rest_btn2.png')
swap_render = set_img_render('ttt_imgs/swap_btn2.png')
x_lb_render = set_img_render('ttt_imgs/x_label.png')
o_lb_render = set_img_render('ttt_imgs/o_label.png')
x_wins_render = set_img_render('ttt_imgs/x_wins.png')
o_wins_render = set_img_render("ttt_imgs/o_wins.png")
xo_tie_render = set_img_render("ttt_imgs/xo_tie.png")

# btnclick is used to determine whether a button will be x or o
btnclick = True

def buttons(button):                # parameter is a btn, since btn img, text, state, and other def will be used
    global btnclick                 # uses global keyword since btnclick will change values in the function
    swap["state"] = "disabled"      # as soon as a btn is clicked the swap btn will be disabled

    if btnclick == True:            #if true, then the btn's img will be an x
        button.configure(image = x_render, text = 'x', state = 'disabled')
        lb.configure(image = o_lb_render)
        btnclick = False            # changed to false so player o can have a turn
        check_x()
        if lb['text'] != 'x wins':
            check_tie()

    elif btnclick == False:         #if false, then the btn's img will be an o
        button.configure(image = o_render, text = 'o', state = 'disabled')
        lb.configure(image = x_lb_render)
        btnclick = True             # back to true so player x can have a turn
        check_o()
        if lb['text'] != 'o wins':
            check_tie()

# this method is used to check if player x has won the game
def check_x():
    if b1["text"] == "x" and b2["text"] == "x" and b3["text"] == "x":
        lb.configure(image = x_wins_render, text = 'x wins')
        btns_disable()
    elif b4["text"] == "x" and b5["text"] == "x" and b6["text"] == "x":
        lb.configure(image = x_wins_render, text = 'x wins')
        btns_disable()
    elif b7["text"] == "x" and b8["text"] == "x" and b9["text"] == "x":
        lb.configure(image = x_wins_render, text = 'x wins')
        btns_disable()
    elif b1["text"] == "x" and b4["text"] == "x" and b7["text"] == "x":
        lb.configure(image = x_wins_render, text = 'x wins')
        btns_disable()
    elif b2["text"] == "x" and b5["text"] == "x" and b8["text"] == "x":
        lb.configure(image = x_wins_render, text = 'x wins')
        btns_disable()
    elif b3["text"] == "x" and b6["text"] == "x" and b9["text"] == "x":
        lb.configure(image = x_wins_render, text = 'x wins')
        btns_disable()
    elif b1["text"] == "x" and b5["text"] == "x" and b9["text"] == "x":
        lb.configure(image = x_wins_render, text = 'x wins')
        btns_disable()
    elif b3["text"] == "x" and b5["text"] == "x" and b7["text"] == "x":
        lb.configure(image = x_wins_render, text = 'x wins')
        btns_disable()

# similar to check_x() but instead checks to see if player o wins
def check_o():
    if b1["text"] == "o" and b2["text"] == "o" and b3["text"] == "o":
        lb.configure(image = o_wins_render, text = 'o wins')
        btns_disable()
    elif b4["text"] == "o" and b5["text"] == "o" and b6["text"] == "o":
        lb.configure(image = o_wins_render, text = 'o wins')
        btns_disable()
    elif b7["text"] == "o" and b8["text"] == "o" and b9["text"] == "o":
        lb.configure(image = o_wins_render, text = 'o wins')
        btns_disable()
    elif b1["text"] == "o" and b4["text"] == "o" and b7["text"] == "o":
        lb.configure(image = o_wins_render, text = 'o wins')
        btns_disable()
    elif b2["text"] == "o" and b5["text"] == "o" and b8["text"] == "o":
        lb.configure(image = o_wins_render, text = 'o wins')
        btns_disable()
    elif b3["text"] == "o" and b6["text"] == "o" and b9["text"] == "o":
        lb.configure(image = o_wins_render, text = 'o wins')
        btns_disable()
    elif b1["text"] == "o" and b5["text"] == "o" and b9["text"] == "o":
        lb.configure(image = o_wins_render, text = 'o wins')
        btns_disable()
    elif b3["text"] == "o" and b5["text"] == "o" and b7["text"] == "o":
        lb.configure(image = o_wins_render, text = 'o wins')
        btns_disable()

# this method is used to check if all btns has either an x or an o and no winner is possible
def check_tie():
    count = 0
    for b in btns:
        if b['text'] != '':
            count += 1

    if count == 9 and (lb['text'] != 'x wins' or lb['text'] != 'y wins'):
        lb.configure(image = xo_tie_render)

# method used to disable btns when there is a winner in the game
def btns_disable():
    for b in btns:
        if b.image == bg_render:
            b['state'] = 'disabled'

# this is used to help create the btns needed for the game
def create_btn(render, cm, x, y):
    btn = Button(window, image = render, command = cm)
    btn.image = render
    btn.grid(row = x, column = y)
    return btn

# this method is for the exit btn to close the window
def exit_w():
    window.destroy()
    return

# this method allows players to switch the order in which a person moves in the beginning
def swap_w():
    global btnclick
    if btnclick == True:        # if true then player o will start first
        btnclick = False
        lb.configure(image = o_lb_render)

    else:                       # if its false, then player x will start first
        btnclick = True
        lb.configure(image = x_lb_render)

# method is used for the restart btn to reset all the 9 tiles in the game
def restart_w():
    swap["state"] = "active"
    for b in btns:
        b.configure(image = bg_render, state = 'active', text = '')

    global btnclick
    if btnclick == True:
        lb.configure(image = x_lb_render, text = '')
    else:
        lb.configure(image = o_lb_render, text = '')

# all 9 btns that are used when playing tic tac toe, uses lambda to take a buttons(btn)
b1 = create_btn(bg_render, lambda: buttons(b1), 0, 0)
b2 = create_btn(bg_render, lambda: buttons(b2), 0, 1)
b3 = create_btn(bg_render, lambda: buttons(b3), 0, 2)
b4 = create_btn(bg_render, lambda: buttons(b4), 1, 0)
b5 = create_btn(bg_render, lambda: buttons(b5), 1, 1)
b6 = create_btn(bg_render, lambda: buttons(b6), 1, 2)
b7 = create_btn(bg_render, lambda: buttons(b7), 2, 0)
b8 = create_btn(bg_render, lambda: buttons(b8), 2, 1)
b9 = create_btn(bg_render, lambda: buttons(b9), 2, 2)

#exit btn
ex = create_btn(ex_render, exit_w, 3, 0)

#swap btn
swap = create_btn(swap_render, swap_w, 3, 1)

#restart btn
res = create_btn(res_render, restart_w, 3, 2)

#label for when it is either x's, o's turn, x wins, y wins, or when it's a tie
lb = Label(window, image = x_lb_render)
lb.image = x_lb_render
lb.grid(row = 4, column = 0, rowspan = 3, columnspan = 6)

# useful when calling restart() since it'll use a for loop
btns = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

#prevents the window from be able to change sizes
window.resizable(False, False)
window.mainloop()

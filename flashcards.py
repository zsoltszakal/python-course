from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

###### --- Read Data --- ########

try:
    data = pandas.read_csv("words_to_learn.csv")
    data_dict = data.to_dict(orient="records")

except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    data_dict = data.to_dict(orient="records")


current_card = {}

###### --- Functions --- ########



def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_pic, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_pic, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def delete_card():
    data_dict.remove(current_card)
    df = pandas.DataFrame(data_dict)
    df.to_csv("words_to_learn.csv", index=False)
    next_card()



###### --- User Interface --- ########

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_pic = canvas.create_image(410, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)

b_wrong_img = PhotoImage(file="images/wrong.png")
w_button = Button(image=b_wrong_img, highlightthickness=0, command=next_card)
w_button.grid(column=0, row=1)

b_right_img = PhotoImage(file="./images/right.png")
r_button = Button(image=b_right_img, highlightthickness=0, command=delete_card)
r_button.grid(column=1, row=1)




next_card()


window.mainloop()

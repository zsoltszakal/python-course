import tkinter


def change():
    text = float(input.get())
    gbp_t = round(text * 5035, 0)
    gbp.config(text=gbp_t)


window = tkinter.Tk()
window.title("XRP TO GBP")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)


input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

#Label
main = tkinter.Label()
main.grid(column=0, row=0)

my_label3 = tkinter.Label(text="XRP", font=("Arial", 12, "bold"))
my_label3.grid(column=2, row=0)

my_label = tkinter.Label(text="is equal", font=("Arial", 12, "bold"))
my_label.grid(column=0, row=1)

gbp = tkinter.Label(text="0", font=("Arial", 12, "bold"))
gbp.grid(column=1, row=1)

my_label2 = tkinter.Label(text="GBP", font=("Arial", 12, "bold"))
my_label2.grid(column=2, row=1)

# my_label.config(padx=25, pady=40)


#Button
button = tkinter.Button(text="Click me", command=change)
button.grid(column=1, row=2)



window.mainloop()

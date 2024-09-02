import tkinter as tk
from tkinter import ttk
import main

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("900x900")

# global variables to switch between x and o images
global imageX_used
imageX_used = False

global imageCircle_used
imageCircle_used = False

# images
circle_image = tk.PhotoImage(file="New Pics/ooo.png")
background_img = tk.PhotoImage(file="New Pics/purple.png")
x_image = tk.PhotoImage(file="New Pics/xxx.png")
reset_button_image = tk.PhotoImage(file="reset_button.png")

# home 
back_image = tk.PhotoImage(file="button_back.png")

# frame in root.
frame = ttk.Frame(root, width=64, height=64)
# those positions so it can strech
frame.grid(row=1, column=1)

x = ""
# label
winning_label = tk.Label(root, text=f"Player {x} wins", font=('Courier', 30))

# center frame
root.columnconfigure(0, weight=1)
root.columnconfigure(2, weight=1)

root.rowconfigure(0, weight=1)
root.rowconfigure(2, weight=1)

# button dictionary
status_dict = {
    "button1": "",
    "button2": "",
    "button3": "",
    "button4": "",
    "button5": "",
    "button6": "",
    "button7": "",
    "button8": "",
    "button9": "",
}

# funtion crearte base buttons
# def create_buttons(num):
#     button = "button"+str(num)
#     button = tk.Tk(frame, image=background_img, command=lambda x=num: main.main.button_press(button, x), borderwidth=0)
#     return button

# for i in range(1, 10):
#     j = 0
#     button = create_buttons(i)
#     button_list = [button]
#     if i <= 3:
#         button.grid(row=1, column=1+j)
    

# buttons colum 1
button1 = tk.Button(frame, image=background_img, command=lambda x="1": main.main.button_press(button1, x), borderwidth=0)
button4 = tk.Button(frame, image=background_img, command=lambda x="4": main.main.button_press(button4, x), borderwidth=0)
button7 = tk.Button(frame, image=background_img, command=lambda x="7": main.main.button_press(button7, x), borderwidth=0)

# button colum 2
button2 = tk.Button(frame, image=background_img, command=lambda x="2": main.main.button_press(button2, x), borderwidth=0)
button5 = tk.Button(frame, image=background_img, command=lambda x="5": main.main.button_press(button5, x), borderwidth=0)
button8 = tk.Button(frame, image=background_img, command=lambda x="8":main.main. button_press(button8, x), borderwidth=0)

# buttons colum 3
button3 = tk.Button(frame, image=background_img, command=lambda x="3": main.main.button_press(button3, x), borderwidth=0)
button6 = tk.Button(frame, image=background_img, command=lambda x="6": main.main.button_press(button6, x), borderwidth=0)
button9 = tk.Button(frame, image=background_img, command=lambda x="9": main.main.button_press(button9, x), borderwidth=0)

# back button
back_button = tk.Button(root, command=back_image, borderwidth=0)
back_button.grid(row=2, column=4)

# reset button
reset_button = tk.Button(root, image=reset_button_image, command=main.main.reset, borderwidth=0)
reset_button.grid(row=2, column=1)

button_list = [button1, button2, button3, button4, button5, button6, button7, button8, button9]


button1.grid(row=2, column=1)
button4.grid(row=5, column=1)
button7.grid(row=8, column=1)

button2.grid(row=2, column=3)
button5.grid(row=5, column=3)
button8.grid(row=8, column=3)

button3.grid(row=2, column=6)
button6.grid(row=5, column=6)
button9.grid(row=8, column=6)

if __name__ == "__main__":
    main.main(status_dict, winning_label, button_list, background_img, x_image, circle_image)

root.mainloop()
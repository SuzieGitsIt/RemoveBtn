import tkinter as tk                                    # Tkinter's Tk class
from functools import partial                           # freezing one function while executing another
  
app = tk.Tk()
app.geometry('200x200')
  
set1_var = tk.IntVar()

def toggle(txt_i):                                                         # function to toggle what button click does
    btn_name = (btn_ids[txt_i])                                            # create 50 unique button names from btn_ids[n]
    btn_name.config(text=f"{btn_text[txt_i]}") 
    print("button name: ", btn_name)                                    # btn_name = .!window.!button##
    if btn_name.config('relief')[-1] == 'sunken':                       # if btn_name relief configuration is equal to sunken
        btn_name.config(relief="raised", bg='white')                    # second button click raises the button back up
    else:
        btn_name.config(relief="sunken", bg='grey')                     # first button click sinks the button

btn_row1 = []
btn_row2 = []
btn_row3 = []
def chk1(btn_list):                                                       # Creating a function for removing widgets from grid
    row = set1_var.get()
    for i in range(0,3):
        btn_row1.append(btn_list[i])
    for i in range(3,6):
        btn_row2.append(btn_list[i])
    for i in range(6,9):
        btn_row3.append(btn_list[i])

    if row:
        print("Checkbox selected", row)                                              # c = column, max 25 columns
        for j in range(0,3):
            btn_row1[j].grid(column=j+2, row=1)
        for j in range(0,3):
            btn_row2[j].grid(column=j+2, row=2)
        for j in range(0,3):
            btn_row3[j].grid(column=j+2, row=3)

    else:
        print("Checkbox unselected", row)                                             # c = column, max 25 columns
        for j in range(0,3):
            btn_row1[j].grid_remove()
        for j in range(0,3):
            btn_row2[j].grid_remove()
        for j in range(0,3):
            btn_row3[j].grid_remove()

btn_ids = []
btn_text = []
count_btn_txt = 0
for i in range(0,9):
    btn_text.append(count_btn_txt+1)
    btn = tk.Button(app, width=4, text=btn_text[count_btn_txt], relief="raised", command=partial(toggle, count_btn_txt))    # create buttons & assign unique arg (i) to run function (change)
    btn_ids.append(btn)
    count_btn_txt +=1

chk_btn = tk.Checkbutton(app, text="Checkbox", onvalue = 1, offvalue = 0, variable=set1_var, command=lambda: chk1(btn_ids))     # Create and show button with remove() function
chk_btn.grid(column=1, row=1)
  
app.mainloop()

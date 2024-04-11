from tkinter import *
from PIL import ImageTk, Image
from tkinter.messagebox import askyesno

root = Tk()
root.geometry("300x400+500+200")
root.resizable(False, False)
root.title("Weight Converter")
# icon_image = ImageTk.PhotoImage(Image.open("light.png"))
icon_image = ImageTk.PhotoImage(Image.open("dark.png"))
root.iconphoto(False, icon_image)
root.configure(bg="lightgrey")

weight_label = Label(root, text="Enter Your Weight", bg="light grey", font="Arial 9 bold")
enter_weight = Entry(root, relief=SOLID, border=2, width=30)
weight_label.place(x=60,y=20)
enter_weight.place(x=61, y=45)

convert_weight_label = Label(root, text="Weight Convert", bg="light grey", font="Arial 12 bold")
convert_weight_label.pack(pady=85)

error = Label(root, text="Note: It Will Take Only Integer", fg="red", bg="lightgrey", font="Arial 10 bold")
error.place(x=55, y=275)

# about owner
about_label = Label(root, text="Ⓒ Copyright 2024 Made by Parveen Biswas", bg="lightgrey", font=("Arial 10"))
about_label.place(x=20, y=375)

# close window
def close():
    comfimation = askyesno(title="Exit", message="Do you want to Exit ?")
    if comfimation:
        root.destroy()
root.protocol("WM_DELETE_WINDOW", close)

# checkbutton input
kg = IntVar()
pound = IntVar()
ounce = IntVar()

Input_kg_button = Checkbutton(root, text="Kilogram", variable=kg, font="Arial 10 bold" , onvalue=1, offvalue=0, bg="lightgrey", activebackground="lightgrey")
Input_kg_button.place(x=30, y=130)
Input_pound_button = Checkbutton(root, text="Pound", variable=pound, font="Arial 10 bold" , onvalue=1, offvalue=0, bg="lightgrey", activebackground="lightgrey")
Input_pound_button.place(x=30, y=170)
Input_ounce_button = Checkbutton(root, text="Ounce", variable=ounce, font="Arial 10 bold" , onvalue=1, offvalue=0, bg="lightgrey", activebackground="lightgrey")
Input_ounce_button.place(x=30, y=210)

# checkbutton output
Okg = IntVar()
Opound = IntVar()
Oounce = IntVar()

Output_kg_button = Checkbutton(root, text="Kilogram", variable=Okg, font="Arial 10 bold" , onvalue=1, offvalue=0, bg="lightgrey", activebackground="lightgrey")
Output_kg_button.place(x=178, y=130)
Output_pound_button = Checkbutton(root, text="Pound", variable=Opound, font="Arial 10 bold" , onvalue=1, offvalue=0, bg="lightgrey", activebackground="lightgrey")
Output_pound_button.place(x=178, y=170)
Output_ounce_button = Checkbutton(root, text="Ounce", variable=Oounce, font="Arial 10 bold" , onvalue=1, offvalue=0, bg="lightgrey", activebackground="lightgrey")
Output_ounce_button.place(x=178, y=210)

# result display
result_display_label = Label(root, text="Result",bg="lightgrey", font="Arial 9 bold")
result_disp = Text(root, relief=SOLID, height=1, width=25)
result_display_label.place(x=20, y=248)
result_disp.place(x=67, y=250)

# convert function
def convert_function():
    g = float(enter_weight.get()) * 1
    pound1 = float(enter_weight.get()) * 1
    ounce1 = float(enter_weight.get()) * 1

    if kg.get() == 1:
        if  Okg.get()==1:
            result_disp.delete('1.0', 'end')
            result_disp.insert("1.0","%s grams" % g)
    elif pound.get() == 1:
        if  Opound.get()==1:
            result_disp.delete('1.0', 'end')
            result_disp.insert("1.0","%s pound" % pound1)
    elif ounce.get() == 1:
        if  Oounce.get()==1:
            result_disp.delete('1.0', 'end')
            result_disp.insert("1.0","%s ounce" % ounce1)
    else:
        pass
    
# diff
    kg_pound = float(enter_weight.get()) * 2.20462
    pound_kg = float(enter_weight.get()) * 0.453592
    kg_ounce = float(enter_weight.get()) * 35.274
    ounce_kg = float(enter_weight.get()) * 0.0283495
    ounce_pound = float(enter_weight.get()) * 0.0625
    pound_ounce = float(enter_weight.get()) * 16

    if kg.get() == 1:
        if Opound.get() == 1:
            result_disp.delete('1.0', 'end')
            result_disp.insert("1.0","%s pound" % kg_pound)
    elif pound.get() == 1:
        if  Okg.get() == 1:
            result_disp.delete('1.0', 'end')
            result_disp.insert("1.0","%s grams" % pound_kg)
    else:
        pass

    

    if ounce.get() == 1:
        if Okg.get() == 1:
            result_disp.delete('1.0', 'end')
            result_disp.insert("1.0","%s grams" % ounce_kg)
    elif kg.get() == 1:
        if Oounce.get() == 1:
            result_disp.delete('1.0', 'end')
            result_disp.insert("1.0","%s ounce" % kg_ounce)
    elif pound.get() == 1:
        if Oounce.get() == 1:
            result_disp.delete('1.0', 'end')
            result_disp.insert("1.0","%s ounce" % pound_ounce)
    else:
        pass

    if ounce.get() == 1:
        if Opound.get() == 1:
            result_disp.delete('1.0', 'end')
            result_disp.insert("1.0","%s pound" % ounce_pound)
    else:
        pass


convert_button = Button(root, text="Convert", command=lambda:convert_function(),relief=SOLID, width=20 ,font="Arial 10 bold", fg="red", bg="white", activebackground="red", activeforeground="white")
convert_button.place(x=68, y=300)




root.mainloop()
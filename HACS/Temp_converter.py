from tkinter import *
from tkinter import messagebox
import tkinter as tk

def ConvertTemp():

        celsuis = T_c.get()
        Fahrenheit = T_f.get()
        
        
        if celsuis.strip():
            
            try:
                celsuis = float(celsuis)
            except ValueError:
                cap.destroy()
                messagebox.showinfo("Temp Converter", "Invalid Input")
                return
        
            celsuis = celsuis*1.8
            celsuis = celsuis + 32
            messagebox.showinfo("Temp Converter", f"It is {celsuis} Fahrenheit")
            cap.destroy()
        
        elif Fahrenheit.strip():
            
            try:
                Fahrenheit = float(Fahrenheit)
            except ValueError:
                cap.destroy()
                messagebox.showinfo("Temp Converter", "Invalid Input")
                return
            
            Fahrenheit = Fahrenheit - 32
            Fahrenheit = Fahrenheit*5
            Fahrenheit = Fahrenheit/9
            messagebox.showinfo("Temp Converter", f"It is {Fahrenheit} Celsuis")
            cap.destroy()



cap = tk.Tk()

Header = cap.title('Temp Converter')
my_canvas = tk.Canvas(cap, bg="black", height=300, width=800)
my_canvas.pack()

# adding the labels for the tkinter window
label_celsuis = tk.Label(cap, text='Enter temp in celsuis: ')
label_celsuis.config(font=('helvetica', 14), fg='white', bg='black')
my_canvas.create_window(150, 100, window=label_celsuis)

label_f = tk.Label(cap, text='Enter temp in fahrenheit: ')
label_f.config(font=('helvetica', 14), fg='white', bg='black')
my_canvas.create_window(630, 100, window=label_f)


# creating input window
T_c = tk.Entry(cap)
my_canvas.create_window(170, 150, height=30, width=300, window=T_c)

# creating input window
T_f = tk.Entry(cap)
my_canvas.create_window(630, 150, height=30, width=300, window=T_f)




# the resize button
button = tk.Button(
    cap,
    text="Convert",
    width=25,
    height=3,
    bg="white",
    fg="black",
    font=('helvetica', 10, 'bold'),
    command=ConvertTemp
    )

my_canvas.create_window(400, 150, height=40,width=150, window=button)

cap.mainloop()

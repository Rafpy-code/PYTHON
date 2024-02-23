import tkinter as tk

OptionList = ["Crear nueva lista","Agregar artículo","Eliminar artículo","Terminar lista"] 
app = tk.Tk()
app.geometry('300x350')

variable = tk.StringVar(app)
variable.set(OptionList[0])

opt = tk.OptionMenu(app, variable, *OptionList)
opt.config(width=100, font=('Helvetica', 14))
opt.pack()

app.mainloop()
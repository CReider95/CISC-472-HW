import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def SlicerScript():
   print("button clicked")

B = Tkinter.Button(top, text ="HW Jan 19th", command = SlicerScript)

B.pack()
top.mainloop()

from tkinter import *

window = Tk()
window.geometry("600x400")
window.configure(bg="magenta", padx=10, pady=10)
window.title("Guass Formula GUI")

def summate():
 start = int(startEntry.get())
 end = int(endEntry.get())
 sum=0
 for x in range(start, end+1):
    sum += x
    sumLabel.configure(text=sum)


frame1 = Frame(window, bg="magenta", height=200, width=200, padx=10, pady=10)
frame1.pack()
frame2 = Frame(window, bg="magenta", height=200, width=200, padx=10, pady=10)
frame2.pack()
frame3 = Frame(window, bg="magenta", height=200, width=200, padx=10, pady=10)
frame3.pack()
frame4 = Frame(window, bg="magenta", height=200, width=200, padx=10, pady=10)
frame4.pack()

startLabel = Label(frame1, bg="magenta", fg="white", text="Enter below: ", font = ("Courier",17))
startLabel.pack()

startEntry = Entry(frame1, bg= "purple", fg="white", font = ("Courier",25))
startEntry.pack()

endLabel = Label(frame2, bg="magenta", fg="white", text="Enter below: ", font = ("Courier",17))
endLabel.pack()

endEntry = Entry(frame2, bg= "purple", fg="white", font = ("Courier",25))
endEntry.pack()

button = Button(frame3, bg= "purple", fg="purple", text="Click Here", height=1, width=5, font = ("",14), command = summate)
button.pack()

sumLabel = Label(frame4, bg="purple", fg="white", text="sum:___", font = ("Courier",25))
sumLabel.pack()

window.mainloop()
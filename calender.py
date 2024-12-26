from tkinter import *
import calendar

root=Tk()
root.config(background="lightblue")
root.title("Calendar")
root.geometry("300x200")
root.resizable(False,False)

def view_calendar():
    window=Tk()
    window.config(background="lightgreen")
    window.title("Complete year calendar")
    window.geometry("600x600")
    window.resizable(False,False)

    get_year=int(year_en.get())
    window_cont=calendar.calendar(get_year)

    text_widget=Text(window,wrap=NONE,font=("courier",10,"bold"),bg="lightgreen")
    text_widget.insert(END,window_cont)
    text_widget.config(state=DISABLED)
    text_widget.pack(expand=True,fill=BOTH)  

    window.mainloop()

name=Label(root,text="Calendar",bg="light pink",font=("Arial",20,"bold"))
name.grid(row=1,column=1,padx=90,pady=10)

year=Label(root,text="Enter the year",font=("Arial",15,"bold"),bg="lightblue")
year.grid(row=2,column=1,pady=10)

year_en=Entry(root,font=("arial",15,"bold"),width=15,justify="center")
year_en.grid(row=3,column=1,pady=5)

show=Button(root,text="Show calendar",fg="red",bg="gray",font=("Arial",10,"bold"),command=view_calendar)
show.grid(row=4,column=1,pady=10)

root.mainloop()
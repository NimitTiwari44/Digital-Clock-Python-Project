from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    minu = time.strftime('%M')
    sec = time.strftime('%S')
    am_pm = time.strftime('%p')
    
    lab_hr.config(text=hr)
    lab_min.config(text=minu)
    lab_sec.config(text=sec)
    lab_am.config(text=am_pm)
    
    
    dat = time.strftime('%d')
    mon = time.strftime('%m')
    year = time.strftime('%y')
    day = time.strftime('%a')
    
    lab_date.config(text=dat)
    lab_month.config(text=mon)
    lab_year.config(text=year)
    lab_day.config(text=day)
    
    
    lab_hr.after(200, date_time)
    
clock = Tk()
clock.title('   Digital Clock   ')
clock.geometry('1000x500')
clock.config(bg="blue")

lab_hr = Label(clock, text="00", font=('Time New Roman',60,"bold"), bg="blue",fg="white")
lab_hr.place(x=120, y=60,height=100, width=100)
lab_hr_txt = Label(clock, text="Hour", font=('Time New Roman',20,"bold"), bg="blue",fg="white")
lab_hr_txt.place(x=120, y=190,height=40, width=100)

lab_min = Label(clock, text="00", bg="blue", fg="white", font=('Time New Roman',60,"bold"))
lab_min.place(x=340, y=60, height=100, width=100)
lab_min_txt = Label(clock, text="Min", bg="blue", fg="white", font=('Time New Roman',20,"bold"))
lab_min_txt.place(x=340, y=190, height=40, width=100)

lab_sec = Label(clock, text="00", bg="blue", fg="white", font=('Time New Roman', 60, "bold"))
lab_sec.place(x=560, y=60, height=100, width=100)
lab_sec_txt = Label(clock, text="Sec", bg="blue", fg="white", font=('Time New Roman', 20, "bold"))
lab_sec_txt.place(x=560, y=190, height=40, width=100)

lab_am = Label(clock, text="00", bg="blue", fg="white", font=('Time New Roman', 40, "bold"))
lab_am.place(x=780, y=60, height=100, width=100)
lab_am_txt = Label(clock, text="AM/PM", bg="blue", fg="white", font=('Time New Roman', 20, "bold"))
lab_am_txt.place(x=780, y=190, height=40, width=100)



lab_date = Label(clock, text="00", font=('Time New Roman',60,"bold"), bg="blue",fg="white")
lab_date.place(x=120, y=260,height=100, width=100)
lab_date_txt = Label(clock, text="Date", font=('Time New Roman',20,"bold"), bg="blue",fg="white")
lab_date_txt.place(x=120, y=390,height=30, width=100)

lab_month = Label(clock, text="00", bg="blue", fg="white", font=('Time New Roman',60,"bold"))
lab_month.place(x=340, y=260, height=100, width=100)
lab_month_txt = Label(clock, text="Month", bg="blue", fg="white", font=('Time New Roman',20,"bold"))
lab_month_txt.place(x=340, y=390, height=30, width=100)

lab_year = Label(clock, text="00", bg="blue", fg="white", font=('Time New Roman', 60, "bold"))
lab_year.place(x=560, y=260, height=100, width=100)
lab_year_txt = Label(clock, text="Year", bg="blue", fg="white", font=('Time New Roman', 20, "bold"))
lab_year_txt.place(x=560, y=390, height=30, width=100)

lab_day = Label(clock, text="00", bg="blue", fg="white", font=('Time New Roman', 40, "bold"))
lab_day.place(x=780, y=260, height=100, width=100)
lab_day_txt = Label(clock, text="Day", bg="blue", fg="white", font=('Time New Roman', 20, "bold"))
lab_day_txt.place(x=780, y=390, height=30, width=100)

date_time()

clock.mainloop()
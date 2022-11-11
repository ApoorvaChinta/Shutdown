from tkinter import *
import os

def restart():
    os.system('shutdown /r /t 1')
def restart_time():
    os.system('shutdown /r /t 20')
def shutdown():
    os.system('shutdown /r /t 1')
def notepad():
    os.system('notepad')
def date():
    os.system('date')

st=Tk()
st.title('Shutdown App')
st.geometry('500x500')
st.config(bg='Grey')

r_button=Button(st,text='Restart',font=('Time New Roman', 15,'bold'),relief=RAISED,cursor='plus',command=restart)
r_button.place(x=30,y=20,height=40,width=200)

rt_button=Button(st,text='Restart_time',font=('Time New Roman', 15,'bold'),relief=RAISED,cursor='plus',command=restart_time)
rt_button.place(x=30,y=80,height=40,width=200)

st_button=Button(st,text='Shutdown',font=('Time New Roman', 15,'bold'),relief=RAISED,cursor='plus',command=shutdown)
st_button.place(x=30,y=140,height=40,width=200)

note_button=Button(st,text='Notepad',font=('Time New Roman', 15,'bold'),relief=RAISED,cursor='plus',command=notepad)
note_button.place(x=30,y=200,height=40,width=200)

date_button=Button(st,text='Date',font=('Time New Roman', 15,'bold'),relief=RAISED,cursor='plus',command=date)
date_button.place(x=30,y=260,height=40,width=200)


st.mainloop()

from cgitb import text
from email import message
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


GUI = Tk() #ทีตัวใหญ เคตัวเล็ก
GUI.title('โปรแกรมคำนวณปลา')
GUI.geometry('500x300')


L= Label(GUI,text='กรุณากรอกจำนวนปลา',font=(None,20))
L.pack()

v_quantity = StringVar()# เป็นตัวแปลข้อความเมื่อพิมพิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI,textvariable=v_quantity, font=(None,20))
E1.pack()

def Cal():
    try:    
        quan = float(v_quantity.get())
        calc = quan * 39 #ราคา39 บาทต่อกิโล
        messagebox.showinfo('ราคาทั้งหมด','ราคาปลาทั้งหมด {} บาท'.format(calc) )
        v_quantity.set('1')
        E1.focus()
    except:
        messagebox.showwarning('กรอกผิด','กรุณากรอกตัวเลขเท่านั้น')
        v_quantity.set('1')
        E1.focus()

B = ttk.Button(GUI, text='คำนวณ',command=Cal)
B.pack(ipadx=30,ipady=20)


GUI.mainloop() #เพื่อให้โปรแกรมรันตลอดเวลา
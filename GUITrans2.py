# GUITranslator.py
from tkinter import *
#จากไลบรารี่ชื่อ tkinter,* คือให้ดึงความสามารถหลักมาทั้งหมด
from tkinter import ttk #ttk is theme of tk
###----------google translate----------
from googletrans import Translator
translator = Translator() #สร้างฟังชั่นแปลภาษาขึ้นมา


GUI = Tk() #สร้างหน้าต่างหลัก
GUI.geometry('500x300') #ขยายขนาดหน้าจอ = กว้างxสูง
GUI.title('โปรแกรมแปลภาษา by วุ้นแปลภาษา') #ชื่อหน้าต่าง

#----------Config----------
FONT = ('Angsana New',15) #ลักษณะฟ้อน + ขนาดตัวอักษร

#----------Label----------
L = ttk.Label(GUI,text='กรุณากรอกคำศัพท์ที่ต้องการแปล',font=FONT)
L.pack()


#----------Entry (ช่องกรอรกข้อความ)----------
v_vocab = StringVar() #กล่องเก็บข้อความที่เป็น Stringเท่านั้น

E1 = ttk.Entry(GUI,textvariable = v_vocab,font=FONT,width=40)
E1.pack(pady=10)


#-------------Button (ปุ่มแปล)-------------
def Translate():
    vocab = v_vocab.get() #.get คือให้แสดงผลออกมา
    meaning = translator.translate(vocab,dest='th')
    print(vocab + ' : ' + meaning.text)
    print(meaning.pronunciation)
    v_result.set(vocab + ' : ' + meaning.text) #สั่งโชว์ในgui

B1 = ttk.Button(GUI,text='Translate',command=Translate) #สร้างปุ่ม
B1.pack(ipadx=20,ipady=10) #โชว์ปุ่มขึ้นมาวางจากบนลงล่าง ipadx,y=ขนาดปุ่ม

#----------Label----------
L = ttk.Label(GUI,text='คำแปล',font=FONT)
L.pack()

#----------Result----------
v_result = StringVar() #นี้คือกล่องเก็บคำแปล
FONT2 = ('Angsana New',20)
R1 = ttk.Label(GUI,textvariable=v_result,font=FONT2,foreground='green')
R1.pack()

GUI.mainloop() #ทำให้โปรแกรมรันได้ตลอดเวลาจนกว่าจะปิด (ต้องอยู่บรรทัดสุดท้าย)

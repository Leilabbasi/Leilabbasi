from tkinter import *
from PIL import Image,ImageTk
import tkinter.font as font
#=========================window===================================================
window = Tk()
window.geometry('695x740')
window.title('calculator')
window.resizable(width=False , height=False)
window.configure(bg='black')
#==========================photo=================================================
photo_bg = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2.png')
photo_0 = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (2).png')
photo_plus = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (18).png')
photo_1 = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (3).png')
photo_2 = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (4).png')
photo_3 = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (5).png')
photo_4 = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (6).png')
photo_5 = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (7).png')
photo_6 = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (8).png')
photo_neg = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (15).png')
photo_7 = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (9).png')
photo_8 = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (10).png')
photo_9 = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (11).png')
photo_x = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (12).png')
photo_sin = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (13).png')
photo_pr = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (14).png')
photo_cos = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (16).png')
photo_pn = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (17).png')
photo_tan = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (19).png')
photo_tq = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (20).png')
photo_dot = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (21).png')
photo_sinh = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (22).png')
photo_cosh = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (23).png')
photo_tanh = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (24).png')
photo_pi = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (25).png')
photo_log10 = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (26).png')
photo_exp = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (27).png')
photo_w = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (28).png')
photo_clr = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (29).png')
photo_log = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (30).png')
photo_ms = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\2 (31).png')
photo_field1 = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\InShot_20220706_155206556 (2).png')
photo_field2 = PhotoImage(file = r'C:\Users\WebVajhegan\Pictures\Saved Pictures\InShot_20220706_155206556 (3).png')

operation_Font = font.Font(size=35)
operation_Value = StringVar()
num_1= StringVar()
num_2 = StringVar()
result_Value = StringVar()
expression = ''
expression2 = ''
selected_Input = 1
operation = ''

#=========================label===========================================
Label_bg = Label(window, image=photo_bg)
Label_bg.place(x=1,y=1)
input_number1 = Entry(window , textvariable=num_1)
input_number1.place(x=35 , y=60 , height=50 , width=125)
input_number2 = Entry(window , textvariable=num_2)
input_number2.place(x=205 , y=60 , height=50 , width=125)
result_Entry = Entry(window , textvariable=result_Value)
result_Entry.place(x=340 , y=60 , height=50 , width=320)
operation_field = Entry(window , textvariable= operation_Value , font= operation_Font)
operation_field.place(x=165 , y=60 , height=50 , width=35)

#==============================function================================

def set_operation(op) :
    global operation
    operation = op
    operation_Value.set(op)
    
def set_input1():
    global selected_Input
    selected_Input = 1
    
    
def set_input2():
    global selected_Input
    selected_Input = 2    
    
    
def set_number(number):
    global expression
    global expression2
    expression = expression + str(number)
    expression2 = expression2 + str(number)
    
    if selected_Input== 1:
        expression2 =''
        num_1.set(expression)
        
    elif selected_Input== 2:
        expression =''
        num_2.set(expression2)
        

def clear_input() :
    num_1.set('')
    num_2.set('')
    result_Value.set('')
    operation_Value.set('')


def show_result() :
    if operation == '+' :
        result = float(num_1.get()) + float(num_2.get())
        result_Value.set(result)
        
    elif operation == '-' :
        result = float(num_1.get()) - float(num_2.get())
        result_Value.set(result)        
        
    elif operation == '*' :
        result = float(num_1.get()) * float(num_2.get())
        result_Value.set(result)        
        
    elif operation == '/' :
        result = float(num_1.get()) / float(num_2.get())
        result_Value.set(result)        
        
#=========================button==========================================
button_0 = Button(window,image = photo_0 , command = lambda : set_number(0))
button_0.place(x=135 , y=480)
button_plus = Button(window,image = photo_plus, command = lambda : set_operation('+'))
button_plus.place(x=345 , y=378)
button_1 = Button(window , image = photo_1, command = lambda : set_number(1))
button_1.place(x=28 , y=378)
button_2 = Button(window , image=photo_2, command = lambda : set_number(2))
button_2.place(x=135 , y=378)
button_3 = Button(window , image =photo_3, command = lambda : set_number(3))
button_3.place(x=240 , y=378)
button_4 = Button(window , image =photo_4, command = lambda : set_number(4))
button_4.place(x=28 , y=275)
button_5 = Button(window , image =photo_5, command = lambda : set_number(5))
button_5.place(x=135 , y=275)
button_6 = Button(window , image=photo_6, command = lambda : set_number(6))
button_6.place(x=240 , y=275)
button_neg = Button(window , image =photo_neg, command = lambda : set_operation('-'))
button_neg.place(x=345 , y=275)
button_7 = Button(window , image = photo_7, command = lambda : set_number(7))
button_7.place(x=28 , y=175)
button_8 = Button(window , image=photo_8, command = lambda : set_number(8))
button_8.place(x=135 , y=175)
button_9 = Button(window , image =photo_9, command = lambda : set_number(9))
button_9.place(x=240 , y=175)
button_x = Button(window , image = photo_x, command = lambda : set_operation('*'))
button_x.place(x=345 , y=175)
button_sin = Button(window , image=photo_sin, command = lambda : set_operation())
button_sin.place(x=455 , y=175)
button_pr = Button(window , image = photo_pr, command = lambda : set_number(0))
button_pr.place(x=560 , y=175)
button_cos = Button(window , image = photo_cos, command = lambda : set_number(0))
button_cos.place(x=455 , y=275)
button_pn = Button(window , image = photo_pn, command = lambda : set_number(0))
button_pn.place(x=560 , y=275)
button_tan = Button(window , image = photo_tan, command = lambda : set_number(0))
button_tan.place(x=455 , y=378)
button_tq = Button(window , image = photo_tq, command = lambda : set_number(0))
button_tq.place(x=560 , y=378)
button_dot = Button(window , image =photo_dot, command = lambda : set_number(0))
button_dot.place(x=28 , y=480)
button_sinh = Button(window , image = photo_sinh, command = lambda : set_number(0))
button_sinh.place(x=240 , y=480)
button_cosh = Button(window , image = photo_cosh, command = lambda : set_number(0))
button_cosh.place(x=345 , y=480)
button_tanh = Button(window , image = photo_tanh, command = lambda : set_number(0))
button_tanh.place(x=455 , y=480)
button_pi = Button(window , image =photo_pi, command = lambda : set_number(0))
button_pi.place(x=560 , y=480)
button_log10 = Button(window , image = photo_log10, command = lambda : set_number(0))
button_log10.place(x=28 , y=580)
button_exp = Button(window , image = photo_exp, command = lambda : set_number(0))
button_exp.place(x=135 , y=580)
button_w = Button(window , image = photo_w, command = lambda : set_operation('/'))
button_w.place(x=240 , y=580)
button_clr = Button(window , image = photo_clr, command = lambda : clear_input())
button_clr.place(x=345 , y=580)
button_log = Button(window , image = photo_log, command = lambda : set_number(0))
button_log.place(x=455 , y=580)
button_ms = Button(window , image =photo_ms, command = lambda : show_result())
button_ms.place(x=560 , y=580)
button_field1 = Button(window , image =photo_field1 ,command=lambda: set_input1())
button_field1.place(x=30 , y=135 , height=40 , width=100 )
button_field2 = Button(window , image =photo_field2 ,command= lambda: set_input2())
button_field2.place(x=200 , y=135 , height=40 , width=100)
#==================================================================================
window.mainloop()






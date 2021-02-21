from tkinter import*
from tkinter import Menu
from tkinter import messagebox


root = Tk()
root.title('Kennartfoundation Calc')
root.geometry("320x501+530+100")
root.config(background='#393939')
root.resizable(False,0)
root.iconbitmap('icons3/KM.ico')
root.attributes('-alpha', 0.9)


# function.............
def enterNumber(x):
        if entry_box.get() =="O":  # default value is O so we need to remove it
            entry_box.delete(0, 'end') 
            entry_box.insert(0, str(x)) # this will insert whatever going to be pressed  #(x is our first number) and zero is our first index
        else:
            length=len(entry_box.get()) # it depend on the length
            entry_box.insert(length, str(x)) # second number is been used whenever it is been pressed

    
def enterOperator(x):
    if entry_box.get() !="O": #......ZERO is default value and which is empty ).....it have to start with number #and have to have a number inside cannot be empty
        length=len(entry_box.get())
        entry_box.insert(length, btn_operator[x] ['text'])  #this is trigered whenevere an operator is been clicked or will understand the button that was clicked


def funcClear():
    entry_box.delete(0,END) #this functio delete whatever value inside and insert default value
    entry_box.insert(0, "O") # this function insert the default value


result = 0
result_list=[]
def funcOperator():
    try:
        content = entry_box.get()
        result = eval(content)
        entry_box.delete(0, END)
        entry_box.insert(0, str(result))
        result_list.append(content)
        result_list.reverse()
        statusBar.configure(text='History :'+'|'.join(result_list[:5]),font='verdana 10 bold')# join function will show the list items
    except ZeroDivisionError:
        entry_box.delete(0, END)
        entry_box.insert(0, "Impossible division")
    except SyntaxError:
       entry_box.delete(0, END)
       entry_box.insert(0, str('SyntaxError !!'))
    except:
        messagebox.showinfo('Zero', "Not possible\nplease click a number before", icon="info")



def buttonPress(n):
    if entry_box.get() =="O":
        entry_box.delete(0, 'end')
        entry_box.insert(0, str(n)) 
    else:
        length=len(entry_box.get())
        entry_box.insert(length, str(n)) 

    
def funcDelete():
    length=len(entry_box.get())
    entry_box.delete(length-1, 'end') #-1 is used because length value start from 1 (but indesis start from 0)
    if length == 1:
        entry_box.insert(0, "O") #this means after deleting everything insert back the default value


def exit(*event):
    if messagebox.askyesno("Quit?", "Are you sure you want to quit the program", icon='warning'):
        root.destroy()
    else:
        command = root
        return


def About():
    global ios
    global icom 
    ios = Toplevel()
    ios.title('Artfoundation')
    ios.geometry("318x232+531+100")
    ios.config(background='#393939')
    ios.resizable(False,False)
    ios.iconbitmap('icons3/KM.ico')
    ios.transient(root)
    ios.attributes('-alpha', 0.9)

    icom = PhotoImage(file='icons3/AA.png')
    delete = Label(ios,  image=icom, bg='#393939', compound=RIGHT)
    delete.place(x=8,y=5)

    ios.label = Label(ios, text="Kennart Calc\nVersion 2.0 (OS Build)'\n@ 2020 Kennartfoundation. All rights reserved.",font='deansgate 10 bold', fg='yellow', bg='#393939')
    ios.label.place(x=10, rely=0.54)
    ios.label = Label(ios, text="Develop by \nKennartfoundation", bg='#393939', fg='yellow', font='deansgate 13')
    ios.label.place(x=160, rely=0.30)

    label = Label(ios, width=100, bg='white')
    label.place(x=0, y=120, height=1)
    ios.config(bg='#393939')

    button = Button(ios, text='Ok!!', width=7, font='deansgate 10 bold', bg='#393939', fg='white', command=close)
    button.place(x=223, y=200)

def close():
    if messagebox.askyesno('About', 'Wanna close the help Menu!!', icon='info'):
        ios.destroy()
    else:
        return


menu = Menu()
root.config(menu = menu)
filename = Menu(menu, tearoff=0, activebackground='teal')
menu.add_cascade(label='File', menu=filename)
filename.add_command(label='Exit', command=exit)

help_= Menu(menu, tearoff=0, activebackground='teal')
menu.add_cascade(label='Help', menu=help_)
help_.add_command(label='About',  command=About)


# entry button ........................................
entry_box = Entry(root, font='deansgate 19', width=20,  bd=5,  justify='right',bg='#e6e6fa')
entry_box.insert(0, 'O') #O is use because if not we can't use 0.3... # O default value 
entry_box.place(x=12, y=10, height=40,)
entry_box.focus()


# Number button.........#..........(button numbers)
btn_numbers =[]
for i in range(10): #zero to 9 #.............
    btn_numbers.append(Button(width=4, text=str(i), font='deansgate 15 bold', fg='white', #str is use because is integer if not it would generate error
        relief='groove', bg='#393939',command=lambda x=i: enterNumber(x))) # x will show the number which is been click    (follow by function)

btn_text=1 #started with 1 to increase the number
for i in range(0, 3):
    for j in range(0, 3):
        btn_numbers[btn_text].place(x=15+j*77, y=79+i*70) #btn_numbers
        btn_text +=1 # use to increase the text value.......#....(button numbers)

 
#operator_button
btn_operator=[]
for i in range(3): #the operator is 4
    btn_operator.append(Button(width=4,font='deansgate 15 bold',fg='black', bg = "#98DBC6",  relief='groove',
        command=lambda x=i:enterOperator(x))) # x will show the number which is been click    (follow by function)


btn_operator[0]['text']="*"
btn_operator[1]['text']="/"
btn_operator[2]['text']="+"
#btn_operator[2]['text']="/"

for i in range(3):
    btn_operator[i].place(x=245,y=79+i*70)


btn_zero = Button(width=17, text='0', font='times 15 bold', fg='white', bg='#393939', relief='groove',command=lambda x=0: enterNumber(x))
btn_clear = Button(width=4,text='Clear', font='deansgate 15', fg='white', bg='#e67019', relief='groove', command=funcClear)
btn_clear.place(x=16,y=360)
btn_zero.place(x=14,y=290)
btn_dot= Button(width=4,text='.', font='times 15 bold', fg='white', bg='#393939', relief='groove', command=lambda x='.': enterNumber(x))
btn_dot.place(x=90,y=360)
btn_equals = Button(width=4,text='=', font='times 15 bold', fg='white', bg='#393939', relief='groove', command=funcOperator)
btn_equals.place(x=169,y=360)

subtract = Button(text = "-", bg = "#98DBC6", relief='groove', width=4, font='deansgate 15 bold', command=lambda n='-': buttonPress(n))
subtract.place(x=245,y=289)

icon = PhotoImage(file='icons3/arrow.png')
btn_delete = Button(width=51,height=35, font='times 15 bold', fg='white', bg='#e67019', relief='groove', command=funcDelete,image=icon)
btn_delete.place(x=246,y=360)

statusBar= Label(root, text='History :', relief='sunken',height=3,anchor='w',font='verdana 11 bold')
statusBar.pack(side=BOTTOM,fil=X)


root.protocol('WM_DELETE_WINDOW', exit)
root.mainloop()

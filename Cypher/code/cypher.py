from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import string
import collections
import os


window = Tk()
window.title('Ceaser Cypher')
image_path = os.getcwd()
window.iconphoto(False,PhotoImage(file=image_path+'\\icons\\miscellaneous-gold-bird.png'))
WIDTH = 700
HEIGHT = 400
window.geometry(f'{WIDTH}x{HEIGHT}')
window.resizable(False,False)
BGCOLOR = '#400101'
FONTSTYLE = 'Arial'
FONTSIZE = 8

# Creation of the Tab menu
Tab_menu = ttk.Notebook(window,width=WIDTH,height=HEIGHT-25)
Tab_menu.pack()

# **** START OF CYPHER TAB ****
cypher_tab = Frame(Tab_menu,bg=BGCOLOR)

def encrypt_data():

    lower_alphabet = collections.deque(string.ascii_lowercase)
    upper_alphabet = collections.deque(string.ascii_uppercase)
    symbols_alphabet = collections.deque(string.punctuation)
    numeric_alphabet = collections.deque(string.digits)
    

    encrypted_textbox.config(state=NORMAL)
    encrypted_textbox.delete(1.0,END)
    encrypted_textbox.config(state=DISABLED)

    security_lvl = Toplevel()
    security_lvl.title('Encryption lvl')
    security_lvl.geometry('250x150')
    security_lvl.iconphoto(False,PhotoImage(file=image_path+'\\icons\\miscellaneous-gold-bird.png'))
    security_lvl.resizable(False,False)


    def cipher():
        
        decrypted_text = str(decrypted_textbox.get(1.0,END))

        lower_alphabet.rotate(int(sc_lvl))
        upper_alphabet.rotate(int(sc_lvl))
        symbols_alphabet.rotate(int(sc_lvl))
        numeric_alphabet.rotate(int(sc_lvl))

        lower = ''.join(list(lower_alphabet))
        upper = ''.join(list(upper_alphabet))
        symbols = ''.join(list(symbols_alphabet))
        numbers = ''.join(list(numeric_alphabet))

        encrypted_textbox.config(state=NORMAL)
        encrypted_textbox.insert(END,decrypted_text.translate(str.maketrans(string.ascii_lowercase,lower)).translate(str.maketrans(string.ascii_uppercase,upper)).translate(str.maketrans(string.punctuation,symbols)).translate(str.maketrans(string.digits,numbers)))
        encrypted_textbox.config(state=DISABLED)


    def set_security_lvl():
        global sc_lvl
        sc_lvl = int(security_value.get())
        security_lvl.destroy()
        cipher()
        

    def cancel_security_lvl():
        security_lvl.destroy()


    # Security Background
    main_security_frame = Frame(security_lvl,bg=BGCOLOR,height=150)
    main_security_frame.pack(fill=BOTH)

    # Security Labels
    securtiy_label_frame1 = Frame(main_security_frame,bg=BGCOLOR)
    sc_label1 = Label(securtiy_label_frame1,text='Input Encryption LvL',font=('Segoe Script Bold',14),bg=BGCOLOR,fg='#ffffff')
    sc_label1.grid(row=0,column=0)
    securtiy_label_frame1.place(x=10,y=15)

    securtiy_label_frame2 = Frame(main_security_frame,bg=BGCOLOR)
    sc_label2 = Label(securtiy_label_frame2,text='1 - 32',font=('Segoe Script Bold',12),bg=BGCOLOR,fg='#ffffff')
    sc_label2.grid(row=0,column=0)
    securtiy_label_frame2.place(x=50,y=54)

    # Security lvl Entry box
    security_entrybox_frame = Frame(main_security_frame,bg=BGCOLOR)
    # Creating character restrictions for the Entry box
    def entry_box_length(*args):
        try:
            entry_data = str(security_value.get())
            for char in entry_data:
                if char.isalpha()==True:
                    security_value.set(0)
            if len(entry_data) > 2:
                security_value.set(entry_data[:2])
            if int(entry_data) > 32:
                security_value.set(32)
        except TclError and ValueError:
            pass
    security_value = StringVar()
    security_value.set(0)
    security_value.trace('w',entry_box_length)
    sc_enrtybox = Entry(security_entrybox_frame,textvariable=security_value,width=2,justify=RIGHT)
    sc_enrtybox.grid(row=0,column=0)
    security_entrybox_frame.place(x=120,y=60)

    # Security Buttons
    security_button_frame = Frame(main_security_frame,bg=BGCOLOR)
    sc_button = Button(security_button_frame,text='Set',padx=16,bg='#080808',fg='#ffffff',activebackground='#080808',activeforeground='#db0000',font=('Segoe Script Bold',8),command=set_security_lvl)
    sc_button.grid(row=0,column=0)
    sc_button2 = Button(security_button_frame,text='Cancel',padx=4,bg='#080808',fg='#ffffff',activebackground='#080808',activeforeground='#db0000',font=('Segoe Script Bold',8),command=cancel_security_lvl)
    sc_button2.grid(row=0,column=1)
    security_button_frame.place(x=70,y=90)


def decrypt_data():
   
    decrypted_textbox.delete(1.0,END)

    def cipher(input,index):

        lower_alphabet = collections.deque(string.ascii_lowercase)
        upper_alphabet = collections.deque(string.ascii_uppercase)
        symbols_alphabet = collections.deque(string.punctuation)
        numeric_alphabet = collections.deque(string.digits)
        
        lower_alphabet.rotate(index)
        upper_alphabet.rotate(index)
        symbols_alphabet.rotate(index)
        numeric_alphabet.rotate(index)

        lower = ''.join(list(lower_alphabet))
        upper = ''.join(list(upper_alphabet))
        symbols = ''.join(list(symbols_alphabet))
        numbers = ''.join(list(numeric_alphabet))
        
        return input.translate(str.maketrans(lower,string.ascii_lowercase)).translate(str.maketrans(upper,string.ascii_uppercase)).translate(str.maketrans(symbols,string.punctuation)).translate(str.maketrans(numbers,string.digits))

    for x in range(len(string.punctuation)):
        data = f'{x} | {cipher(encrypted_textbox.get(1.0,END),x)}'
        decrypted_textbox.insert(END,data)


def import_file():

    file = askopenfilename(title='Choose a File',filetypes=(('Text Files','*.txt'),('All Files','*.*')))

    try:
        userfile = open(file)
    except FileNotFoundError:
        return

    import_window = Toplevel()
    import_window.title('Import')
    import_window.geometry('250x150')
    import_window.iconphoto(False,PhotoImage(file=image_path+'\\icons\\miscellaneous-gold-bird.png'))
    import_window.resizable(False,False)

        
    def close_import_window():

        if encrypt_variable.get() == True:
            decrypted_textbox.delete(1.0,END)
            decrypted_textbox.insert(END,userfile.read())
        
        if decrypt_variable.get() == True:
            encrypted_textbox.config(state=NORMAL)
            encrypted_textbox.delete(1.0,END)
            encrypted_textbox.insert(END,userfile.read())
            encrypted_textbox.config(state=DISABLED)

        print(encrypt_variable.get())
        print(decrypt_variable.get())
        import_window.destroy()

    # Security Background
    main_import_frame = Frame(import_window,bg=BGCOLOR,height=150)
    main_import_frame.pack(fill=BOTH)

    # Security Labels
    import_label_frame1 = Frame(main_import_frame,bg=BGCOLOR)
    sc_label1 = Label(import_label_frame1,text='Choose What Happens',font=('Segoe Script Bold',14),bg=BGCOLOR,fg='#ffffff')
    sc_label1.grid(row=0,column=0)
    import_label_frame1.place(x=10,y=10)

    XVIEW = 85
    import_label_frame2 = Frame(main_import_frame,bg=BGCOLOR)
    sc_label2 = Label(import_label_frame2,text='Encrypt File',font=('Segoe Script Bold',10),bg=BGCOLOR,fg='#ffffff')
    sc_label2.grid(row=0,column=0)
    import_label_frame2.place(x=XVIEW,y=50)

    import_label_frame3 = Frame(main_import_frame,bg=BGCOLOR)
    sc_label3 = Label(import_label_frame3,text='Decrypt File',font=('Segoe Script Bold',10),bg=BGCOLOR,fg='#ffffff')
    sc_label3.grid(row=0,column=0)
    import_label_frame3.place(x=XVIEW,y=75)

    # Security Buttons
    import_checkbutton_frame = Frame(main_import_frame,bg=BGCOLOR)
    encrypt_variable = BooleanVar()
    encrypt_checkbutton = Checkbutton(import_checkbutton_frame,variable=encrypt_variable,bg=BGCOLOR,activebackground=BGCOLOR,command=close_import_window)
    encrypt_checkbutton.grid(row=0,column=0)

    decrypt_variable = BooleanVar()
    decrypt_checkbutton = Checkbutton(import_checkbutton_frame,variable=decrypt_variable,bg=BGCOLOR,activebackground=BGCOLOR,command=close_import_window)
    decrypt_checkbutton.grid(row=1,column=0)
    import_checkbutton_frame.place(x=60,y=51)

    import_button_frame = Frame(main_import_frame,bg=BGCOLOR)
    sc_button2 = Button(import_button_frame,text='Cancel',padx=4,bg='#080808',fg='#ffffff',activebackground='#080808',activeforeground='#db0000',font=('Segoe Script Bold',8),command=close_import_window)
    sc_button2.grid(row=0,column=0)
    import_button_frame.place(x=95,y=115)


def export_file():

    file = asksaveasfile(title='Export the data',initialfile='data',defaultextension='.txt',filetypes=(('text files','*.txt'),('all files','*.*')),)
    
    if file == None:
        return

    export_window = Toplevel()
    export_window.title('Export')
    export_window.geometry('250x150')
    export_window.iconphoto(False,PhotoImage(file=image_path+'\\icons\\miscellaneous-gold-bird.png'))
    export_window.resizable(False,False)

    def close_export_window():

        if encrypt_variable.get() == True:

            text = encrypted_textbox.get(1.0,END)

        if decrypt_variable.get() == True:
            text = decrypted_textbox.get(1.0,END)

        try:
            file.write(text)
            file.close()
        except AttributeError:
            pass

        export_window.destroy()

    # Security Background
    main_import_frame = Frame(export_window,bg=BGCOLOR,height=150)
    main_import_frame.pack(fill=BOTH)

    # Security Labels
    import_label_frame1 = Frame(main_import_frame,bg=BGCOLOR)
    sc_label1 = Label(import_label_frame1,text='Choose What Happens',font=('Segoe Script Bold',14),bg=BGCOLOR,fg='#ffffff')
    sc_label1.grid(row=0,column=0)
    import_label_frame1.place(x=10,y=10)

    XVIEW = 85
    import_label_frame2 = Frame(main_import_frame,bg=BGCOLOR)
    sc_label2 = Label(import_label_frame2,text='Save Encrypted Text',font=('Segoe Script Bold',10),bg=BGCOLOR,fg='#ffffff')
    sc_label2.grid(row=0,column=0)
    import_label_frame2.place(x=XVIEW,y=50)

    import_label_frame3 = Frame(main_import_frame,bg=BGCOLOR)
    sc_label3 = Label(import_label_frame3,text='Save Decrypted Text',font=('Segoe Script Bold',10),bg=BGCOLOR,fg='#ffffff')
    sc_label3.grid(row=0,column=0)
    import_label_frame3.place(x=XVIEW,y=75)

    # Security Buttons
    import_checkbutton_frame = Frame(main_import_frame,bg=BGCOLOR)
    encrypt_variable = BooleanVar()
    encrypt_checkbutton = Checkbutton(import_checkbutton_frame,variable=encrypt_variable,bg=BGCOLOR,activebackground=BGCOLOR,command=close_export_window)
    encrypt_checkbutton.grid(row=0,column=0)

    decrypt_variable = BooleanVar()
    decrypt_checkbutton = Checkbutton(import_checkbutton_frame,variable=decrypt_variable,bg=BGCOLOR,activebackground=BGCOLOR,command=close_export_window)
    decrypt_checkbutton.grid(row=1,column=0)
    import_checkbutton_frame.place(x=60,y=51)

    import_button_frame = Frame(main_import_frame,bg=BGCOLOR)
    sc_button2 = Button(import_button_frame,text='Cancel',padx=4,bg='#080808',fg='#ffffff',activebackground='#080808',activeforeground='#db0000',font=('Segoe Script Bold',8),command=close_export_window)
    sc_button2.grid(row=0,column=0)
    import_button_frame.place(x=95,y=115)


def clear_dectrypted_field():
    decrypted_textbox.delete(1.0,END)


def clear_enctrypted_field():
    encrypted_textbox.config(state=NORMAL)
    encrypted_textbox.delete(1.0,END)
    encrypted_textbox.config(state=DISABLED)

# Main Cypher Title
title_frame = Frame(cypher_tab,bg=BGCOLOR)
title_label = Label(title_frame,text='Caeser Cypher',font=('Segoe Script Bold',28),bg=BGCOLOR,fg='#ffffff')
title_label.grid(row=0,column=0)
title_frame.place(x=205,y=0)
# Main Cypher Checkbuttons
edit_encrypted_textbox_frame = Frame(cypher_tab,bg=BGCOLOR)
def edit_encrypted_textbox():
    if edit_textbox_variable.get() == True:
        encrypted_textbox.config(state=NORMAL)
    if edit_textbox_variable.get() == False:
        encrypted_textbox.config(state=DISABLED)

edit_textbox_variable = BooleanVar()
edit_encrypted_textbox_checkbutton = Checkbutton(edit_encrypted_textbox_frame,variable=edit_textbox_variable,bg=BGCOLOR,activebackground=BGCOLOR,activeforeground='#ffffff',command=edit_encrypted_textbox)
edit_encrypted_textbox_checkbutton.grid(row=0,column=0)
edit_encrypted_textbox_label = Label(edit_encrypted_textbox_frame,text='Edit Encryption Box',font=('Segoe Script Bold',10),fg='#ffffff',bg=BGCOLOR)
edit_encrypted_textbox_label.grid(row=0,column=1)
edit_encrypted_textbox_frame.place(x=430,y=100)
# Main Cypher entries/buttons/labels
textbox_frame = Frame(cypher_tab,bg=BGCOLOR)
 # Text Box Titles
encrypt_label = Label(textbox_frame,text='Decrypted Text',font=('Segoe Script Bold',10),bg=BGCOLOR,fg='#ffffff')
encrypt_label.grid(row=0,column=0)
decrypt_label = Label(textbox_frame,text='Encrypted Text',font=('Segoe Script Bold',10),bg=BGCOLOR,fg='#ffffff')
decrypt_label.grid(row=0,column=3)
 # Buttons
encrypt_btn = Button(textbox_frame,text='Encrypt',padx=-3,bg='#080808',fg='#ffffff',activebackground='#080808',activeforeground='#db0000',font=('Segoe Script Bold',8),command=encrypt_data)
encrypt_btn.grid(row=1,column=2,padx=4)
decrypt_btn = Button(textbox_frame,text='Decrypt',padx=-3,bg='#080808',fg='#ffffff',activebackground='#080808',activeforeground='#db0000',font=('Segoe Script Bold',8),command=decrypt_data)
decrypt_btn.grid(row=2,column=2,padx=4)
import_btn = Button(textbox_frame,text='Import',padx=4,bg='#080808',fg='#ffffff',activebackground='#080808',activeforeground='#db0000',font=('Segoe Script Bold',8),command=import_file)
import_btn.grid(row=3,column=2,padx=4)
export_btn = Button(textbox_frame,text='Export',padx=4,bg='#080808',fg='#ffffff',activebackground='#080808',activeforeground='#db0000',font=('Segoe Script Bold',8),command=export_file)
export_btn.grid(row=4,column=2,padx=4)
encrypt_clear_btn = Button(textbox_frame,text='Clear Encrypted Field',padx=4,bg='#080808',fg='#ffffff',activebackground='#080808',activeforeground='#db0000',font=('Segoe Script Bold',8),command=clear_enctrypted_field)
encrypt_clear_btn.grid(row=5,column=3,pady=4)
decrypt_clear_btn = Button(textbox_frame,text='Clear Decryted Field',padx=4,bg='#080808',fg='#ffffff',activebackground='#080808',activeforeground='#db0000',font=('Segoe Script Bold',8),command=clear_dectrypted_field)
decrypt_clear_btn.grid(row=5,column=0,pady=4)
 # Text Boxes
decrypted_textbox = Text(textbox_frame,bg='#f5d395',font=(FONTSTYLE,FONTSIZE),width=48,height=10)
decrypted_textbox.grid(row=1,column=0,rowspan=4)
encrypted_textbox = Text(textbox_frame,bg='#f5d395',font=(FONTSTYLE,FONTSIZE),width=48,height=10)
encrypted_textbox.grid(row=1,column=3,rowspan=4)
encrypted_textbox.config(state=DISABLED)
 # Scrollbars
encrypted_scrollbar = Scrollbar(textbox_frame,orient=VERTICAL,command=encrypted_textbox.yview)
encrypted_scrollbar.grid(row=1,column=4,rowspan=4,sticky=N+S)
encrypted_textbox.config(yscrollcommand=encrypted_scrollbar.set)
decrypted_scrollbar = Scrollbar(textbox_frame,orient=VERTICAL,command=decrypted_textbox.yview)
decrypted_scrollbar.grid(row=1,column=1,rowspan=4,sticky=N+S)
decrypted_textbox.config(yscrollcommand=decrypted_scrollbar.set)
textbox_frame.place(x=7,y=130)

# **** END OF CYPHER TAB ****
cypher_tab.pack()


Tab_menu.add(cypher_tab,text='Caeser Cypher')



window.mainloop()

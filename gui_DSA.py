from tkinter import *
from src.DS import *
#const
btn_width = 100 
btn_height = 40 
ent_width = 150
ent_height = 30
win_width = 800
win_height = 320

er = "Error"
err_open = r"You must to choose any file `\_(•_•)_/`"


def main():

    def go_sign():        
        root.destroy()
        sign_frame()

    def go_check():
        root.destroy()
        check_frame()

    root = Tk()
    root.geometry("{}x{}".format(win_width, win_height))
    root.title("DSA")
    root.resizable(False, False)
    root.focus_force()
    
    fr_mainmenu = Frame(root, bg = "gray", width = win_width, \
                        height = win_height)

    fr_mainmenu.pack(fill="both", side="top", expand=True)

    btn_enc = Button(fr_mainmenu, text = "Make sign", bg='pink', fg='black', command = go_sign)
    btn_dec = Button(fr_mainmenu, text = "Check sign", bg='pink', fg='black', command = go_check)

    btn_enc.place(relx=0.5, x = -btn_width // 2, \
                  rely=0.5, y = -btn_height, \
                  width=btn_width,height=btn_height)
    btn_dec.place(relx=0.5,  x = -btn_width // 2, \
                  rely=0.5, y = 1, \
                  width=btn_width, height=btn_height)
    
    root.mainloop()


def sign_frame():

    def go_back():
        root.destroy()
        main()

    def go_sign():

        p = p_enter.get()
        if is_number(p):
            p = int(p)   
        else:
            p = 0
            show_error(20)
            return
        q = q_enter.get()
        if is_number(q):
            q = int(q)
        else:
            q = 0
            show_error(10)
            return
        h = h_enter.get()
        if is_number(h):
            h = int(h) 
        else:
            h = 0
            show_error(30)
            return
        k = k_enter.get()
        if is_number(k):
            k = int(k) 
        else:
            k = 0
            show_error(60)
            return
        x = x_enter.get()
        if is_number(x):
            x = int(x)
        else:
            x = 0
            show_error(50)
            return

        fname = open_file()
        if (fname):    
            data, r, s, y, fhash = dsa_file_sign(p=p, q=q, h=h, k=k, x=x, filename= fname)

            if (data != "-Error"):
                textbox.configure(state=NORMAL)
                textbox.delete(1.0, END)
                textbox.insert(1.0, "SHA-1: {hash}\nY: {y}\nR: {r}\nS: {s}\n".format(hash=fhash, y=y, r=r, s=s)) 
                textbox.configure(state=DISABLED)
            else:
                show_error(r)
        else:
            show_error(7)   

    root = Tk()
    root.geometry("{}x{}".format(win_width, win_height))
    root.title("DSA")
    root.resizable(False, False)
    root.focus_force()

    #Frame
    fr_sign = Frame(root, bg="gray", width=win_width, \
                        height=win_height)
    fr_sign.pack(side="top")

    #Labels    
    lb_p = Label(fr_sign, text="P = ")
    lb_p.place(relx=.04, rely=.06)
    lb_q = Label(fr_sign, text="Q = ")
    lb_q.place(relx=.04, rely=.18)
    lb_h = Label(fr_sign, text="H = ")
    lb_h.place(relx=.04, rely=.30)
    lb_x = Label(fr_sign, text="X = ")
    lb_x.place(relx=.04, rely=.42)
    lb_k = Label(fr_sign, text="K = ")
    lb_k.place(relx=.04, rely=.54)

    #Entry
    p_enter = Entry(fr_sign, font="Tahoma")
    p_enter.place(relx=.22, x=-ent_width//2, rely=.05, \
                  width=ent_width, height=ent_height)
    q_enter = Entry(fr_sign, font="Tahoma")
    q_enter.place(relx=.22, x=-ent_width//2, rely=.17,  \
                  width=ent_width, height=ent_height)
    h_enter = Entry(fr_sign, font="Tahoma")
    h_enter.place(relx=.22, x=-ent_width//2, rely=.29, \
                  width=ent_width, height=ent_height)

    x_enter = Entry(fr_sign, font="Tahoma")
    x_enter.place(relx=.22, x=-ent_width//2, rely=.41, \
                  width=ent_width, height=ent_height)

    k_enter = Entry(fr_sign, font="Tahoma")
    k_enter.place(relx=.22, x=-ent_width//2, rely=.53, \
                  width=ent_width, height=ent_height)

    textbox = Text(fr_sign, font="Arial 18", bg = "#c3aee2", wrap=WORD, \
                   state=NORMAL)
    textbox.place(relx=.40, height=win_height, width=win_width - win_width * 0.4)
    textbox.insert(1.0, "") 
    textbox.configure(state=DISABLED)
    scroll = Scrollbar(textbox, command=textbox.yview)
    textbox["yscrollcommand"] = scroll.set
    scroll.pack(side="right", fill="y")

    #Buttons
    btn_back = Button(fr_sign, text="Make Sign", bg='pink', fg='black', command = go_sign)
    btn_back.place(relx=.25, x=-btn_width//2, rely=.67, width=btn_width, height=btn_height)
    btn_back = Button(fr_sign, text="Back", bg='pink', fg='black', command = go_back)
    btn_back.place(relx=.25, x=-btn_width//2, rely=.8, width=btn_width, height=btn_height)

    root.mainloop()

def check_frame():

    def go_back():
        root.destroy()
        main()

    def go_check():
        

        def insert_tb_msg(msg):
            '''
            Вставка в textbox данного фрейма сообщением
            '''
            textbox.configure(state=NORMAL)
            textbox.delete(1.0, END)
            textbox.insert(1.0, msg) 
            textbox.configure(state=DISABLED)

        p = p_enter.get()
        if is_number(p):
            p = int(p)   
        else:
            p = 0
            show_error(2)
            return
        q = q_enter.get()
        if is_number(q):
            q = int(q)
        else:
            q = 0
            show_error(1)
            return
        h = h_enter.get()
        if is_number(h):
            h = int(h) 
        else:
            h = 0
            show_error(3)
            return
        y = y_enter.get()
        if is_number(k):
            y = int(y) 
        else: 
            y = 0
            _show_error("Are you entered Y?")
            return

        fname = open_file()
        if (fname):    
            
            result = dsa_check_file_sign(p=p, q=q, h=h, y=y, filename=fname)

            if result == 0:
                insert_tb_msg("SUCCESS")
            elif result == -1:
                insert_tb_msg("REJECT")
            else:
                show_error(result)         

    root = Tk()
    root.geometry("{}x{}".format(win_width, win_height))
    root.title("Check sign")
    root.resizable(False, False)
    root.focus_force()

    #Frame
    fr_ch_sign = Frame(root, bg="gray", width=win_width, \
                        height=win_height)
    fr_ch_sign.pack(side="top")

    #Labels    
    lb_p = Label(fr_ch_sign, text="P = ")
    lb_p.place(relx=.04, rely=.06)
    lb_q = Label(fr_ch_sign, text="Q = ")
    lb_q.place(relx=.04, rely=.18)
    lb_h = Label(fr_ch_sign, text="H = ")
    lb_h.place(relx=.04, rely=.30)
    lb_y = Label(fr_ch_sign, text="Y = ")
    lb_y.place(relx=.04, rely=.42)

    #Entry
    p_enter = Entry(fr_ch_sign, font="Tahoma")
    p_enter.place(relx=.22, x=-ent_width//2, rely=.05, \
                  width=ent_width, height=ent_height)
    q_enter = Entry(fr_ch_sign, font="Tahoma")
    q_enter.place(relx=.22, x=-ent_width//2, rely=.17,  \
                  width=ent_width, height=ent_height)
    h_enter = Entry(fr_ch_sign, font="Tahoma")
    h_enter.place(relx=.22, x=-ent_width//2, rely=.29, \
                  width=ent_width, height=ent_height)

    y_enter = Entry(fr_ch_sign, font="Tahoma")
    y_enter.place(relx=.22, x=-ent_width//2, rely=.41, \
                  width=ent_width, height=ent_height)

    textbox = Text(fr_ch_sign, font="Arial 18", bg = "#c3aee2", wrap=WORD, \
                   state=NORMAL)
    textbox.place(relx=.40, height=win_height, width=win_width - win_width * 0.4)
    textbox.insert(1.0, "") 
    textbox.configure(state=DISABLED)
    scroll = Scrollbar(textbox, command=textbox.yview)
    textbox["yscrollcommand"] = scroll.set
    scroll.pack(side="right", fill="y")

    #Buttons
    btn_back = Button(fr_ch_sign, text="Check Sign", bg='pink', fg='black', command = go_check)
    btn_back.place(relx=.25, x=-btn_width//2, rely=.67, width=btn_width, height=btn_height)
    btn_back = Button(fr_ch_sign, text="Back", bg='pink', fg='black', command = go_back)
    btn_back.place(relx=.25, x=-btn_width//2, rely=.8, width=btn_width, height=btn_height)

    root.mainloop()

def _show_error(msg):
    from tkinter import messagebox
    root = Tk()
    root.withdraw() #Для messagebox нужно окно, а то оно создается пустым `\_(•_•)_/`
    messagebox.showerror(er, msg)
    print(msg)
    root.destroy()
    return 0
    
def open_file():
    '''

    '''
    filename = ""
    from tkinter import filedialog
    root = Tk()
    root.withdraw()
    filename = filedialog.askopenfilename(initialdir = "/", title="Select file")
    print("Open: {}".format(filename))
    root.destroy()
    if (filename):
        return filename

def show_error(err):
    if err == 1:
        _show_error("Q is not correct")
    if err == 2:
        _show_error("P is not correct")
    if err == 3:
        _show_error("H is not correct")
    if err == 4:
        _show_error("G is not correct")
    if err == 5:
        _show_error("X is not correct")
    if err == 6:
        _show_error("K is not correct")
    if err == -1:
        _show_error("Try new K")
    if err == 10:
        _show_error("Please, enter Q")
    if err == 20:
        _show_error("Please, enter P")
    if err == 30:
        _show_error("Please, enter H")
    if err == 50:
        _show_error("Please, enter X")
    if err == 60:
        _show_error("Please, enter K")
    if err == 7:
        _show_error(err_open)
    if err == 100:
        _show_error("Error in getting R or S...\nMay be problen in symbol '|' ")



if __name__ == "__main__":
    main()




#Bibliotecas:
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import DataBaser


#Criar a Janela
janela = Tk()
janela.title("DP System - Access panel")
janela.geometry("600x300")
janela.configure(background="white")
janela.resizable(width=False, height=False)
janela.iconbitmap(default="icons/LogoIcon.ico")

#TransparenciaJanela
janela.attributes("-alpha", 0.9)


#---CarregandoImagens
logo = PhotoImage(file="icons/logo.png")


#-----Widgets
LeftFrame = Frame(janela, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(janela, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

#ColocandoLogo
logolabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
logolabel.place(x=50, y=100)

#NomeUsuário
UserLabel = Label(RightFrame, text="Usuário: ", font=("Century", 20), bg="MIDNIGHTBLUE", fg="White")
UserLabel.place(x=5, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=140, y=110)

#Senha
PassLabel = Label(RightFrame, text="Password: ", font=("Century", 20), bg="MIDNIGHTBLUE", fg="White")
PassLabel.place(x=5, y=160)

PassEntry = ttk.Entry(RightFrame, width=30, show="*")
PassEntry.place(x=140, y=170)

#------Botões

def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    DataBaser.cursor.execute('''
    SELECT * FROM Users
    WHERE (User = ? AND Password = ?)                          
    ''', (User, Pass))
    print("Selecionou")

    #verificar o Login...
    VerifyLogin = DataBaser.cursor.fetchone()
    try:
        if User in VerifyLogin and Pass in VerifyLogin:
            messagebox.showinfo(title= "Login Info", message="Welcome, Access Agreed.")
    except:
        messagebox.showinfo(title="Login Info", message="Denied Access, please Sign up.")

LoginButton = ttk.Button(RightFrame, text="Login", width= 30, command=Login)
LoginButton.place(x=185, y=220)

def Register():
    #removendo widgets register e login
    LoginButton.place(x=5000,)
    RegisterButton.place(x=5000)
    #Inserindo widgets de cadastro
    NomeLabel = Label(RightFrame, text="Name:", font=("Century", 20), bg="MIDNIGHTBLUE", fg="White")
    NomeLabel.place(x=15, y=10)

    NomeEntry = ttk.Entry(RightFrame, width=30)
    NomeEntry.place(x=130, y=20)

    EmailLabel = Label(RightFrame, text="Email:", font=("Century", 20), bg="MIDNIGHTBLUE", fg="White" )
    EmailLabel.place(x=15, y=40)

    EmailEntry = ttk.Entry(RightFrame, width=30)
    EmailEntry.place(x=130, y=50)

    def RegisterToDataBaser():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()
        
        if (Name == "" or Email == "" or User == "" or Pass == ""):
            messagebox.showerror(title="Register Error", message="Fill All!")
        else:
            DataBaser.cursor.execute('''
            INSERT INTO USERS(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            ''', (Name, Email, User, Pass))
            DataBaser.conn.commit
            messagebox.showinfo(title="Register Info", message="Register Sucessfull.")


    RegisterReg = ttk.Button(RightFrame, text="Register", width= 30, command=RegisterToDataBaser)
    RegisterReg.place(x=100, y=220)

    def BackToLogin():
        #removendo widgets de cadastro nome e email...
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)

        RegisterReg.place(x=5000)
        Back.place(x=5000)


        #Trazendo de volta o login e o register que tiramos na outra def(register)...
        LoginButton.place(x=185, y=220)
        RegisterButton.place(x=15, y=220)
    
   
    Back = ttk.Button(RightFrame, text="Back", width=15, command=BackToLogin)
    Back.place(x=125, y=260)

RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)
RegisterButton.place(x= 15, y = 220)


janela.mainloop()
from tkinter import*

#--------------------Tkinter Base Setup ---------------------# 

window = Tk()
window.title("BitLink End-Point")
window.geometry("1200x650")
window.minsize("1200","650")
window.maxsize("1200","650")

winFrame = Frame(window,width="1200",height="650",bg="black")
winFrame.pack()
winFrame.pack_propagate(0)

#--------------------Tkinter Base Setup End ------------------# 

def HomeViewDarkTheme(event):

    #--------------------Global Var --------------------#  
    global winFrame
    

    #--------------------Global Var End -----------------# 

    winFrame.destroy()



    #--------------------Main Frame ---------------------# 

    winFrame = Frame(window,width="1200",height="650",bg="black")
    winFrame.pack()
    winFrame.pack_propagate(0)

    #--------------------Main Frame End ------------------# 

    #--------------------Home Button --------------------#

    homeButtonImg = PhotoImage(file="res\\Blue Asset\\Dark theme\\Buttons\\Non-Hoved\\home.png").subsample(2,2)
    hovHomeButtonImg = PhotoImage(file="res\\Blue Asset\\Dark theme\\Buttons\\Hoved\\hovHome.png").subsample(2,2)

    def HomeButtonEnterFrame(event):
        homeButton.config(image=hovHomeButtonImg)

    def HomeButtonLeaveFrame(event):
        homeButton.config(image=homeButtonImg)


    homeButton = Label(winFrame,image=homeButtonImg,bg="black",cursor="hand2")
    homeButton.place(x=30,y=200)

    homeButton.bind('<Enter>',HomeButtonEnterFrame)
    homeButton.bind('<Leave>',HomeButtonLeaveFrame)

    #--------------------Home Button End------------------#

    #--------------------Scan Button ---------------------#

    scanButtonImg = PhotoImage(file="res\\Blue Asset\\Dark theme\\Buttons\\Non-Hoved\\scan.png").subsample(2,2)
    hovScanButtonImg = PhotoImage(file="res\\Blue Asset\\Dark theme\\Buttons\\Hoved\\hovScan.png").subsample(2,2)

    def ScanButtonEnterFrame(event):
        scanButton.config(image=hovScanButtonImg)

    def ScanButtonLeaveFrame(event):
        scanButton.config(image=scanButtonImg)


    scanButton = Label(winFrame,image=scanButtonImg,bg="black",cursor="hand2")
    scanButton.place(x=30,y=240)

    scanButton.bind('<Enter>',ScanButtonEnterFrame)
    scanButton.bind('<Leave>',ScanButtonLeaveFrame)

    #--------------------Scan Button End------------------#

    #--------------------Health Button -------------------#

    healthButtonImg = PhotoImage(file="res\\Blue Asset\\Dark theme\\Buttons\\Non-Hoved\\health.png").subsample(2,2)
    hovHealthButtonImg = PhotoImage(file="res\\Blue Asset\\Dark theme\\Buttons\\Hoved\\hovHealth.png").subsample(2,2)

    def HealthButtonEnterFrame(event):
        healthButton.config(image=hovHealthButtonImg)

    def HealthButtonLeaveFrame(event):
        healthButton.config(image=healthButtonImg)


    healthButton = Label(winFrame,image=healthButtonImg,bg="black",cursor="hand2")
    healthButton.place(x=30,y=280)

    healthButton.bind('<Enter>',HealthButtonEnterFrame)
    healthButton.bind('<Leave>',HealthButtonLeaveFrame)

    #--------------------Health Button End ---------------#



    #--------------------Accounts Button -----------------#

    accountsButtonImg = PhotoImage(file="res\\Blue Asset\\Dark theme\\Buttons\\Non-Hoved\\accounts.png").subsample(2,2)
    hovAccountsButtonImg = PhotoImage(file="res\\Blue Asset\\Dark theme\\Buttons\\Hoved\\hovAccounts.png").subsample(2,2)

    def AccountsButtonEnterFrame(event):
        accountsButton.config(image=hovAccountsButtonImg)

    def AccountsButtonLeaveFrame(event):
        accountsButton.config(image=accountsButtonImg)


    accountsButton = Label(winFrame,image=accountsButtonImg,bg="black",cursor="hand2")
    accountsButton.place(x=30,y=320)

    accountsButton.bind('<Enter>',AccountsButtonEnterFrame)
    accountsButton.bind('<Leave>',AccountsButtonLeaveFrame)

    #--------------------Accounts Button End -------------#

    #--------------------Internet Button -----------------#

    internetButtonImg = PhotoImage(file="res\\Blue Asset\\Dark theme\\Buttons\\Non-Hoved\\internet.png").subsample(2,2)
    hovInternetButtonImg = PhotoImage(file="res\\Blue Asset\\Dark theme\\Buttons\\Hoved\\hovInternet.png").subsample(2,2)

    def InternetButtonEnterFrame(event):
        internetButton.config(image=hovInternetButtonImg)

    def InternetButtonLeaveFrame(event):
        internetButton.config(image=internetButtonImg)


    internetButton = Label(winFrame,image=internetButtonImg,bg="black",cursor="hand2")
    internetButton.place(x=30,y=360)

    internetButton.bind('<Enter>',InternetButtonEnterFrame)
    internetButton.bind('<Leave>',InternetButtonLeaveFrame)

    #--------------------Internet Button End -------------#

    #----------------White Theme Change Button------------#

    def WhiteThemeChangeButtonEnter(event):
        whiteThemeChangeButton.config(fg="aqua")
    
    def WhiteThemeChangeButtonLeave(event):
        whiteThemeChangeButton.config(fg="white")

    def WhiteThemeCall(event):
        HomeViewWhiteTheme()

    whiteThemeChangeButton = Label(winFrame,text="White Theme v1.0",bg="black",cursor="hand2",
                                    font=( "Poppins",10,"bold"),fg="white")
    whiteThemeChangeButton.place(x=1060,y=610)

    whiteThemeChangeButton.bind('<Enter>',WhiteThemeChangeButtonEnter)
    whiteThemeChangeButton.bind('<Leave>',WhiteThemeChangeButtonLeave)
    whiteThemeChangeButton.bind('<Button-1>',WhiteThemeCall)

    #----------------White Theme Change Button------------#




def HomeViewWhiteTheme():

    #--------------------Global Var --------------------#  
    global winFrame
    

    #--------------------Global Var End -----------------# 

    winFrame.destroy()



    #--------------------Main Frame ---------------------# 

    winFrame = Frame(window,width="1200",height="650",bg="white")
    winFrame.pack()
    winFrame.pack_propagate(0)

    #--------------------Main Frame End ------------------# 

    #--------------------Home Button --------------------#

    homeButtonImg = PhotoImage(file="res\\Blue Asset\\White theme\\Buttons\\Non-Hoved\\home.png").subsample(2,2)
    hovHomeButtonImg = PhotoImage(file="res\\Blue Asset\\White theme\\Buttons\\Hoved\\hovHome.png").subsample(2,2)

    def HomeButtonEnterFrame(event):
        homeButton.config(image=hovHomeButtonImg)

    def HomeButtonLeaveFrame(event):
        homeButton.config(image=homeButtonImg)


    homeButton = Label(winFrame,image=homeButtonImg,bg="white",cursor="hand2")
    homeButton.place(x=30,y=200)

    homeButton.bind('<Enter>',HomeButtonEnterFrame)
    homeButton.bind('<Leave>',HomeButtonLeaveFrame)

    #--------------------Home Button End------------------#

    #--------------------Scan Button ---------------------#

    scanButtonImg = PhotoImage(file="res\\Blue Asset\\White theme\\Buttons\\Non-Hoved\\scan.png").subsample(2,2)
    hovScanButtonImg = PhotoImage(file="res\\Blue Asset\\White theme\\Buttons\\Hoved\\hovScan.png").subsample(2,2)

    def ScanButtonEnterFrame(event):
        scanButton.config(image=hovScanButtonImg)

    def ScanButtonLeaveFrame(event):
        scanButton.config(image=scanButtonImg)


    scanButton = Label(winFrame,image=scanButtonImg,bg="white",cursor="hand2")
    scanButton.place(x=30,y=240)

    scanButton.bind('<Enter>',ScanButtonEnterFrame)
    scanButton.bind('<Leave>',ScanButtonLeaveFrame)

    #--------------------Scan Button End------------------#

    #--------------------Health Button -------------------#

    healthButtonImg = PhotoImage(file="res\\Blue Asset\\White theme\\Buttons\\Non-Hoved\\health.png").subsample(2,2)
    hovHealthButtonImg = PhotoImage(file="res\\Blue Asset\\White theme\\Buttons\\Hoved\\hovHealth.png").subsample(2,2)

    def HealthButtonEnterFrame(event):
        healthButton.config(image=hovHealthButtonImg)

    def HealthButtonLeaveFrame(event):
        healthButton.config(image=healthButtonImg)


    healthButton = Label(winFrame,image=healthButtonImg,bg="white",cursor="hand2")
    healthButton.place(x=30,y=280)

    healthButton.bind('<Enter>',HealthButtonEnterFrame)
    healthButton.bind('<Leave>',HealthButtonLeaveFrame)

    #--------------------Health Button End ---------------#



    #--------------------Accounts Button -----------------#

    accountsButtonImg = PhotoImage(file="res\\Blue Asset\\White theme\\Buttons\\Non-Hoved\\accounts.png").subsample(2,2)
    hovAccountsButtonImg = PhotoImage(file="res\\Blue Asset\\White theme\\Buttons\\Hoved\\hovAccounts.png").subsample(2,2)

    def AccountsButtonEnterFrame(event):
        accountsButton.config(image=hovAccountsButtonImg)

    def AccountsButtonLeaveFrame(event):
        accountsButton.config(image=accountsButtonImg)


    accountsButton = Label(winFrame,image=accountsButtonImg,bg="white",cursor="hand2")
    accountsButton.place(x=30,y=320)

    accountsButton.bind('<Enter>',AccountsButtonEnterFrame)
    accountsButton.bind('<Leave>',AccountsButtonLeaveFrame)

    #--------------------Accounts Button End -------------#

    #--------------------Internet Button -----------------#

    internetButtonImg = PhotoImage(file="res\\Blue Asset\\White theme\\Buttons\\Non-Hoved\\internet.png").subsample(2,2)
    hovInternetButtonImg = PhotoImage(file="res\\Blue Asset\\White theme\\Buttons\\Hoved\\hovInternet.png").subsample(2,2)

    def InternetButtonEnterFrame(event):
        internetButton.config(image=hovInternetButtonImg)

    def InternetButtonLeaveFrame(event):
        internetButton.config(image=internetButtonImg)


    internetButton = Label(winFrame,image=internetButtonImg,bg="white",cursor="hand2")
    internetButton.place(x=30,y=360)

    internetButton.bind('<Enter>',InternetButtonEnterFrame)
    internetButton.bind('<Leave>',InternetButtonLeaveFrame)

    #--------------------Internet Button End -------------#

    #----------------Dark Theme Change Button-------------#

    def DarkThemeChangeButtonEnter(event):
        darkThemeChangeButton.config(fg="aqua")
    
    def DarkThemeChangeButtonLeave(event):
        darkThemeChangeButton.config(fg="black")


    darkThemeChangeButton = Label(winFrame,text="Dark Theme v1.0",bg="white",cursor="hand2",
                                    font=( "Poppins",10,"bold"),fg="black")

    darkThemeChangeButton.place(x=1060,y=610)

    darkThemeChangeButton.bind('<Enter>',DarkThemeChangeButtonEnter)
    darkThemeChangeButton.bind('<Leave>',DarkThemeChangeButtonLeave)
    darkThemeChangeButton.bind('<Button-1>',HomeViewDarkTheme)

    #----------------Dark Theme Change Button-------------#


HomeViewWhiteTheme()


window.mainloop()

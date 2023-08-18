from tkinter import *
from tkinter import messagebox
import copy
import matplotlib.pyplot as plt
from tkinter import *
from tkinter.filedialog import *
import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
import tkinter
from tkinter import Label
from tkinter import Tk
from tkinter import Label
import time
import sys
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from PIL import ImageTk, Image
#################################### BACKGROUND OF LOGIN SYSTEM
window = Tk()
canvas = Canvas(window, width = 3000 ,height = 169900)
image = ImageTk.PhotoImage(Image.open("C:\\Users\\Syed Hussain\\Desktop\\New folder (2)\\hh.jpg"))

canvas.create_image(0,0,anchor = NW, image = image)
canvas.pack()

window.resizable(False,False)
window.geometry("800x500+300+100")
window.title("Login")
################### condition to proceed further
same=""

#################### FORGET SYSTEMS
def openNewWindow_Freshman():
    def check():
        code = "9876"
        password = "ad+1000"
        verify = code1.get()
        if (verify == code):
            label1 = Label(newWindow, text = " Your password is: "+password+"       " ,fg = "black", font = ("new times roman", 17, "bold"))
            label1.place(x = 240, y = 300) 
            
        else:
            label1 = Label(newWindow, text = " Verification code is incorrect! ", fg = "black", font = ("new times roman", 17, "bold"))
            label1.place(x = 240, y = 300)

#-------------------------------------------------------------------------------------------------------------------------------------            
            
    newWindow = Toplevel(window)
    newWindow.resizable(False,False)
    newWindow.geometry("800x500+300+100")
    
    label1 = Label(newWindow, text = " If you want to retrieve the Password then write your verification code here! ", fg = "black", font = ("new times roman", 16, "italic"))
    label1.place(x = 0, y = 15)
        
    label1 = Label(newWindow, text = " Verification Code ", fg = "black", bg = "yellow" , font = ("times new roman", 20, "bold"))
    label1.place(x = 300, y = 110)
    
    button2 = Button(newWindow, text = "   Check   ", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = check)
    button2.place(x = 350, y = 210)   
        
    code1 = StringVar()
    textBox2 = Entry(newWindow, textvar = code1, width = 15, font = ("arial", 20, "bold"))
    textBox2.place(x = 300, y = 160)
    
#----------------------------------------------------------------------------------------------------------------------------------
###################### LOGIN SYSTEM
def login():
    global same
    users = {'admin': 'ad+1000'}
    username = userName.get()
    Pass = password.get()
    if username in users :
        if (users[username] == Pass):
            label4 = Label(window, text = ("Welcome " + username),width = 25, font = ("arial", 40, "bold"))
            label4.place(x = 0, y = 400)
            same="TRUE"
                                        
        else:
            label4 = Label(window, text = ("Incorrect Password for " + username),width = 25, font = ("arial", 40, "bold"))
            label4.place(x = 0, y = 400)
            same="FALSE"

    else:
        label4 = Label(window, text = (username + " does not exist"),width = 25, font = ("arial", 40, "bold"))
        label4.place(x = 0, y = 400)
        same="FALSE"

#----------------------------------------------------------------------------------------------------------------

label1 = Label(window, text = " Login System ", fg = "black", font = ("new times roman", 40, "bold"))
label1.place(x = 200, y = 15)

label2 = Label(window, text = "User Name :", font = ("arial", 16, "bold"))
label2.place(x = 110, y = 150)

userName = StringVar()
textBox1 = Entry(window, textvar = userName, width = 30, font = ("arial", 16, "bold"))
textBox1.place(x = 290, y = 150)

label3 = Label(window, text = "Password :", font = ("arial", 16, "bold"))
label3.place(x = 116, y = 250)

password = StringVar()
textBox2 = Entry(window, textvar = password, width = 30, font = ("arial", 16, "bold"))
textBox2.place(x = 290, y = 250)

button1 = Button(window, text = "   Login   ", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = login)
button1.place(x = 230, y = 340)

button1 = Button(window, text = "   Forgot Password?   ", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = openNewWindow_Freshman)
button1.place(x = 360, y = 340)
         
#display window
window.mainloop()
############################################## SRMS TABS WINDOW
if same=="TRUE":
    ################################################################################################
    ############################ MERGE SORT #############################################
    def MergeSort(lst):
        if len(lst) > 1:
            mid = len(lst)//2
            part1 = lst[:mid]
            part2 = lst[mid:]
            MergeSort(part1)
            MergeSort(part2)
            i,j=0,0
            while i < len(part1) and j < len(part2):
                if int(part1[i][2])<int(part2[j][2]):
                    lst[i+j] = part1[i]
                    i += 1
                else:
                    lst[i+j] = part2[j]
                    j += 1
            while i < len(part1):
                lst[i+j] = part1[i]
                i += 1
            while j < len(part2):
                lst[i+j]=part2[j]
                j += 1
    ################## BINARY SEARCH ##############################
    def binary_search_iterative(lst, item,way):
        i=0
        j=len(lst)-1
        pt=0
        pos=0
        while i<=j and pt==0:
            mid=(i+j)//2
            if int(lst[mid][2])==int(item):
                pt=1
                pos=mid+1
            elif int(lst[mid][2])>int(item):
                j=(mid-1)
            elif int(lst[mid][2])<int(item):
                i=(mid+1)
        if pt==1 and way==False:
            return lst[pos-1]
        elif pt==1 and way==True:
            return pos-1
        else:
            return -1
    ###########################################  DATA FILE  FOR READ WRITE  ##############################################
    filename1='file2.txt'
    def readFile1(filename1):
        f=open(filename1).read()
        d={}
        count=0
        word=""
        for x in f:
            if x==".":
                word=""
                count=0
            elif x!=",":
                word+=x
            elif x=="," and count==0:
                name=word
                d[name]=[]
                count+=1
                word=""
            elif x=="," and  count==1:
                d[name].append(word)
                word=""
        return d
    (readFile1(filename1))
    linelist=(readFile1(filename1))
    ################ MAKING DICT WITH RESPECT TO YEARS ################
    sophomore={}
    freshman={}
    senior={}
    for k,v in linelist.items():
        if "sophomore" in v:
            sophomore[k]=v
        if "senior" in v:
            senior[k]=v
        if "freshman" in v:
            freshman[k]=v
    ################## MAKING LIST OF ALL STUDENTS #######################
    All_students=[]
    for x in freshman:
        l=[]
        l.append(x)
        collect=freshman.get(x)
        for x in collect:
            l.append(x)
        All_students.append(l)
    for x in sophomore:
        l=[]
        l.append(x)
        collect=sophomore.get(x)
        for x in collect:
            l.append(x)
        All_students.append(l)
    for x in senior:
        l=[]
        l.append(x)
        collect=senior.get(x)
        for x in collect:
            l.append(x)
        All_students.append(l)
    #########################  UPDATE THE DATA IN FILE #################
    def update_data(All_students):
        text=All_students
        save=open('file2.txt',"w") 
        for x in text:
            for y in range(len(x)):
                a=x[y]
                save.write(a+",")
            save.write(".")
        save.close()
        return 
    ############################ GENERATE GRADE LIST OR FILE ####################3
    filename='f1.txt'
    def readFile(filename):
        f=open(filename).read()
        l=[]
        word=""
        li=[]
        for x in f:
            if x==".":
                sa=copy.copy(li)
                l.append(sa)
                li=[]
            elif x!=",":
                word+=x
            elif x==",":
                li.append(word)
                word=""
        return l
    (readFile(filename))
    linelist1=(readFile(filename))
    ########################### MAKING LISTS OF COURSES ##########
    Pfun_course=[]
    DSA_course=[]
    Cal1_course=[]
    Cal2_course=[]
    IECE_course=[]
    ECA_course=[]
    for x in linelist1:
        if "DSA" in x :
            DSA_course.append(x)
        elif  "PFun" in x :
            Pfun_course.append(x)
        elif  "CAL-I" in x:
            Cal1_course.append(x)
        elif  "CAL-II" in x:
            Cal2_course.append(x)
        elif "IECE" in x:
            IECE_course.append(x)
        elif "ECA" in x:
            ECA_course.append(x)
    #####################    UPDATE THE LIST OF COURSES #############
    def coursesupdate(linelist1):
        for x in linelist1:
            if "DSA" in x :
                cp=0
                for y in DSA_course:
                    if x[2]  in y:
                        cp=1
                        break
                if cp==0:
                    DSA_course.append(x)
                    
            elif  "PFun" in x :
                cp=0
                for y in Pfun_course:
                    if x[2]  in y:
                        cp=1
                        break
                if cp==0:
                    Pfun_course.append(x)
            elif  "CAL-I" in x:
                cp=0
                for y in Cal1_course:
                    if x[2]  in y:
                        cp=1
                        break
                if cp==0:
                    Cal1_course.append(x)
            elif  "CAL-II" in x:
                cp=0
                for y in Cal2_course:
                    if x[2]  in y:
                        cp=1
                        break
                if cp==0:
                    Cal2_course.append(x)
            elif "IECE" in x:
                cp=0
                for y in IECE_course:
                    if x[2]  in y:
                        cp=1
                        break
                if cp==0:
                    IECE_course.append(x)
            elif "ECA" in x:
                cp=0
                for y in ECA_course:
                    if x[2]  in y:
                        cp=1
                        break
                if cp==0:
                    ECA_course.append(x)
        return
    ### file update process
    #### update or save list
    def update_data2(linelist1):
        text=linelist1
        save=open('f1.txt',"w") 
        for x in text:
            for y in range(len(x)):
                a=x[y]
                save.write(str(a)+",")
            save.write(".")
        save.close()
        readFile('f1.txt')
        coursesupdate(linelist1)
        return 
    ##############################################################################################################################
    ##############################################################################################################################

    master = Tk()
    master.title("STUDENT RECORDE MANAGEMENT SYSTEM")
    ## window colour background
    master.geometry('100x6688')  
    ################### BACKGROUND WALLPAPER
    canvas = Canvas(master)
    canvas = Canvas(master, width = 24090 ,height = 24000)
    image = ImageTk.PhotoImage(Image.open("C:\\Users\\Syed Hussain\\Desktop\\New folder (2)\\cc5.png"))

    canvas.create_image(0,0,anchor = NW, image = image)
    canvas.pack()
    ################## TIME CODE 
    def get_time():
        master.geometry('4000x2400')   
        timeVar = time.strftime("%I:%M:%S %p")
        clock.config(text=timeVar)
        clock.place(x=1150,y=10)
        clock.after(200,get_time)
    
    Upper_right = Label(master,text ='Time',font=("Arial",20),bg="red",fg="black")
    Upper_right.place(x= 1150, y = 10, anchor ='ne')
    clock = Label(master, font=("Arial",20),bg="red",fg="black")
    clock.pack()
    ################################ QUICKKK SEARCH   ##################
    def login():
        global All_students
        id=stdname.get()
        result=binary_search_iterative(All_students, id,False)
        print(All_students)
        print(id,result)
        if int(id)>0 and result!=-1:
            label_11 = Label(master, text=("Name : "+ result[0].capitalize()+"    "),font=('Helvetica 18 underline italic'),bg="black",fg="white")
            label_11.place(x=950,y=340)
            label_11 = Label(master, text=("Father Name : "+ result[1].capitalize()+"  "),font=('Helvetica 18 underline italic'),bg="black",fg="white")
            label_11.place(x=950,y=370)
            label_11 = Label(master, text=("Student ID : "+ result[2].capitalize()+"  "),font=('Helvetica 18 underline italic'),bg="black",fg="white")
            label_11.place(x=950,y=400)
            label_11 = Label(master, text=("Major  : "+ result[3].upper()+"  "),font=('Helvetica 18 underline italic'),bg="black",fg="white")
            label_11.place(x=950,y=430)
            label_11 = Label(master, text=("Year  : "+ result[4].upper()+"  "),font=('Helvetica 18 underline italic'),bg="black",fg="white")
            label_11.place(x=950,y=460)
            label_11 = Label(master, text=("Course  : "+ result[5].upper()+"  "),font=('Helvetica 18 underline italic'),bg="black",fg="white")
            label_11.place(x=950,y=490)
            label_11 = Label(master, text=("Phone Number  : "+ result[6].capitalize()+"  "),font=('Helvetica 18 underline italic'),bg="black",fg="white")
            label_11.place(x=950,y=520)
            label_11 = Label(master, text=("Address  : "+ result[7].capitalize()+"  "),font=('Helvetica 13 underline italic'),bg="black",fg="white")
            label_11.place(x=950,y=550)

        elif int(id)==0 :
            label_11 = Label(master, text=("                           "),font=('Helvetica 200 underline'),bg="white",fg="white")
            label_11.place(x=950,y=340)
        else:
            label_11 = Label(master, text=("RECORDE NOT FOUND !! "),font=('Helvetica 18 underline italic'),bg="black",fg="white")
            label_11.place(x=950,y=440)




    HEADING = Label(master,text ='QUICK SEARCH', font= ('Helvetica 19 underline italic'),bg="blue",fg="white")
    HEADING.place(x= 1200, y = 200, anchor ='ne')
    label_1 = Label(master, text="STUDENT ID:",font=('Helvetica 16 underline'),bg="black",fg="white")
    label_1.place(x=900,y=250)
    stdname=IntVar()
    entry_1 = Entry(master,textvar=stdname,font=("arial", 16, "bold"),width=15)
    entry_1.place(x=1050,y=250)
    button1 = Button(master, text = "SEARCH ", fg = "black", bg = "white", relief = "raised", font = ("arial", 12, "bold"), command = login)
    button1.place(x = 1120, y = 300)

    ######################## UPADTE STUDeNTS RECORDE  ############################3
    def student_update():
        window = Toplevel(master)
        window.geometry('500x600')
        window.title("REGISTRATION FORM")
        def login():
            global linelist1
            global freshman
            global All_students
            global sophomore
            global senior
            name = stdname.get()
            fname = fathername.get()
            addres=address.get()
            years=year.get()
            ph=phone.get()
            stid=stdID.get()
            Major=major.get()
            cours=course.get()
            if years == "freshman" :
                if name not in freshman.keys():
                    freshman[name]=[]
                    freshman[name].append(fname)
                    freshman[name].append(stid)
                    freshman[name].append(years)
                    freshman[name].append(Major)
                    freshman[name].append(cours)
                    freshman[name].append(ph)
                    freshman[name].append(addres)
                    label4 = Label(window, text = ("SUCCESS FULLY"), font = ("arial", 15))
                    label4.place(x = 300, y = 520)
                    All_students.append([name,fname,stid,years,Major,cours,ph,addres])
                    for x in All_students:
                        if name in x:
                            linelist1.append([x[0],x[3],x[2],x[4],x[5],"0/0","0/0","0/0"])
                    MergeSort(All_students)
                    update_data(All_students)
                    update_data2(linelist1)
                    print(All_students)


                else:
                    label4 = Label(window, text = ("Already EXIST!!!  "), font = ("arial", 15))
                    label4.place(x = 300, y = 520)
            if years == "sophomore" :
                if name not in sophomore.keys():
                    sophomore[name]=[]
                    sophomore[name].append(fname)
                    sophomore[name].append(stid)
                    sophomore[name].append(years)
                    sophomore[name].append(Major)
                    sophomore[name].append(cours)
                    sophomore[name].append(ph)
                    sophomore[name].append(addres)
                    label4 = Label(window, text = ("SUCCESS FULLY"), font = ("arial", 15))
                    label4.place(x = 300, y = 520)
                    All_students.append([name,fname,stid,years,Major,cours,ph,addres])
                    for x in All_students:
                        if name in x:
                            linelist1.append([x[0],x[3],x[2],x[4],x[5],"0/0","0/0","0/0"])
                    update_data2(linelist1)
                    MergeSort(All_students)
                    update_data(All_students)

                else:
                    label4 = Label(window, text = ("Already EXIST!!!  "), font = ("arial", 15))
                    label4.place(x = 300, y = 520)
            if years == "senior" :
                if name not in senior.keys():
                    senior[name]=[]
                    senior[name].append(fname)
                    senior[name].append(stid)
                    senior[name].append(years)
                    senior[name].append(Major)
                    senior[name].append(cours)
                    senior[name].append(ph)
                    senior[name].append(addres)
                    label4 = Label(window, text = ("SUCCESS FULLY"), font = ("arial", 15))
                    label4.place(x = 300, y = 520)
                    All_students.append([name,fname,stid,years,Major,cours,ph,addres])
                    for x in All_students:
                        if name in x:
                            linelist1.append([x[0],x[3],x[2],x[4],x[5],"0/0","0/0","0/0"])
                    update_data2(linelist1)
                    MergeSort(All_students)
                    update_data(All_students)

                else:
                    label4 = Label(window, text = ("Already EXIST!!!  "), font = ("arial", 15))
                    label4.place(x = 300, y = 520)
                    

    #----------------------------------------------------------------------------------------------------------------
    #first lable
        label_0 = Label(window, text="REGISTRATION  FORM",width=20,font=("times new roman", 25))
        label_0.place(x=90,y=53)

        label_1 = Label(window, text="Name:",width=20,font=("times new roman", 12))
        label_1.place(x=80,y=130)
        stdname=StringVar()
        entry_1 = Entry(window,textvar=stdname,width=30)
        entry_1.place(x=240,y=130)

        label_2 = Label(window, text="Father's name:",width=20,font=("times new roman", 12))
        label_2.place(x=68,y=180)
        fathername=StringVar()
        entry_2 = Entry(window,textvar=fathername,width=30)
        entry_2.place(x=240,y=180)
        
        label_3 = Label(window, text="Student ID:",width=20,font=("times new roman", 12))
        label_3.place(x=70,y=230)
        stdID=StringVar()
        entry_2 = Entry(window,textvar=stdID,width=30)
        entry_2.place(x=240,y=230)

        label_4 = Label(window, text="Major:",width=20,font=("times new roman", 12))
        label_4.place(x=70,y=280)
        major=StringVar()
        entry_2 = Entry(window,textvar=major,width=30)
        entry_2.place(x=240,y=280)

        label_5 = Label(window, text="Course:",width=20,font=("times new roman", 12))
        label_5.place(x=70,y=330)
        course=StringVar()
        entry_2 = Entry(window,textvar=course)
        entry_2.place(x=240,y=330)

        label_5 = Label(window, text = "Phone No:", width =20, font=("times new roman", 12))
        label_5.place(x=70,y=380)
        phone=StringVar()
        entry_2 = Entry(window,textvar=phone)
        entry_2.place(x=240,y=380)

        label_5 = Label(window, text = "Address:", width =20, font=("times new roman", 12))
        label_5.place(x=70,y=430)
        address=StringVar()
        entry_2 = Entry(window,textvar=address,width=30)
        entry_2.place(x=240,y=430)
    
        label_6 = Label(window, text = "YEAR:", width =20, font=("times new roman", 12))
        label_6.place(x=70,y=480)
        year=StringVar()
        entry_2 = Entry(window,textvar=year,width=30)
        entry_2.place(x=240,y=480)

        button1 = Button(window, text = "   SUBMIT   ", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = login)
        button1.place(x = 100, y = 525)
        window.resizable(False,False)
        Label(window).pack()
    HEADING = Label(master,text ='UPDATE STUDENT', font= ('Helvetica 17 underline italic'),bg="blue",fg="white")
    HEADING.place(x= 1210, y = 70, anchor ='ne')
    button1=tkinter.Button(master,text="CLICK",font=("Arial",16,"bold"),bg='white',fg='black',width=18,
                            height=2,command=student_update)
    button1.place(x=1000, y=120)
    ###############################################################################################
    ################################################################################################
    ##$################### HEADING OF SRMS
    HEADING = Label(master,text ='STUDENT RECORD MANAGEMENT SYSTEM', font= ('Helvetica 25 underline'),bg="black",fg="white")
    HEADING.place(x= 1000, y = 10, anchor ='ne')
    ####################################################################################################
    def openNewWindow_Freshman1():
        global DSA_course
        # Toplevel object which will 
        # be treated as a new window
        newWindow = Toplevel(master)
        newWindow.title("MANAGEMENT")
        newWindow.geometry("2000x2000")
        def std():
            global DSA_course
            label_1 = Label(newWindow, text="STUDENTS",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=400,y=20)
            label_1 = Label(newWindow, text="YEAR",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=800,y=20)
            label_1 = Label(newWindow, text="MAJOR",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=1000,y=20)
            label_1 = Label(newWindow, text="ID",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=1200,y=20)
            a=70
            num=1
            for k in DSA_course:
                label_1 = Label(newWindow, text=str(num)+"   "+k[0],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=400,y=a)
                label_1 = Label(newWindow, text=k[1],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=800,y=a)
                label_1 = Label(newWindow, text=k[3],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=1000,y=a)
                label_1 = Label(newWindow, text=k[2],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=1200,y=a)
                a+=50
                num+=1
                
        label_1 = Label(newWindow, text="List of Students:",width=0,font=("times new roman", 20))
        label_1.place(x=0,y=0)

        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black',command=std).place(x=0,y = 40)
        #########################################
        ################    Grade List:
        def GL():
            global DSA_course
            label_1 = Label(newWindow, text="STUDENTS",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=350,y=20)
            label_1 = Label(newWindow, text="TEST#1",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=700,y=20)
            label_1 = Label(newWindow, text="TEST#2",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=850,y=20)
            label_1 = Label(newWindow, text="TEST#3",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=1000,y=20)
            label_1 = Label(newWindow, text="PERCENTAGE",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=1150,y=20)
            a=70
            num=1
            for k in DSA_course:
                label_1 = Label(newWindow, text=str(num)+"   "+k[0],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=350,y=a)
                g1=k[5].split('/')
                g2=k[6].split('/')
                g3=k[7].split('/')
                label_1 = Label(newWindow, text=k[4+1],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=700,y=a)
                label_1 = Label(newWindow, text=k[5+1],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=850,y=a)
                label_1 = Label(newWindow, text=k[6+1],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=1000,y=a)
                per=0
                if (int(g1[0])!=0 or int(g2[0])!=0 or int(g3[0])!=0) and (int(g1[1])!=0 or int(g2[1])!=0 or int(g3[1])!=0):
                    per=((int(g1[0])+int(g2[0])+int(g3[0]))/(int(g1[1])+int(g2[1])+int(g3[1])))*100
                    per=round(per,1)
                label_1 = Label(newWindow, text=str(per)+"%",width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=1150,y=a)
                a+=50
                num+=1
        label_2 = Label(newWindow, text="Grade List:",width=0,font=("times new roman", 20))
        label_2.place(x=1,y=150)
        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black',command=GL).place(x=0,y = 190)
    ########################v Upgrade grade:

        def openNewWindow_Freshman1():

            # Toplevel object which will 
            # be treated as a new window
            newWindow2 = Toplevel(newWindow)
            def upgrad():
                MergeSort(DSA_course)
                ID=id.get()
                result=binary_search_iterative(DSA_course,int(ID),True)
                t1=testt1.get()
                t2=testt2.get()
                t3=testt3.get()
                li=DSA_course[result]
                if len(t1)!=0:
                    li[5],t1=t1,li[5]
                if len(t2)!=0:
                    li[6],t2=t2,li[6]
                if len(t3)!=0:
                    li[7],t3=t3,li[7]
                label_09 = Label(newWindow2, text="GRADES UPDATED ",width=0,font=("times new roman", 20))
                label_09.place(x=600,y=600)   
                update_data2(linelist1)
            # update grade
            label_08 = Label(newWindow2, text="UPDATE GRADE",width=0,font=("times new roman", 40,"bold"))
            label_08.place(x=470,y=10)   
            
            # student name
            label_09 = Label(newWindow2, text="Student ID :",width=0,font=("times new roman", 20))
            label_09.place(x=0,y=150)   
            id=StringVar()
            textBox1 = Entry(newWindow2,textvariable=id, width = 20, font = ("times new roman", 20))
            textBox1.place(x = 180, y = 150)     
            
            # test 1:
            label_05 = Label(newWindow2, text="Test 1:",width=0,font=("times new roman", 20))
            label_05.place(x=0,y=270)   
            testt1=StringVar()
            textBox2 = Entry(newWindow2,textvariable=testt1, width = 7, font = ("times new roman", 20))
            textBox2.place(x = 100, y = 270)
            
            # test 2:
            label_04 = Label(newWindow2, text="Test 2:",width=0,font=("times new roman", 20))
            label_04.place(x=0,y=370)   
            testt2=StringVar()
            textBox3 = Entry(newWindow2,textvariable=testt2, width = 7, font = ("times new roman", 20))
            textBox3.place(x = 100, y = 370)
            
            # test 3:
            label_07 = Label(newWindow2, text="Test 3:",width=0,font=("times new roman", 20))
            label_07.place(x=0,y=470)   
            testt3=StringVar()
            textBox6 = Entry(newWindow2,textvariable=testt3, width = 7, font = ("times new roman", 20))
            textBox6.place(x = 100, y = 470)
            ######## DATA ID ###################
            label_1 = Label(newWindow2, text="STUDENTS",width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
            label_1.place(x=500+200,y=90)
            label_1 = Label(newWindow2, text="ID",width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
            label_1.place(x=850+200,y=90)
            num=1
            a=130
            for k in DSA_course:
                label_1 = Label(newWindow2, text=str(num)+"   "+k[0],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=500+200,y=a)
                label_1 = Label(newWindow2, text=k[2],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=850+200,y=a)
                a+=50
                num+=1
            # update button
            Button(newWindow2, text='Update',width=15, height = 3,font=("times new roman", 15),bg='yellow',fg='black', command = upgrad).place(x=0,y = 570)

            # newWindow = tk.Tk()
            newWindow2.geometry("40000x60000")
            newWindow2.title("Update Grade")
            # newWindow.config(bg = "white")
            top = Frame(newWindow2)
            top.pack(padx = 10, pady = 5, anchor = 'nw')
        label_3 = Label(newWindow, text="Update Grade:",width=0,font=("times new roman", 20))
        label_3.place(x=2,y=300)
        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black', command = openNewWindow_Freshman1).place(x=0,y = 340)

    ################################################# Students Progress
        def graph():
            xaxis=[]
            yaxis=[]
            for k in DSA_course:
                g1=k[5].split('/')
                g2=k[6].split('/')
                g3=k[7].split('/')
                per=0
                if (int(g1[0])!=0 or int(g2[0])!=0 or int(g3[0])!=0) and (int(g1[1])!=0 or int(g2[1])!=0 or int(g3[1])!=0):
                    per=((int(g1[0])+int(g2[0])+int(g3[0]))/(int(g1[1])+int(g2[1])+int(g3[1])))*100
                    per=round(per,1)
                yaxis.append(per)
                xaxis.append(k[0])
            plt.bar(xaxis, yaxis)
            plt.ylabel('STUDENTS PROGRESS')
            plt.show()
                
        label_4 = Label(newWindow, text="Student Progress:",width=0,font=("times new roman", 20))
        label_4.place(x=3,y=450)

        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black',command=graph).place(x=0,y = 490)

        #################################### Notepad Calling:

        def openNewWindow_Freshman():

            # Toplevel object which will 
            # be treated as a new window
            newWindow1 = Toplevel(newWindow)
            
            def saveFile():
                new_file = asksaveasfile(mode = 'w', filetype = [('text files', '.txt')])
                if new_file is None:
                    return
                text = str(entry.get(1.0, END))
                new_file.write(text)
                new_file.close()

            def openFile():
                file = askopenfile(mode = 'r', filetype = [('text files', '*.txt')])
                if file is not None:
                    content = file.read()
                entry.insert(INSERT, content)

            def clearFile():
                entry.delete(1.0, END)

            # newWindow = tk.Tk()
            newWindow1.geometry("400x600")
            newWindow1.title("Notepad")
            # newWindow.config(bg = "white")
            top = Frame(newWindow1)
            top.pack(padx = 10, pady = 5, anchor = 'nw')

            b1 = Button(newWindow1, text="Open", bg = "white", command = openFile)
            b1.pack(in_ = top, side=LEFT)

            b2 = Button(newWindow1, text="Save", bg = "white", command = saveFile)
            b2.pack(in_ = top, side=LEFT)

            b3 = Button(newWindow1, text="Clear", bg = "white", command = clearFile)
            b3.pack(in_ = top, side=LEFT)

            b4 = Button(newWindow1, text="Exit", bg = "white", command = exit)
            b4.pack(in_ = top, side=LEFT)

            entry = Text(newWindow1, wrap = WORD, bg = "#F9DDA4", font = ("poppins", 15))
            entry.pack(padx = 10, pady = 5, expand = TRUE, fill = BOTH)

            # A Label widget to show in toplevel
            Label(newWindow1).pack()
        # Announcement Pad:
        label_5 = Label(newWindow, text="Announcement PAD:",width=0,font=("times new roman", 20))
        label_5.place(x=4,y=590)

        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black', command = openNewWindow_Freshman).place(x=0,y = 640)
        #################################### CLEAR  FUNCTION
        def clear():
            label_5 = Label(newWindow, text="                                     ",width=789,font=("times new roman", 400),bg='white',fg='black')
            label_5.place(x=320,y=0)
        Button(newWindow, text=' CLEAR ',width=15, height = 3,font=("times new roman", 15),bg='yellow',fg='black', command = clear).place(x=1200,y = 620)
        label_5 = Label(newWindow, text="                                     ",width=789,font=("times new roman", 400),bg='white',fg='black')
        label_5.place(x=320,y=0)
        # A Label widget to show in toplevel
        Label(newWindow).pack()
    #############################################
    ############3  freshman HEADING
    HEADING =Label(master,text ='FRESHMAN',font= ('Helvetica 18 underline'),bg="black",fg="white")
    HEADING.place(x=140, y = 30, anchor ='ne')
    im = PhotoImage(file='c6.png')
    im = im.subsample(2,2)
    button1=tkinter.Button(master,width=200,image=im,
                            height=180,command=openNewWindow_Freshman1,compound=CENTER)
    button1.place(x=0, y=70)
    ###################################################################
    ##################################################################
    #################################################################
    def openNewWindow_Sophomore():
        
        # Toplevel object which will 
        # be treated as a new window
        global IECE_course
        # Toplevel object which will 
        # be treated as a new window
        newWindow = Toplevel(master)
        newWindow.title("MANAGEMENT")
        newWindow.geometry("2000x2000")
        def std():
            global IECE_course
            label_1 = Label(newWindow, text="STUDENTS",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=400,y=20)
            label_1 = Label(newWindow, text="YEAR",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=800,y=20)
            label_1 = Label(newWindow, text="MAJOR",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=1000,y=20)
            label_1 = Label(newWindow, text="ID",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=1200,y=20)
            a=70
            num=1
            for k in IECE_course:
                label_1 = Label(newWindow, text=str(num)+"   "+k[0],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=400,y=a)
                label_1 = Label(newWindow, text=k[1],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=800,y=a)
                label_1 = Label(newWindow, text=k[3],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=1000,y=a)
                label_1 = Label(newWindow, text=k[2],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=1200,y=a)
                a+=50
                num+=1
                
        label_1 = Label(newWindow, text="List of Students:",width=0,font=("times new roman", 20))
        label_1.place(x=0,y=0)

        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black',command=std).place(x=0,y = 40)
        #########################################
        ################    Grade List:
        def GL():
            global IECE_course
            label_1 = Label(newWindow, text="STUDENTS",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=350,y=20)
            label_1 = Label(newWindow, text="TEST#1",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=700,y=20)
            label_1 = Label(newWindow, text="TEST#2",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=850,y=20)
            label_1 = Label(newWindow, text="TEST#3",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=1000,y=20)
            label_1 = Label(newWindow, text="PERCENTAGE",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=1150,y=20)
            a=70
            num=1
            for k in IECE_course:
                label_1 = Label(newWindow, text=str(num)+"   "+k[0],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=350,y=a)
                g1=k[5].split('/')
                g2=k[6].split('/')
                g3=k[7].split('/')
                label_1 = Label(newWindow, text=k[4+1],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=700,y=a)
                label_1 = Label(newWindow, text=k[5+1],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=850,y=a)
                label_1 = Label(newWindow, text=k[6+1],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=1000,y=a)
                per=0
                if (int(g1[0])!=0 or int(g2[0])!=0 or int(g3[0])!=0) and (int(g1[1])!=0 or int(g2[1])!=0 or int(g3[1])!=0):
                    per=((int(g1[0])+int(g2[0])+int(g3[0]))/(int(g1[1])+int(g2[1])+int(g3[1])))*100
                    per=round(per,1)
                label_1 = Label(newWindow, text=str(per)+"%",width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=1150,y=a)
                a+=50
                num+=1
        label_2 = Label(newWindow, text="Grade List:",width=0,font=("times new roman", 20))
        label_2.place(x=1,y=150)
        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black',command=GL).place(x=0,y = 190)
    ########################v Upgrade grade:

        def openNewWindow_Freshman1():

            # Toplevel object which will 
            # be treated as a new window
            newWindow2 = Toplevel(newWindow)
            def upgrad():
                MergeSort(IECE_course)
                ID=id.get()
                result=binary_search_iterative(IECE_course,int(ID),True)
                t1=testt1.get()
                t2=testt2.get()
                t3=testt3.get()
                li=IECE_course[result]
                if len(t1)!=0:
                    li[5],t1=t1,li[5]
                if len(t2)!=0:
                    li[6],t2=t2,li[6]
                if len(t3)!=0:
                    li[7],t3=t3,li[7]
                label_09 = Label(newWindow2, text="GRADES UPDATED ",width=0,font=("times new roman", 20))
                label_09.place(x=600,y=600)   
                update_data2(linelist1)
            # update grade
            label_08 = Label(newWindow2, text="UPDATE GRADE",width=0,font=("times new roman", 40,"bold"))
            label_08.place(x=470,y=10)   
            
            # student name
            label_09 = Label(newWindow2, text="Student ID :",width=0,font=("times new roman", 20))
            label_09.place(x=0,y=150)   
            id=StringVar()
            textBox1 = Entry(newWindow2,textvariable=id, width = 20, font = ("times new roman", 20))
            textBox1.place(x = 180, y = 150)     
            
            # test 1:
            label_05 = Label(newWindow2, text="Test 1:",width=0,font=("times new roman", 20))
            label_05.place(x=0,y=270)   
            testt1=StringVar()
            textBox2 = Entry(newWindow2,textvariable=testt1, width = 7, font = ("times new roman", 20))
            textBox2.place(x = 100, y = 270)
            
            # test 2:
            label_04 = Label(newWindow2, text="Test 2:",width=0,font=("times new roman", 20))
            label_04.place(x=0,y=370)   
            testt2=StringVar()
            textBox3 = Entry(newWindow2,textvariable=testt2, width = 7, font = ("times new roman", 20))
            textBox3.place(x = 100, y = 370)
            
            # test 3:
            label_07 = Label(newWindow2, text="Test 3:",width=0,font=("times new roman", 20))
            label_07.place(x=0,y=470)   
            testt3=StringVar()
            textBox6 = Entry(newWindow2,textvariable=testt3, width = 7, font = ("times new roman", 20))
            textBox6.place(x = 100, y = 470)
            ######## DATA ID ###################
            label_1 = Label(newWindow2, text="STUDENTS",width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
            label_1.place(x=500+200,y=90)
            label_1 = Label(newWindow2, text="ID",width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
            label_1.place(x=850+200,y=90)
            num=1
            a=130
            for k in IECE_course:
                label_1 = Label(newWindow2, text=str(num)+"   "+k[0],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=500+200,y=a)
                label_1 = Label(newWindow2, text=k[2],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=850+200,y=a)
                a+=50
                num+=1
            # update button
            Button(newWindow2, text='Update',width=15, height = 3,font=("times new roman", 15),bg='yellow',fg='black', command = upgrad).place(x=0,y = 570)

            # newWindow = tk.Tk()
            newWindow2.geometry("40000x60000")
            newWindow2.title("Update Grade")
            # newWindow.config(bg = "white")
            top = Frame(newWindow2)
            top.pack(padx = 10, pady = 5, anchor = 'nw')
        label_3 = Label(newWindow, text="Update Grade:",width=0,font=("times new roman", 20))
        label_3.place(x=2,y=300)
        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black', command = openNewWindow_Freshman1).place(x=0,y = 340)

    ################################################# Students Progress
        def graph():
            xaxis=[]
            yaxis=[]
            for k in IECE_course:
                g1=k[5].split('/')
                g2=k[6].split('/')
                g3=k[7].split('/')
                per=0
                if (int(g1[0])!=0 or int(g2[0])!=0 or int(g3[0])!=0) and (int(g1[1])!=0 or int(g2[1])!=0 or int(g3[1])!=0):
                    per=((int(g1[0])+int(g2[0])+int(g3[0]))/(int(g1[1])+int(g2[1])+int(g3[1])))*100
                    per=round(per,1)
                yaxis.append(per)
                xaxis.append(k[0])
            plt.bar(xaxis, yaxis)
            plt.ylabel('STUDENTS PROGRESS')
            plt.show()
                
        label_4 = Label(newWindow, text="Student Progress:",width=0,font=("times new roman", 20))
        label_4.place(x=3,y=450)

        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black',command=graph).place(x=0,y = 490)

        #################################### Notepad Calling:

        def openNewWindow_Freshman():

            # Toplevel object which will 
            # be treated as a new window
            newWindow1 = Toplevel(newWindow)
            
            def saveFile():
                new_file = asksaveasfile(mode = 'w', filetype = [('text files', '.txt')])
                if new_file is None:
                    return
                text = str(entry.get(1.0, END))
                new_file.write(text)
                new_file.close()

            def openFile():
                file = askopenfile(mode = 'r', filetype = [('text files', '*.txt')])
                if file is not None:
                    content = file.read()
                entry.insert(INSERT, content)

            def clearFile():
                entry.delete(1.0, END)

            # newWindow = tk.Tk()
            newWindow1.geometry("400x600")
            newWindow1.title("Notepad")
            # newWindow.config(bg = "white")
            top = Frame(newWindow1)
            top.pack(padx = 10, pady = 5, anchor = 'nw')

            b1 = Button(newWindow1, text="Open", bg = "white", command = openFile)
            b1.pack(in_ = top, side=LEFT)

            b2 = Button(newWindow1, text="Save", bg = "white", command = saveFile)
            b2.pack(in_ = top, side=LEFT)

            b3 = Button(newWindow1, text="Clear", bg = "white", command = clearFile)
            b3.pack(in_ = top, side=LEFT)

            b4 = Button(newWindow1, text="Exit", bg = "white", command = exit)
            b4.pack(in_ = top, side=LEFT)

            entry = Text(newWindow1, wrap = WORD, bg = "#F9DDA4", font = ("poppins", 15))
            entry.pack(padx = 10, pady = 5, expand = TRUE, fill = BOTH)

            # A Label widget to show in toplevel
            Label(newWindow1).pack()
        # Announcement Pad:
        label_5 = Label(newWindow, text="Announcement PAD:",width=0,font=("times new roman", 20))
        label_5.place(x=4,y=590)

        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black', command = openNewWindow_Freshman).place(x=0,y = 640)
        #################################### CLEAR  FUNCTION
        def clear():
            label_5 = Label(newWindow, text="                                     ",width=789,font=("times new roman", 400),bg='white',fg='black')
            label_5.place(x=320,y=0)
        Button(newWindow, text=' CLEAR ',width=15, height = 3,font=("times new roman", 15),bg='yellow',fg='black', command = clear).place(x=1200,y = 620)
        label_5 = Label(newWindow, text="                                     ",width=789,font=("times new roman", 400),bg='white',fg='black')
        label_5.place(x=320,y=0)
        # A Label widget to show in toplevel
        Label(newWindow).pack()
    # sphomore
    HEADING =Label(master,text ='SOPHOMORE',font= ('Helvetica 16 underline'),bg="black",fg="white")
    HEADING.place(x=145, y = 255, anchor ='ne')
    im1 = PhotoImage(file='c3.png')
    im1 = im1.subsample(2,2)
    button1=tkinter.Button(master,width=200,
                            height=190,command=openNewWindow_Sophomore,image=im1)
    button1.place(x=0, y=285)
    #################################################################3
    #################################################################
    ################################################################
    def openNewWindow_Senior():
        global Cal1_course
        # Toplevel object which will 
        # be treated as a new window
        newWindow = Toplevel(master)
        newWindow.title("MANAGEMENT")
        newWindow.geometry("2000x2000")
        def std():
            global Cal1_course
            label_1 = Label(newWindow, text="STUDENTS",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=400,y=20)
            label_1 = Label(newWindow, text="YEAR",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=800,y=20)
            label_1 = Label(newWindow, text="MAJOR",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=1000,y=20)
            label_1 = Label(newWindow, text="ID",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=1200,y=20)
            a=70
            num=1
            for k in Cal1_course:
                label_1 = Label(newWindow, text=str(num)+"   "+k[0],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=400,y=a)
                label_1 = Label(newWindow, text=k[1],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=800,y=a)
                label_1 = Label(newWindow, text=k[3],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=1000,y=a)
                label_1 = Label(newWindow, text=k[2],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=1200,y=a)
                a+=50
                num+=1
                
        label_1 = Label(newWindow, text="List of Students:",width=0,font=("times new roman", 20))
        label_1.place(x=0,y=0)

        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black',command=std).place(x=0,y = 40)
        #########################################
        ################    Grade List:
        def GL():
            global Cal1_course
            label_1 = Label(newWindow, text="STUDENTS",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=350,y=20)
            label_1 = Label(newWindow, text="TEST#1",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=700,y=20)
            label_1 = Label(newWindow, text="TEST#2",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=850,y=20)
            label_1 = Label(newWindow, text="TEST#3",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=1000,y=20)
            label_1 = Label(newWindow, text="PERCENTAGE",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=1150,y=20)
            a=70
            num=1
            for k in Cal1_course:
                label_1 = Label(newWindow, text=str(num)+"   "+k[0],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=350,y=a)
                g1=k[5].split('/')
                g2=k[6].split('/')
                g3=k[7].split('/')
                label_1 = Label(newWindow, text=k[4+1],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=700,y=a)
                label_1 = Label(newWindow, text=k[5+1],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=850,y=a)
                label_1 = Label(newWindow, text=k[6+1],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=1000,y=a)
                per=0
                if (int(g1[0])!=0 or int(g2[0])!=0 or int(g3[0])!=0) and (int(g1[1])!=0 or int(g2[1])!=0 or int(g3[1])!=0):
                    per=((int(g1[0])+int(g2[0])+int(g3[0]))/(int(g1[1])+int(g2[1])+int(g3[1])))*100
                    per=round(per,1)
                label_1 = Label(newWindow, text=str(per)+"%",width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=1150,y=a)
                a+=50
                num+=1
        label_2 = Label(newWindow, text="Grade List:",width=0,font=("times new roman", 20))
        label_2.place(x=1,y=150)
        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black',command=GL).place(x=0,y = 190)
    ########################v Upgrade grade:

        def openNewWindow_Freshman1():

            # Toplevel object which will 
            # be treated as a new window
            newWindow2 = Toplevel(newWindow)
            def upgrad():
                MergeSort(Cal1_course)
                ID=id.get()
                result=binary_search_iterative(Cal1_course,int(ID),True)
                t1=testt1.get()
                t2=testt2.get()
                t3=testt3.get()
                li=Cal1_course[result]
                if len(t1)!=0:
                    li[5],t1=t1,li[5]
                if len(t2)!=0:
                    li[6],t2=t2,li[6]
                if len(t3)!=0:
                    li[7],t3=t3,li[7]
                label_09 = Label(newWindow2, text="GRADES UPDATED ",width=0,font=("times new roman", 20))
                label_09.place(x=600,y=600)   
                update_data2(linelist1)
            # update grade
            label_08 = Label(newWindow2, text="UPDATE GRADE",width=0,font=("times new roman", 40,"bold"))
            label_08.place(x=470,y=10)   
            
            # student name
            label_09 = Label(newWindow2, text="Student ID :",width=0,font=("times new roman", 20))
            label_09.place(x=0,y=150)   
            id=StringVar()
            textBox1 = Entry(newWindow2,textvariable=id, width = 20, font = ("times new roman", 20))
            textBox1.place(x = 180, y = 150)     
            
            # test 1:
            label_05 = Label(newWindow2, text="Test 1:",width=0,font=("times new roman", 20))
            label_05.place(x=0,y=270)   
            testt1=StringVar()
            textBox2 = Entry(newWindow2,textvariable=testt1, width = 7, font = ("times new roman", 20))
            textBox2.place(x = 100, y = 270)
            
            # test 2:
            label_04 = Label(newWindow2, text="Test 2:",width=0,font=("times new roman", 20))
            label_04.place(x=0,y=370)   
            testt2=StringVar()
            textBox3 = Entry(newWindow2,textvariable=testt2, width = 7, font = ("times new roman", 20))
            textBox3.place(x = 100, y = 370)
            
            # test 3:
            label_07 = Label(newWindow2, text="Test 3:",width=0,font=("times new roman", 20))
            label_07.place(x=0,y=470)   
            testt3=StringVar()
            textBox6 = Entry(newWindow2,textvariable=testt3, width = 7, font = ("times new roman", 20))
            textBox6.place(x = 100, y = 470)
            ######## DATA ID ###################
            label_1 = Label(newWindow2, text="STUDENTS",width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
            label_1.place(x=500+200,y=90)
            label_1 = Label(newWindow2, text="ID",width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
            label_1.place(x=850+200,y=90)
            num=1
            a=130
            for k in Cal1_course:
                label_1 = Label(newWindow2, text=str(num)+"   "+k[0],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=500+200,y=a)
                label_1 = Label(newWindow2, text=k[2],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=850+200,y=a)
                a+=50
                num+=1
            # update button
            Button(newWindow2, text='Update',width=15, height = 3,font=("times new roman", 15),bg='yellow',fg='black', command = upgrad).place(x=0,y = 570)

            # newWindow = tk.Tk()
            newWindow2.geometry("40000x60000")
            newWindow2.title("Update Grade")
            # newWindow.config(bg = "white")
            top = Frame(newWindow2)
            top.pack(padx = 10, pady = 5, anchor = 'nw')
        label_3 = Label(newWindow, text="Update Grade:",width=0,font=("times new roman", 20))
        label_3.place(x=2,y=300)
        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black', command = openNewWindow_Freshman1).place(x=0,y = 340)

    ################################################# Students Progress
        def graph():
            xaxis=[]
            yaxis=[]
            for k in Cal1_course:
                g1=k[5].split('/')
                g2=k[6].split('/')
                g3=k[7].split('/')
                per=0
                if (int(g1[0])!=0 or int(g2[0])!=0 or int(g3[0])!=0) and (int(g1[1])!=0 or int(g2[1])!=0 or int(g3[1])!=0):
                    per=((int(g1[0])+int(g2[0])+int(g3[0]))/(int(g1[1])+int(g2[1])+int(g3[1])))*100
                    per=round(per,1)
                yaxis.append(per)
                xaxis.append(k[0])
            plt.bar(xaxis, yaxis)
            plt.ylabel('STUDENTS PROGRESS')
            plt.show()
                
        label_4 = Label(newWindow, text="Student Progress:",width=0,font=("times new roman", 20))
        label_4.place(x=3,y=450)

        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black',command=graph).place(x=0,y = 490)

        #################################### Notepad Calling:

        def openNewWindow_Freshman():

            # Toplevel object which will 
            # be treated as a new window
            newWindow1 = Toplevel(newWindow)
            
            def saveFile():
                new_file = asksaveasfile(mode = 'w', filetype = [('text files', '.txt')])
                if new_file is None:
                    return
                text = str(entry.get(1.0, END))
                new_file.write(text)
                new_file.close()

            def openFile():
                file = askopenfile(mode = 'r', filetype = [('text files', '*.txt')])
                if file is not None:
                    content = file.read()
                entry.insert(INSERT, content)

            def clearFile():
                entry.delete(1.0, END)

            # newWindow = tk.Tk()
            newWindow1.geometry("400x600")
            newWindow1.title("Notepad")
            # newWindow.config(bg = "white")
            top = Frame(newWindow1)
            top.pack(padx = 10, pady = 5, anchor = 'nw')

            b1 = Button(newWindow1, text="Open", bg = "white", command = openFile)
            b1.pack(in_ = top, side=LEFT)

            b2 = Button(newWindow1, text="Save", bg = "white", command = saveFile)
            b2.pack(in_ = top, side=LEFT)

            b3 = Button(newWindow1, text="Clear", bg = "white", command = clearFile)
            b3.pack(in_ = top, side=LEFT)

            b4 = Button(newWindow1, text="Exit", bg = "white", command = exit)
            b4.pack(in_ = top, side=LEFT)

            entry = Text(newWindow1, wrap = WORD, bg = "#F9DDA4", font = ("poppins", 15))
            entry.pack(padx = 10, pady = 5, expand = TRUE, fill = BOTH)

            # A Label widget to show in toplevel
            Label(newWindow1).pack()
        # Announcement Pad:
        label_5 = Label(newWindow, text="Announcement PAD:",width=0,font=("times new roman", 20))
        label_5.place(x=4,y=590)

        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black', command = openNewWindow_Freshman).place(x=0,y = 640)
        #################################### CLEAR  FUNCTION
        def clear():
            label_5 = Label(newWindow, text="                                     ",width=789,font=("times new roman", 400),bg='white',fg='black')
            label_5.place(x=320,y=0)
        Button(newWindow, text=' CLEAR ',width=15, height = 3,font=("times new roman", 15),bg='yellow',fg='black', command = clear).place(x=1200,y = 620)
        label_5 = Label(newWindow, text="                                     ",width=789,font=("times new roman", 400),bg='white',fg='black')
        label_5.place(x=320,y=0)
        # A Label widget to show in toplevel
        Label(newWindow).pack()
    # Seniors
    HEADING =Label(master,text ='SENIORS',font= ('Helvetica 16 underline'),bg="black",fg="white")
    HEADING.place(x=100, y = 480, anchor ='ne')
    im2 = PhotoImage(file='c4.png')
    im2 = im2.subsample(2,2)
    button1=tkinter.Button(master, text="button3",width=200,
                            height=190,command=openNewWindow_Senior,image=im2)
    button1.place(x=0, y=510)
    #################################################################3
    #################################################################
    ################################################################
    def openNewWindow_Senior1():
        global Cal2_course
        # Toplevel object which will 
        # be treated as a new window
        newWindow = Toplevel(master)
        newWindow.title("MANAGEMENT")
        newWindow.geometry("2000x2000")
        def std():
            global Cal2_course
            label_1 = Label(newWindow, text="STUDENTS",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=400,y=20)
            label_1 = Label(newWindow, text="YEAR",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=800,y=20)
            label_1 = Label(newWindow, text="MAJOR",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=1000,y=20)
            label_1 = Label(newWindow, text="ID",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=1200,y=20)
            a=70
            num=1
            for k in Cal2_course:
                label_1 = Label(newWindow, text=str(num)+"   "+k[0],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=400,y=a)
                label_1 = Label(newWindow, text=k[1],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=800,y=a)
                label_1 = Label(newWindow, text=k[3],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=1000,y=a)
                label_1 = Label(newWindow, text=k[2],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=1200,y=a)
                a+=50
                num+=1
                
        label_1 = Label(newWindow, text="List of Students:",width=0,font=("times new roman", 20))
        label_1.place(x=0,y=0)

        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black',command=std).place(x=0,y = 40)
        #########################################
        ################    Grade List:
        def GL():
            global Cal2_course
            label_1 = Label(newWindow, text="STUDENTS",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=350,y=20)
            label_1 = Label(newWindow, text="TEST#1",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=700,y=20)
            label_1 = Label(newWindow, text="TEST#2",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=850,y=20)
            label_1 = Label(newWindow, text="TEST#3",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=1000,y=20)
            label_1 = Label(newWindow, text="PERCENTAGE",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=1150,y=20)
            a=70
            num=1
            for k in Cal2_course:
                label_1 = Label(newWindow, text=str(num)+"   "+k[0],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=350,y=a)
                g1=k[5].split('/')
                g2=k[6].split('/')
                g3=k[7].split('/')
                label_1 = Label(newWindow, text=k[4+1],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=700,y=a)
                label_1 = Label(newWindow, text=k[5+1],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=850,y=a)
                label_1 = Label(newWindow, text=k[6+1],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=1000,y=a)
                per=0
                if (int(g1[0])!=0 or int(g2[0])!=0 or int(g3[0])!=0) and (int(g1[1])!=0 or int(g2[1])!=0 or int(g3[1])!=0):
                    per=((int(g1[0])+int(g2[0])+int(g3[0]))/(int(g1[1])+int(g2[1])+int(g3[1])))*100
                    per=round(per,1)
                label_1 = Label(newWindow, text=str(per)+"%",width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=1150,y=a)
                a+=50
                num+=1
        label_2 = Label(newWindow, text="Grade List:",width=0,font=("times new roman", 20))
        label_2.place(x=1,y=150)
        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black',command=GL).place(x=0,y = 190)
    ########################v Upgrade grade:

        def openNewWindow_Freshman1():

            # Toplevel object which will 
            # be treated as a new window
            newWindow2 = Toplevel(newWindow)
            def upgrad():
                MergeSort(Cal2_course)
                ID=id.get()
                result=binary_search_iterative(Cal2_course,int(ID),True)
                t1=testt1.get()
                t2=testt2.get()
                t3=testt3.get()
                li=Cal2_course[result]
                if len(t1)!=0:
                    li[5],t1=t1,li[5]
                if len(t2)!=0:
                    li[6],t2=t2,li[6]
                if len(t3)!=0:
                    li[7],t3=t3,li[7]
                label_09 = Label(newWindow2, text="GRADES UPDATED ",width=0,font=("times new roman", 20))
                label_09.place(x=600,y=600)   
                update_data2(linelist1)
            # update grade
            label_08 = Label(newWindow2, text="UPDATE GRADE",width=0,font=("times new roman", 40,"bold"))
            label_08.place(x=470,y=10)   
            
            # student name
            label_09 = Label(newWindow2, text="Student ID :",width=0,font=("times new roman", 20))
            label_09.place(x=0,y=150)   
            id=StringVar()
            textBox1 = Entry(newWindow2,textvariable=id, width = 20, font = ("times new roman", 20))
            textBox1.place(x = 180, y = 150)     
            
            # test 1:
            label_05 = Label(newWindow2, text="Test 1:",width=0,font=("times new roman", 20))
            label_05.place(x=0,y=270)   
            testt1=StringVar()
            textBox2 = Entry(newWindow2,textvariable=testt1, width = 7, font = ("times new roman", 20))
            textBox2.place(x = 100, y = 270)
            
            # test 2:
            label_04 = Label(newWindow2, text="Test 2:",width=0,font=("times new roman", 20))
            label_04.place(x=0,y=370)   
            testt2=StringVar()
            textBox3 = Entry(newWindow2,textvariable=testt2, width = 7, font = ("times new roman", 20))
            textBox3.place(x = 100, y = 370)
            
            # test 3:
            label_07 = Label(newWindow2, text="Test 3:",width=0,font=("times new roman", 20))
            label_07.place(x=0,y=470)   
            testt3=StringVar()
            textBox6 = Entry(newWindow2,textvariable=testt3, width = 7, font = ("times new roman", 20))
            textBox6.place(x = 100, y = 470)
            ######## DATA ID ###################
            label_1 = Label(newWindow2, text="STUDENTS",width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
            label_1.place(x=500+200,y=90)
            label_1 = Label(newWindow2, text="ID",width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
            label_1.place(x=850+200,y=90)
            num=1
            a=130
            for k in Cal2_course:
                label_1 = Label(newWindow2, text=str(num)+"   "+k[0],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=500+200,y=a)
                label_1 = Label(newWindow2, text=k[2],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=850+200,y=a)
                a+=50
                num+=1
            # update button
            Button(newWindow2, text='Update',width=15, height = 3,font=("times new roman", 15),bg='yellow',fg='black', command = upgrad).place(x=0,y = 570)

            # newWindow = tk.Tk()
            newWindow2.geometry("40000x60000")
            newWindow2.title("Update Grade")
            # newWindow.config(bg = "white")
            top = Frame(newWindow2)
            top.pack(padx = 10, pady = 5, anchor = 'nw')
        label_3 = Label(newWindow, text="Update Grade:",width=0,font=("times new roman", 20))
        label_3.place(x=2,y=300)
        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black', command = openNewWindow_Freshman1).place(x=0,y = 340)

    ################################################# Students Progress
        def graph():
            xaxis=[]
            yaxis=[]
            for k in Cal2_course:
                g1=k[5].split('/')
                g2=k[6].split('/')
                g3=k[7].split('/')
                per=0
                if (int(g1[0])!=0 or int(g2[0])!=0 or int(g3[0])!=0) and (int(g1[1])!=0 or int(g2[1])!=0 or int(g3[1])!=0):
                    per=((int(g1[0])+int(g2[0])+int(g3[0]))/(int(g1[1])+int(g2[1])+int(g3[1])))*100
                    per=round(per,1)
                yaxis.append(per)
                xaxis.append(k[0])
            plt.bar(xaxis, yaxis)
            plt.ylabel('STUDENTS PROGRESS')
            plt.show()
                
        label_4 = Label(newWindow, text="Student Progress:",width=0,font=("times new roman", 20))
        label_4.place(x=3,y=450)

        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black',command=graph).place(x=0,y = 490)

        #################################### Notepad Calling:

        def openNewWindow_Freshman():

            # Toplevel object which will 
            # be treated as a new window
            newWindow1 = Toplevel(newWindow)
            
            def saveFile():
                new_file = asksaveasfile(mode = 'w', filetype = [('text files', '.txt')])
                if new_file is None:
                    return
                text = str(entry.get(1.0, END))
                new_file.write(text)
                new_file.close()

            def openFile():
                file = askopenfile(mode = 'r', filetype = [('text files', '*.txt')])
                if file is not None:
                    content = file.read()
                entry.insert(INSERT, content)

            def clearFile():
                entry.delete(1.0, END)

            # newWindow = tk.Tk()
            newWindow1.geometry("400x600")
            newWindow1.title("Notepad")
            # newWindow.config(bg = "white")
            top = Frame(newWindow1)
            top.pack(padx = 10, pady = 5, anchor = 'nw')

            b1 = Button(newWindow1, text="Open", bg = "white", command = openFile)
            b1.pack(in_ = top, side=LEFT)

            b2 = Button(newWindow1, text="Save", bg = "white", command = saveFile)
            b2.pack(in_ = top, side=LEFT)

            b3 = Button(newWindow1, text="Clear", bg = "white", command = clearFile)
            b3.pack(in_ = top, side=LEFT)

            b4 = Button(newWindow1, text="Exit", bg = "white", command = exit)
            b4.pack(in_ = top, side=LEFT)

            entry = Text(newWindow1, wrap = WORD, bg = "#F9DDA4", font = ("poppins", 15))
            entry.pack(padx = 10, pady = 5, expand = TRUE, fill = BOTH)

            # A Label widget to show in toplevel
            Label(newWindow1).pack()
        # Announcement Pad:
        label_5 = Label(newWindow, text="Announcement PAD:",width=0,font=("times new roman", 20))
        label_5.place(x=4,y=590)

        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black', command = openNewWindow_Freshman).place(x=0,y = 640)
        #################################### CLEAR  FUNCTION
        def clear():
            label_5 = Label(newWindow, text="                                     ",width=789,font=("times new roman", 400),bg='white',fg='black')
            label_5.place(x=320,y=0)
        Button(newWindow, text=' CLEAR ',width=15, height = 3,font=("times new roman", 15),bg='yellow',fg='black', command = clear).place(x=1200,y = 620)
        label_5 = Label(newWindow, text="                                     ",width=789,font=("times new roman", 400),bg='white',fg='black')
        label_5.place(x=320,y=0)
        # A Label widget to show in toplevel
        Label(newWindow).pack()
    # Seniors
    im3 = PhotoImage(file='c5.png')
    im3 = im3.subsample(2,2)
    button1=tkinter.Button(master, text="button3",width=200,
                            height=190,command=openNewWindow_Senior1,image=im3)
    button1.place(x=300, y=510)
    ########################################
    #######################################################################
    ################################################################################
    def openNewWindow_Freshman2():
        global Pfun_course
        # Toplevel object which will 
        # be treated as a new window
        newWindow = Toplevel(master)
        newWindow.title("MANAGEMENT")
        newWindow.geometry("2000x2000")
        def std():
            global Pfun_course
            label_1 = Label(newWindow, text="STUDENTS",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=400,y=20)
            label_1 = Label(newWindow, text="YEAR",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=800,y=20)
            label_1 = Label(newWindow, text="MAJOR",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=1000,y=20)
            label_1 = Label(newWindow, text="ID",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=1200,y=20)
            a=70
            num=1
            for k in Pfun_course:
                label_1 = Label(newWindow, text=str(num)+"   "+k[0],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=400,y=a)
                label_1 = Label(newWindow, text=k[1],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=800,y=a)
                label_1 = Label(newWindow, text=k[3],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=1000,y=a)
                label_1 = Label(newWindow, text=k[2],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=1200,y=a)
                a+=50
                num+=1
                
        label_1 = Label(newWindow, text="List of Students:",width=0,font=("times new roman", 20))
        label_1.place(x=0,y=0)

        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black',command=std).place(x=0,y = 40)
        #########################################
        ################    Grade List:
        def GL():
            global Pfun_course
            label_1 = Label(newWindow, text="STUDENTS",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=350,y=20)
            label_1 = Label(newWindow, text="TEST#1",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=700,y=20)
            label_1 = Label(newWindow, text="TEST#2",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=850,y=20)
            label_1 = Label(newWindow, text="TEST#3",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=1000,y=20)
            label_1 = Label(newWindow, text="PERCENTAGE",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=1150,y=20)
            a=70
            num=1
            for k in Pfun_course:
                label_1 = Label(newWindow, text=str(num)+"   "+k[0],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=350,y=a)
                g1=k[5].split('/')
                g2=k[6].split('/')
                g3=k[7].split('/')
                label_1 = Label(newWindow, text=k[4+1],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=700,y=a)
                label_1 = Label(newWindow, text=k[5+1],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=850,y=a)
                label_1 = Label(newWindow, text=k[6+1],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=1000,y=a)
                per=0
                if (int(g1[0])!=0 or int(g2[0])!=0 or int(g3[0])!=0) and (int(g1[1])!=0 or int(g2[1])!=0 or int(g3[1])!=0):
                    per=((int(g1[0])+int(g2[0])+int(g3[0]))/(int(g1[1])+int(g2[1])+int(g3[1])))*100
                    per=round(per,1)
                label_1 = Label(newWindow, text=str(per)+"%",width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=1150,y=a)
                a+=50
                num+=1
        label_2 = Label(newWindow, text="Grade List:",width=0,font=("times new roman", 20))
        label_2.place(x=1,y=150)
        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black',command=GL).place(x=0,y = 190)
    ########################v Upgrade grade:

        def openNewWindow_Freshman1():

            # Toplevel object which will 
            # be treated as a new window
            newWindow2 = Toplevel(newWindow)
            def upgrad():
                MergeSort(Pfun_course)
                ID=id.get()
                result=binary_search_iterative(Pfun_course,int(ID),True)
                t1=testt1.get()
                t2=testt2.get()
                t3=testt3.get()
                li=Pfun_course[result]
                if len(t1)!=0:
                    li[5],t1=t1,li[5]
                if len(t2)!=0:
                    li[6],t2=t2,li[6]
                if len(t3)!=0:
                    li[7],t3=t3,li[7]
                label_09 = Label(newWindow2, text="GRADES UPDATED ",width=0,font=("times new roman", 20))
                label_09.place(x=600,y=600)   
                update_data2(linelist1)
            # update grade
            label_08 = Label(newWindow2, text="UPDATE GRADE",width=0,font=("times new roman", 40,"bold"))
            label_08.place(x=470,y=10)   
            
            # student name
            label_09 = Label(newWindow2, text="Student ID :",width=0,font=("times new roman", 20))
            label_09.place(x=0,y=150)   
            id=StringVar()
            textBox1 = Entry(newWindow2,textvariable=id, width = 20, font = ("times new roman", 20))
            textBox1.place(x = 180, y = 150)     
            
            # test 1:
            label_05 = Label(newWindow2, text="Test 1:",width=0,font=("times new roman", 20))
            label_05.place(x=0,y=270)   
            testt1=StringVar()
            textBox2 = Entry(newWindow2,textvariable=testt1, width = 7, font = ("times new roman", 20))
            textBox2.place(x = 100, y = 270)
            
            # test 2:
            label_04 = Label(newWindow2, text="Test 2:",width=0,font=("times new roman", 20))
            label_04.place(x=0,y=370)   
            testt2=StringVar()
            textBox3 = Entry(newWindow2,textvariable=testt2, width = 7, font = ("times new roman", 20))
            textBox3.place(x = 100, y = 370)
            
            # test 3:
            label_07 = Label(newWindow2, text="Test 3:",width=0,font=("times new roman", 20))
            label_07.place(x=0,y=470)   
            testt3=StringVar()
            textBox6 = Entry(newWindow2,textvariable=testt3, width = 7, font = ("times new roman", 20))
            textBox6.place(x = 100, y = 470)
            ######## DATA ID ###################
            label_1 = Label(newWindow2, text="STUDENTS",width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
            label_1.place(x=500+200,y=90)
            label_1 = Label(newWindow2, text="ID",width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
            label_1.place(x=850+200,y=90)
            num=1
            a=130
            for k in Pfun_course:
                label_1 = Label(newWindow2, text=str(num)+"   "+k[0],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=500+200,y=a)
                label_1 = Label(newWindow2, text=k[2],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=850+200,y=a)
                a+=50
                num+=1
            # update button
            Button(newWindow2, text='Update',width=15, height = 3,font=("times new roman", 15),bg='yellow',fg='black', command = upgrad).place(x=0,y = 570)

            # newWindow = tk.Tk()
            newWindow2.geometry("40000x60000")
            newWindow2.title("Update Grade")
            # newWindow.config(bg = "white")
            top = Frame(newWindow2)
            top.pack(padx = 10, pady = 5, anchor = 'nw')
        label_3 = Label(newWindow, text="Update Grade:",width=0,font=("times new roman", 20))
        label_3.place(x=2,y=300)
        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black', command = openNewWindow_Freshman1).place(x=0,y = 340)

    ################################################# Students Progress
        def graph():
            xaxis=[]
            yaxis=[]
            for k in Pfun_course:
                g1=k[5].split('/')
                g2=k[6].split('/')
                g3=k[7].split('/')
                per=0
                if (int(g1[0])!=0 or int(g2[0])!=0 or int(g3[0])!=0) and (int(g1[1])!=0 or int(g2[1])!=0 or int(g3[1])!=0):
                    per=((int(g1[0])+int(g2[0])+int(g3[0]))/(int(g1[1])+int(g2[1])+int(g3[1])))*100
                    per=round(per,1)
                yaxis.append(per)
                xaxis.append(k[0])
            plt.bar(xaxis, yaxis)
            plt.ylabel('STUDENTS PROGRESS')
            plt.show()
                
        label_4 = Label(newWindow, text="Student Progress:",width=0,font=("times new roman", 20))
        label_4.place(x=3,y=450)

        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black',command=graph).place(x=0,y = 490)

        #################################### Notepad Calling:

        def openNewWindow_Freshman():

            # Toplevel object which will 
            # be treated as a new window
            newWindow1 = Toplevel(newWindow)
            
            def saveFile():
                new_file = asksaveasfile(mode = 'w', filetype = [('text files', '.txt')])
                if new_file is None:
                    return
                text = str(entry.get(1.0, END))
                new_file.write(text)
                new_file.close()

            def openFile():
                file = askopenfile(mode = 'r', filetype = [('text files', '*.txt')])
                if file is not None:
                    content = file.read()
                entry.insert(INSERT, content)

            def clearFile():
                entry.delete(1.0, END)

            # newWindow = tk.Tk()
            newWindow1.geometry("400x600")
            newWindow1.title("Notepad")
            # newWindow.config(bg = "white")
            top = Frame(newWindow1)
            top.pack(padx = 10, pady = 5, anchor = 'nw')

            b1 = Button(newWindow1, text="Open", bg = "white", command = openFile)
            b1.pack(in_ = top, side=LEFT)

            b2 = Button(newWindow1, text="Save", bg = "white", command = saveFile)
            b2.pack(in_ = top, side=LEFT)

            b3 = Button(newWindow1, text="Clear", bg = "white", command = clearFile)
            b3.pack(in_ = top, side=LEFT)

            b4 = Button(newWindow1, text="Exit", bg = "white", command = exit)
            b4.pack(in_ = top, side=LEFT)

            entry = Text(newWindow1, wrap = WORD, bg = "#F9DDA4", font = ("poppins", 15))
            entry.pack(padx = 10, pady = 5, expand = TRUE, fill = BOTH)

            # A Label widget to show in toplevel
            Label(newWindow1).pack()
        # Announcement Pad:
        label_5 = Label(newWindow, text="Announcement PAD:",width=0,font=("times new roman", 20))
        label_5.place(x=4,y=590)

        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black', command = openNewWindow_Freshman).place(x=0,y = 640)
        #################################### CLEAR  FUNCTION
        def clear():
            label_5 = Label(newWindow, text="                                     ",width=789,font=("times new roman", 400),bg='white',fg='black')
            label_5.place(x=320,y=0)
        Button(newWindow, text=' CLEAR ',width=15, height = 3,font=("times new roman", 15),bg='yellow',fg='black', command = clear).place(x=1200,y = 620)
        label_5 = Label(newWindow, text="                                     ",width=789,font=("times new roman", 400),bg='white',fg='black')
        label_5.place(x=320,y=0)
        # A Label widget to show in toplevel
        Label(newWindow).pack()
    #############################################
    ############3  freshman HEADING
    HEADING =Label(master,text ='FRESHMAN',font= ('Helvetica 18 underline'),bg="black",fg="white")
    HEADING.place(x=140, y = 30, anchor ='ne')
    im12 = PhotoImage(file='c2.png')
    im12 = im12.subsample(2,2)
    button1=tkinter.Button(master,width=200,image=im12,
                            height=180,command=openNewWindow_Freshman2,compound=CENTER)
    button1.place(x=300, y=70)
    ###############################################################
    ########################################################################
    ########################################################################################
    def openNew_windowsohpomore2():
        global ECA_course
        # Toplevel object which will 
        # be treated as a new window
        newWindow = Toplevel(master)
        newWindow.title("MANAGEMENT")
        newWindow.geometry("2000x2000")
        def std():
            global ECA_course
            label_1 = Label(newWindow, text="STUDENTS",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=400,y=20)
            label_1 = Label(newWindow, text="YEAR",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=800,y=20)
            label_1 = Label(newWindow, text="MAJOR",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=1000,y=20)
            label_1 = Label(newWindow, text="ID",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=1200,y=20)
            a=70
            num=1
            for k in ECA_course:
                label_1 = Label(newWindow, text=str(num)+"   "+k[0],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=400,y=a)
                label_1 = Label(newWindow, text=k[1],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=800,y=a)
                label_1 = Label(newWindow, text=k[3],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=1000,y=a)
                label_1 = Label(newWindow, text=k[2],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=1200,y=a)
                a+=50
                num+=1
                
        label_1 = Label(newWindow, text="List of Students:",width=0,font=("times new roman", 20))
        label_1.place(x=0,y=0)

        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black',command=std).place(x=0,y = 40)
        #########################################
        ################    Grade List:
        def GL():
            global ECA_course
            label_1 = Label(newWindow, text="STUDENTS",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=350,y=20)
            label_1 = Label(newWindow, text="TEST#1",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=700,y=20)
            label_1 = Label(newWindow, text="TEST#2",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=850,y=20)
            label_1 = Label(newWindow, text="TEST#3",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=1000,y=20)
            label_1 = Label(newWindow, text="PERCENTAGE",width=0,font=('Helvetica 18 underline italic', 20),bg='red',fg='white')
            label_1.place(x=1150,y=20)
            a=70
            num=1
            for k in ECA_course:
                label_1 = Label(newWindow, text=str(num)+"   "+k[0],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=350,y=a)
                g1=k[5].split('/')
                g2=k[6].split('/')
                g3=k[7].split('/')
                label_1 = Label(newWindow, text=k[4+1],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=700,y=a)
                label_1 = Label(newWindow, text=k[5+1],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=850,y=a)
                label_1 = Label(newWindow, text=k[6+1],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=1000,y=a)
                per=0
                if (int(g1[0])!=0 or int(g2[0])!=0 or int(g3[0])!=0) and (int(g1[1])!=0 or int(g2[1])!=0 or int(g3[1])!=0):
                    per=((int(g1[0])+int(g2[0])+int(g3[0]))/(int(g1[1])+int(g2[1])+int(g3[1])))*100
                    per=round(per,1)
                label_1 = Label(newWindow, text=str(per)+"%",width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=1150,y=a)
                a+=50
                num+=1
        label_2 = Label(newWindow, text="Grade List:",width=0,font=("times new roman", 20))
        label_2.place(x=1,y=150)
        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black',command=GL).place(x=0,y = 190)
    ########################v Upgrade grade:

        def openNew_windowsohpomore2():

            # Toplevel object which will 
            # be treated as a new window
            newWindow2 = Toplevel(newWindow)
            def upgrad():
                MergeSort(ECA_course)
                ID=id.get()
                result=binary_search_iterative(ECA_course,int(ID),True)
                t1=testt1.get()
                t2=testt2.get()
                t3=testt3.get()
                li=ECA_course[result]
                if len(t1)!=0:
                    li[5],t1=t1,li[5]
                if len(t2)!=0:
                    li[6],t2=t2,li[6]
                if len(t3)!=0:
                    li[7],t3=t3,li[7]
                label_09 = Label(newWindow2, text="GRADES UPDATED ",width=0,font=("times new roman", 20))
                label_09.place(x=600,y=600)   
                update_data2(linelist1)
            # update grade
            label_08 = Label(newWindow2, text="UPDATE GRADE",width=0,font=("times new roman", 40,"bold"))
            label_08.place(x=470,y=10)   
            
            # student name
            label_09 = Label(newWindow2, text="Student ID :",width=0,font=("times new roman", 20))
            label_09.place(x=0,y=150)   
            id=StringVar()
            textBox1 = Entry(newWindow2,textvariable=id, width = 20, font = ("times new roman", 20))
            textBox1.place(x = 180, y = 150)     
            
            # test 1:
            label_05 = Label(newWindow2, text="Test 1:",width=0,font=("times new roman", 20))
            label_05.place(x=0,y=270)   
            testt1=StringVar()
            textBox2 = Entry(newWindow2,textvariable=testt1, width = 7, font = ("times new roman", 20))
            textBox2.place(x = 100, y = 270)
            
            # test 2:
            label_04 = Label(newWindow2, text="Test 2:",width=0,font=("times new roman", 20))
            label_04.place(x=0,y=370)   
            testt2=StringVar()
            textBox3 = Entry(newWindow2,textvariable=testt2, width = 7, font = ("times new roman", 20))
            textBox3.place(x = 100, y = 370)
            
            # test 3:
            label_07 = Label(newWindow2, text="Test 3:",width=0,font=("times new roman", 20))
            label_07.place(x=0,y=470)   
            testt3=StringVar()
            textBox6 = Entry(newWindow2,textvariable=testt3, width = 7, font = ("times new roman", 20))
            textBox6.place(x = 100, y = 470)
            ######## DATA ID ###################
            label_1 = Label(newWindow2, text="STUDENTS",width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
            label_1.place(x=500+200,y=90)
            label_1 = Label(newWindow2, text="ID",width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
            label_1.place(x=850+200,y=90)
            num=1
            a=130
            for k in ECA_course:
                label_1 = Label(newWindow2, text=str(num)+"   "+k[0],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=500+200,y=a)
                label_1 = Label(newWindow2, text=k[2],width=0,font=('Helvetica 18 underline italic', 20),bg='blue',fg='white')
                label_1.place(x=850+200,y=a)
                a+=50
                num+=1
            # update button
            Button(newWindow2, text='Update',width=15, height = 3,font=("times new roman", 15),bg='yellow',fg='black', command = upgrad).place(x=0,y = 570)

            # newWindow = tk.Tk()
            newWindow2.geometry("40000x60000")
            newWindow2.title("Update Grade")
            # newWindow.config(bg = "white")
            top = Frame(newWindow2)
            top.pack(padx = 10, pady = 5, anchor = 'nw')
        label_3 = Label(newWindow, text="Update Grade:",width=0,font=("times new roman", 20))
        label_3.place(x=2,y=300)
        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black', command = openNew_windowsohpomore2).place(x=0,y = 340)

    ################################################# Students Progress
        def graph():
            xaxis=[]
            yaxis=[]
            for k in ECA_course:
                g1=k[5].split('/')
                g2=k[6].split('/')
                g3=k[7].split('/')
                per=0
                if (int(g1[0])!=0 or int(g2[0])!=0 or int(g3[0])!=0) and (int(g1[1])!=0 or int(g2[1])!=0 or int(g3[1])!=0):
                    per=((int(g1[0])+int(g2[0])+int(g3[0]))/(int(g1[1])+int(g2[1])+int(g3[1])))*100
                    per=round(per,1)
                yaxis.append(per)
                xaxis.append(k[0])
            plt.bar(xaxis, yaxis)
            plt.ylabel('STUDENTS PROGRESS')
            plt.show()
                
        label_4 = Label(newWindow, text="Student Progress:",width=0,font=("times new roman", 20))
        label_4.place(x=3,y=450)

        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black',command=graph).place(x=0,y = 490)

        #################################### Notepad Calling:

        def openNewWindow_Freshman():

            # Toplevel object which will 
            # be treated as a new window
            newWindow1 = Toplevel(newWindow)
            
            def saveFile():
                new_file = asksaveasfile(mode = 'w', filetype = [('text files', '.txt')])
                if new_file is None:
                    return
                text = str(entry.get(1.0, END))
                new_file.write(text)
                new_file.close()

            def openFile():
                file = askopenfile(mode = 'r', filetype = [('text files', '*.txt')])
                if file is not None:
                    content = file.read()
                entry.insert(INSERT, content)

            def clearFile():
                entry.delete(1.0, END)

            # newWindow = tk.Tk()
            newWindow1.geometry("400x600")
            newWindow1.title("Notepad")
            # newWindow.config(bg = "white")
            top = Frame(newWindow1)
            top.pack(padx = 10, pady = 5, anchor = 'nw')

            b1 = Button(newWindow1, text="Open", bg = "white", command = openFile)
            b1.pack(in_ = top, side=LEFT)

            b2 = Button(newWindow1, text="Save", bg = "white", command = saveFile)
            b2.pack(in_ = top, side=LEFT)

            b3 = Button(newWindow1, text="Clear", bg = "white", command = clearFile)
            b3.pack(in_ = top, side=LEFT)

            b4 = Button(newWindow1, text="Exit", bg = "white", command = exit)
            b4.pack(in_ = top, side=LEFT)

            entry = Text(newWindow1, wrap = WORD, bg = "#F9DDA4", font = ("poppins", 15))
            entry.pack(padx = 10, pady = 5, expand = TRUE, fill = BOTH)

            # A Label widget to show in toplevel
            Label(newWindow1).pack()
        # Announcement Pad:
        label_5 = Label(newWindow, text="Announcement PAD:",width=0,font=("times new roman", 20))
        label_5.place(x=4,y=590)

        Button(newWindow, text='Click Here',width=20, height = 3,font=("times new roman", 15),bg='yellow',fg='black', command = openNewWindow_Freshman).place(x=0,y = 640)
        #################################### CLEAR  FUNCTION
        def clear():
            label_5 = Label(newWindow, text="                                     ",width=789,font=("times new roman", 400),bg='white',fg='black')
            label_5.place(x=320,y=0)
        Button(newWindow, text=' CLEAR ',width=15, height = 3,font=("times new roman", 15),bg='yellow',fg='black', command = clear).place(x=1200,y = 620)
        label_5 = Label(newWindow, text="                                     ",width=789,font=("times new roman", 400),bg='white',fg='black')
        label_5.place(x=320,y=0)
        # A Label widget to show in toplevel
        Label(newWindow).pack()
    #############################################
    ############3  freshman HEADING
    HEADING =Label(master,text ='FRESHMAN',font= ('Helvetica 18 underline'),bg="black",fg="white")
    HEADING.place(x=140, y = 30, anchor ='ne')
    im21 = PhotoImage(file='c7.png')
    im21 = im21.subsample(2,2)
    button1=tkinter.Button(master,width=200,image=im21,
                            height=180,command=openNew_windowsohpomore2,compound=CENTER)
    button1.place(x=300, y=285)


    get_time()
    master.mainloop()
else:
    print("TRY AGAINN !!!!!!!!!!!!!!!!")


    
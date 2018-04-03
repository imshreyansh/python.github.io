from Tkinter import *
import sqlite3
from tkMessageBox import *
con=sqlite3.Connection('Bus_users')
cur=con.cursor()
cur.execute("create table if not exists Bus(username varchar(20) primary key,fname varchar(20),lname varchar(20),password varchar(20))")

root = Tk()
root.title("Project Information")
root.configure(background='blue')
root.iconbitmap('images/icon.ico')

Label(root, text="Bus Booking", font=("algerian", 20), fg="white", bg="blue", width=28).grid(row=0, column=0)
Label(root, text="Name: Shreyansh Upadhyay", font=("algerian", 15), fg="white", bg="blue").grid(row=1, column=0)
Label(root, text="Enroll No.: 151399", font=("algerian", 15), fg="white", bg="blue").grid(row=2, column=0)
Label(root, text="Batch: B6", font=("algerian", 15), fg="white", bg="blue").grid(row=3, column=0)

def now():
    root.destroy()
    root1 = Tk()
    root1.title("Welcome To The Bus Booking Service")
    root1.iconbitmap('images/icon.ico')

    def account():
        user = username.get()
        cur.execute("select username from Bus where username=(?)", (user,))
        a = cur.fetchall()
        if a != []:
            showerror('Error',"Username Already Exists")
        else:
            l = (username.get(), fname.get(), lname.get(), password.get())
            cur.execute("insert into Bus values(?,?,?,?)",l)
            showinfo('Congratulations !!',"You Are A User Now")
            con.commit()
            username.delete(0,20)
            fname.delete(0,20)
            lname.delete(0,20)
            password.delete(0,20)
            
            
    def account1():
        usr = user.get()
        pasw = pas.get()
        cur.execute("select * from Bus where username=(?) and password=(?)", (usr, pasw,))
        a = cur.fetchall()
        if a==[]:
            showerror('Log In Failed', "Invalid Username or Password")
        else:
            root1.destroy()
            root = Tk()
            root.title("Bus Booking Window")
            root.iconbitmap('images/icon.ico')
            Label(root, text="Bus Booking", font=("algerian", 20), fg="Blue", bg="white", width=53).grid(row=0, column=0, columnspan=4)
            pic = PhotoImage(file="images/bus.gif")
            Label(root, image=pic).grid(row=1,column=0, columnspan=4)
            Label(root, text="Fill The Field To Book", font=("arial", 12), fg="Blue", bg="#CD853F", width=45).grid(row=2, column=0, columnspan=2)
            Label(root, text="Available Seats", font=("arial", 12), fg="Blue", bg="#CD853F", width=45).grid(row=2, column=2, columnspan=2)

            #Bus Booking Information
            def register():
                if fr.get() == "Delhi" and to.get() == "chandigarh":
                    Label(root, text="Indus",  font=("cooper black", 15)).grid(row=3, column=3)
                    Label(root, text="100",  font=("cooper black", 15)).grid(row=4, column=3)
                    
                    
                if fr.get() == "Delhi" and to.get() == "Varanasi":
                    Label(root, text="Casio",  font=("cooper black", 15)).grid(row=3, column=3)
                    Label(root, text="100",  font=("cooper black", 15)).grid(row=4, column=3)
                   
                    
                if fr.get() == "Delhi" and to.get() == "Lucknow":
                    Label(root, text="Smong",  font=("cooper black", 15)).grid(row=3, column=3)
                    Label(root, text="100",  font=("cooper black", 15)).grid(row=4, column=3)
                   

                if fr.get() == "Varanasi" and to.get() == "Delhi":
                    showerror('Error', "No bus available for this route.")

                if fr.get() == "Varanasi" and to.get() == "chandigarh":
                    Label(root, text="Pagara",  font=("cooper black", 15)).grid(row=3, column=3)
                    Label(root, text="100",  font=("cooper black", 15)).grid(row=4, column=3)
                    

                if fr.get() == "Varanasi" and to.get() == "Lucknow":
                    Label(root, text="Ganga",  font=("cooper black", 15)).grid(row=3, column=3)
                    Label(root, text="100",  font=("cooper black", 15)).grid(row=4, column=3)
                    
                    
                if fr.get() == "Lucknow" and to.get() == "Delhi":
                    Label(root, text="vanas",  font=("cooper black", 15)).grid(row=3, column=3)
                    Label(root, text="100",  font=("cooper black", 15)).grid(row=4, column=3)
                    

                if fr.get() == "Lucknow" and to.get() == "chandigarh":
                    Label(root, text="Wango",  font=("cooper black", 15)).grid(row=3, column=3)
                    Label(root, text="100",  font=("cooper black", 15)).grid(row=4, column=3)
                    

                if fr.get() == "Lucknow" and to.get() == "Varanasi":
                    Label(root, text="volvo",  font=("cooper black", 15)).grid(row=3, column=3)
                    Label(root, text="100",  font=("cooper black", 15)).grid(row=4, column=3)
                    
                    
                if fr.get() == "chandigarh" and to.get() == "Delhi":
                    Label(root, text="Pagani",  font=("cooper black", 15)).grid(row=3, column=3)
                    Label(root, text="100",  font=("cooper black", 15)).grid(row=4, column=3)
                   

                if fr.get() == "chandigarh" and to.get() == "Lucknow":
                    Label(root, text="vanity",  font=("cooper black", 15)).grid(row=3, column=3)
                    Label(root, text="100",  font=("cooper black", 15)).grid(row=4, column=3)
                    

                if fr.get() == "chandigarh" and to.get() == "Varanasi":
                    showerror('Sorry', "No Bus Available")

            def go():
                root.destroy()
                root1 = Tk()
                root1.title("Provide Details")
                root1.iconbitmap('images/icon.ico')
                Label(root1, text="Bus Booking", font=("algerian", 20), fg="Blue", bg="white", width=53).grid(row=0, column=0, columnspan=4)
                Label(root1, text="Passenger Detail", font=("arial", 12), fg="Blue", bg="#CD853F", width=22).grid(row=1, column=0)
                Label(root1, text="Name", font=("arial", 12), fg="Blue", bg="#CD853F", width=27).grid(row=1, column=1)
                Label(root1, text="Gender", font=("arial", 12), fg="Blue", bg="#CD853F", width=22).grid(row=1, column=2)

                Label(root1, text="Passenger 1",  font=("cooper black", 15), fg="Blue",).grid(row=2, column=0)
                name = Entry(root1, width=30, font=("arial", 11),bg=('#ffcccc'))
                name.grid(row=2, column=1)
                gender = StringVar(root1)
                gender.set("Select")
                OptionMenu(root1, gender, "Male", "Female").grid(row=2, column=2)
            

                Label(root1, text="Passenger 2",  font=("cooper black", 15), fg="Blue").grid(row=3, column=0)
                name = Entry(root1, width=30, font=("arial", 11),bg=('#ffcccc'))
                name.grid(row=3, column=1)
                gender = StringVar(root1)
                gender.set("Select")
                OptionMenu(root1, gender, "Male", "Female").grid(row=3, column=2)
               

                Label(root1, text="Passenger 3",  font=("cooper black", 15), fg="Blue").grid(row=4, column=0)
                name = Entry(root1, width=30, font=("arial", 11),bg=('#ffcccc'))
                name.grid(row=4, column=1)
                gender = StringVar(root1)
                gender.set("Select")
                OptionMenu(root1, gender, "Male", "Female").grid(row=4, column=2)
                

                Label(root1, text="Passenger 4",  font=("cooper black", 15), fg="Blue").grid(row=5, column=0)
                name = Entry(root1, width=30, font=("arial", 11),bg=('#ffcccc'))
                name.grid(row=5, column=1)
                gender = StringVar(root1)
                gender.set("Select")
                OptionMenu(root1, gender, "Male", "Female").grid(row=5, column=2)
                


                def done():
                    showinfo('Congratulations !!', "Ticket Booked")
                    root1.destroy()

                Button(root1, text="Book Ticket", compound='center', font=("arial", 10), bg='blue', fg='white', width=15, command=lambda: done()).grid(row=8, columnspan=4)




            #Station Selection
            Label(root, text="From: ", font=("cooper black", 15),fg="Blue").grid(row=3, column=0)
            fr = StringVar(root)
            fr.set("Source")
            OptionMenu(root, fr, "Delhi", "Varanasi", "Lucknow", "chandigarh").grid(row=3, column=1)
            
            Label(root, text="To: ", font=("cooper black", 15),fg="Blue").grid(row=4, column=0)
            to = StringVar(root)
            to.set("Destination")
            OptionMenu(root, to, "Delhi", "Varanasi", "Lucknow", "chandigarh").grid(row=4, column=1)
            
            Label(root, text="Travelling Date:", font=("cooper black", 15),fg="Blue").grid(row=5, column=0)
            date = Entry(root, width=30, font=("arial", 11),bg=('#ffcccc'))
            date.grid(row=5, column=1)
            date.insert(0,"dd/mm")
            
           
            Button(root, text="Submit", compound='center', font=("arial", 10), bg='Blue', fg='white', width=10, command=lambda: register()).grid(row=7, columnspan=2)

            #Availablity
            Label(root, text="Bus Name: ", font=("cooper black", 15),fg="Blue").grid(row=3, column=2)
            Label(root, text="00", font=("cooper black", 15),fg="Blue").grid(row=3, column=3)
            Label(root, text="Available Seats: ", font=("cooper black", 15),fg="Blue").grid(row=4, column=2)
            Label(root, text="00", font=("cooper black", 15),fg="Blue").grid(row=4, column=3)
           

            Button(root, text="Book Now", compound='center', font=("arial", 10), bg='Blue', fg='white', width=10, command=lambda: go()).grid(row=9, column=2, columnspan=2)
            Entry().insert("Sorry For The Error !!")




    Label(root1, text="Bus Booking", font=("algerian", 20), fg="Blue", bg="white", width=53).grid(row=0, column=0, columnspan=4)
    img = PhotoImage(file="images/bus.gif")
    Label(root1,image=img).grid(row=1,column=0, columnspan=4)
    Label(root1, text="Already a User ? Log In", font=("arial", 12), fg="Blue", bg="white", width=45).grid(row=2, column=0, columnspan=2)
    Label(root1, text="Dont have an account ? Register", font=("arial", 12), fg="Blue", bg="White", width=45).grid(row=2, column=2, columnspan=2)
    #Entry account1
    Label(root1, text="Username: ", font=("cooper black", 15),fg=('Blue')).grid(row=3, column=0)
    user = Entry(width=30, font=("arial", 11), bg=('#ffcccc'))
    user.grid(row=3, column=1)

    Label(root1, text="Password: ", font=("cooper black", 15),fg=('Blue')).grid(row=4, column=0)
    pas = Entry(width=30, font=("arial", 11), bg=('#ffcccc'))
    pas.grid(row=4, column=1)

    Button(root1, text="Log In", compound='center', font=("arial", 10), bg='Blue', fg='white', width=10, command=lambda: account1()).grid(row=5, columnspan=2)

    #Entry account
    Label(root1, text="Username: ", font=("cooper black", 15),fg=('Blue')).grid(row=3, column=2)
    username = Entry(root1, width=30, font=("arial", 11), bg=('#ffcccc') )
    username.grid(row=3, column=3)

    Label(root1, text="Firstname: ", font=("cooper black", 15),fg=('Blue')).grid(row=4, column=2)
    fname = Entry(root1, width=30, font=("arial", 11), bg=('#ffcccc'))
    fname.grid(row=4, column=3)

    Label(root1, text="Lastname: ", font=("cooper black", 15),fg=('Blue')).grid(row=5, column=2)
    lname = Entry(root1, width=30, font=("arial", 11), bg=('#ffcccc'))
    lname.grid(row=5, column=3)

    Label(root1, text="Password: ", font=("cooper black", 15),fg=('Blue')).grid(row=6, column=2)
    password = Entry(root1, width=30, font=("arial", 11), bg=('#ffcccc'))
    password.grid(row=6, column=3)

    Button(root1, text="Sign Up", compound='center', font=("arial", 10), bg='Blue', fg='white', width=10, command=lambda: account()).grid(row=7, column=3, columnspan=2)
    root1.mainloop()

Button(root, text="Click To Go", font=("Times New Roman", 14), bg='Brown', fg='white', width=50, command=lambda: now()).grid(row=4, column=0)

root.mainloop()

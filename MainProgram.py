import readfile as rf
import Maindisplay as dl
import Write as w
import datetime
path = "libary books.txt"
main_db= rf.main_db(path)
dl.display_items(main_db)
dl.menu_message()

u_Value = False
while u_Value == False:
    try:
        
        user_number = int(input("Enter a number:"))
        if user_number > 0 and user_number<5:
            #dl.menu_message()
            u_Value = True
        else:
            print('Invalid Synatx')
    except:
        print('Invalid ')
        
def borrow(db):
    #print(db)
    
    val=False
    while val==False:
        try:
            student_name=input("Enter your First Name:").lower().strip()
            student_id=str(int(input("Enter your student id")))
            val=True
        except:
            print("Invalid Name")
    
    
    time = str(datetime.datetime.now())
    print(time)
    student_file=open(student_name+student_id+".txt","a")
    student_file.write("Student Name : "+student_name+"\n")
    student_file.write("Student ID : "+student_id+"\n")
    student_file.write(time+"\n")
    value=False      
    while value==False:
        try:
            borrowing = int(input("Enter the serial no of the book you want to borrow:"))
            #print(db)
            if borrowing <= len(db):
                
                if  borrowing>0 and borrowing<13:
                    value=True
    
                    user_value=False
                    while user_value==False:
                        try:
                            user_qty = int(input("Enter the quantity  of books you want to borrow:"))
                            if user_qty>0:
                                if user_qty<=int(db[borrowing-1][2]) :
                                    db[borrowing-1][2]=str(int(db[borrowing-1][2])-user_qty)
                                    price=str(float(db[borrowing-1][3])*user_qty)
                                    student_file.write("Name of Book : "+db[borrowing-1][0]+"\n")
                                    student_file.write("Name of Author : "+db[borrowing-1][1]+"\n")
                                    student_file.write("Price : "+price+"\n")
                                    print("the name of Book:"+(db[borrowing-1][0]))
                                    print("the name of Author:"+(db[borrowing-1][1]))
                                    print("the total price:"+price)
                                    user_value=True                                  
                                else:
                                    print("The number of quantity you have entered is invalid")    
                            elif user_qty==0:
                                print("the is not quantity")
                                user_value=True
                                value = False
                                     #retun(db)                        
                            else:
                                print("wrong quantity ")
                                user_value=False
                        except:
                          print("Invalid syntax")            
                else:
                    print("The number you have entered to borrow is invalid serial number")
            else:
                    print("The number you have entered to borrow is invalid serial number")
                            
            
        except:
            print('Invalid Serial Number')
         
            
    return db

def return_books(db):
    value=False     
    while value==False:
        try:
            returing = int(input("Enter the serial no of the book you want to return:"))
            #print(db)
            if returing <= len(db):
                
                if  returing>0 and returing<13:
                    value=True
    
                    user_val=False
                    while user_val==False:
                        try:
                            return_qty = int(input("Enter the quantity  of books you want to return:"))
                            if return_qty <4 and return_qty >0:
                                db[return_qty-1][2]=str(int(db[return_qty -1][2])+return_qty )
                                price=str(float(db[return_qty -1][3])*return_qty )
                                user_val=True            
                            else:
                                print("The number of quantity you have entered is invalid")
                                print("The available stock of books is",db[return_qty -1][2])
                                user_val=False
                            
                        except:
                            print("Invalid syntax occured")           
                else:
                    print("The number you have entered to return is invalid serial number")
            else:
                    print("The number you have entered to return is invalid serial number")
                            
            
        except:
            print('Invalid Serial Number')
         
            
    return db


            
            


def main(user_input,db):
    if user_input == 1:
        dl.display_items(db)
        
        dl.menu_message()
        main(int(input("Enter a number:")),db)
                

    elif user_input ==2:
        
        print("BORROWING BOOKS")
        
        main_db=borrow(db)
        #print(main_db)
        w.main_overwrite(main_db)
        
        print("You have to return books within 10 days otherewise you will have to pay 5 per day ")

        while True:
            reply = str(input("Do you want to run the program again then Enter 'y' otherewise Enter'n' : ")).lower().strip()
            if reply=="y":
                dl.menu_message()
                main(int(input("Enter a number:")),db)
            else:
                break
            


    elif user_input ==3:        
        print("RETURING BOOKS")
        ids=False
        while ids==False:
            try:
                name=input("Enter your First Name:").lower().strip()
                stu_id=str(int(input("Enter your student id")))
                file4=open(name+stu_id+".txt","r")
                ids=True   
            except:
                print("the student id Invalid ")
                ids=False
                    
        stu=[]
        for i in file4:
            stu.append(i.replace("\n","").split(","))
        #print(stu)    
        print("your borrowed date:"+stu[2][0])
        date=str(datetime.datetime.now())
        print("your return date:"+date)
            
        date_return=int(input("for how many days book is taken"))
        
        if date_return>10:
            total= date_return-10
            print("total amount of fine:"+int(total))
        else:
            print("you have return in time")
    
        main_db=return_books(db)
        w.main_overwrite(main_db)  
            
        while True:
            reply = str(input("Do you want to run the program again then Enter 'y' otherewise Enter'n' : ")).lower().strip()
            if reply=="y":
                dl.menu_message()
                main(int(input("Enter a number:")),db)
            else:
                break
                
                
    else:
        print("Thank you")
        exit()

   
main(user_number,main_db)

def menu_message():
    '''menu message display the massage'''
    print("Enter No.1 to Display book list again?")
    print("Enter No.2 to Borrow the book from libary?")
    print("Enter No.3 to Return the book into libary?")
    print("Enter No.4 to End the program")
 
    

def display_items(list2d):
    '''display items in list'''
    print("S.No.\t\tBook Name\t\tAuthor\t\t\tStock Left\tPrice")
    for i in range(len(list2d)):
        print(i+1,end="\t\t")
        for j in range(len(list2d[i])):
            print(list2d[i][j],end="\t\t")
        print("\n")
            

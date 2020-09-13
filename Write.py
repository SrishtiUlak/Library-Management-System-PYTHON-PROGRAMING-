def main_overwrite(list2d):
    file = open("libary books.txt","w")
    for i in range(len(list2d)):
        counter=1
        for j in range(len(list2d[i])):
            file.write(list2d[i][j])
            if counter<=3:
                file.write(",")
                counter+=1
        file.write("\n")

        

         

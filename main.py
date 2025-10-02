from pathlib import Path 
import os 
def path_file():
    path = Path("")
    files=list(path.rglob('*'))

    for i,files in enumerate(files):
        print(f"{i+1} : {files}")

def create_file():
    try:
        
        print("\nExiceted files\n")

        path_file()

        file__name=input("\nenter  new  file name :-".upper())
        path=Path(file__name)
        if not  path.exists():
           with open(file__name,'x') as f:
             data=input("Write something in this file :-")
             f.write(data)
             print(f"A new file [{file__name}] created ✅".upper())
        else:
           print(f"The file [{file__name}] is all ready exisits :")
    except Exception as creating_error:
        print(f"Opps there is an errror {creating_error}")
    
def read_file():
   try:
     print("\nRead any file from there :\n")
     path_file()

     file_name=input("Which file you :-")
     paht=Path(file_name)
     if  paht.exists() and paht.is_file():
             with open(file_name,'r') as read:
              data=read.read()      
              print(f"\n{data}") 
              print("The file readed succesfully ✅".upper())      
     else:
        print(f"The file {file_name} not exist in our directory")
   except Exception as readEr:
       print(f"There an error acourded {readEr}".upper())
   
def update_file():
   try:
      print("\n Update any file from there:\n")
      path_file()
      file_name=input("Enter the file name :-")
      path =Path(file_name)
   
      if path.exists() and path.is_file():
         print("\npress 1 for appending some cantent in your file ")
         print("press 2 for over writing the data of you ")
         print("press 3 changing the name of your  file")
         work=int(input("Enter  what do you whant to do :-"))
         if work == 1:
             with open(file_name,'a') as fa:
                data=input("Enter the data :-")
                fa.write(data) 
                fa.close()
                print("New data appended succesfully ✅".upper())
         elif work == 2:
            with open(file_name,'w') as fw:
               w_data=input("Enter what do you whant to over-write :-")
               fw.write("  " + w_data)
               print("New data appended succesfully ✅".upper())
               fw.close()

         elif work ==3:
            new_name=input("\nEnter the new name of the file:-")
            p2=Path(new_name)
            path.rename(p2)
            print("The file renamed succesfully ✅".upper())
            
         else:
            print("press Only given options :")     
   
      else:
         print(f"The file {file_name} not exist in our dierctory")
   except Exception as UpdatingEr:
      print(f"There is an error acourd {UpdatingEr}")

def delete_file():
   try:
       print("\n Delete from those files :")
       print("\n")
       path_file()
       delete=input("\nEnter the file name that you whant to delete :-")
       path=Path(delete)
    
       if path.exists() and path.is_file():
          os.remove(delete)
          print("\nOne file deleted successfully..✅".upper())
    
       else:
          print(f"the file {delete} not exist")
   except  Exception as Derr:
      print(f"an error acourd {Derr}")
           

while True:
    print("\n")
    print('______________________________')
    print("press 1 for creating  a  file")
    print("press 2 for reading   a  file")
    print("press 3 for updating  a  file")
    print("press 4 for deletion  a  file")
    print("press 5 for exit")
    print('______________________________')

    try:
      descion=int(input("\ntell me your descion :-".upper()))
    except Exception as descionEr:
       print(f"There an error acourded {descionEr}".upper())
    
    else:
      
        if descion == 1:
          create_file()
      
        elif descion ==2:
           read_file()
      
        elif descion ==3:
           update_file()
        
        elif descion == 4:
           delete_file()
         
        elif descion == 5:
           print("Byee")
           break        
        else:
           print("enter Only given option ".upper())

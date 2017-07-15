def start():
      control=str(input("Are You Admin/Student (A/S):")).upper();
      if control=='A' or control=='ADMIN':
            pass
      elif control=='S' or control=='STUDENT':
            count=0;
            while True:
                  stu_name=str(input("Enter Student Name:"));          
                  if stu_name in name:
                        for i in data_base.keys():
                              if stu_name==i:
                                    stu_password=str(input("Enter password:"));
                                    print(dashed);
                                    break;
                        if stu_password==data_base[stu_name]:
                              s_display;
                  else:
                        print("Student Name not register\n\t(or)\nReEnter the name:");
                        count=count+1;
                        if count==2:
                              print("<<<<<<<<<<Terminate>>>>>>>>>>");
                              break;
                        continue;
                        
                              
      else:
            print("<<<<<<<Enter options only>>>>>>")
            
            
def s_display(stu_name,stu_password):
      if stu_name in  name:
            index=name.index(stu_name);
            print("Name:",name[index],'\tDepartment:',dep[index],'\nYear:',year[index],'\t\tCGPA:',cgpa[index],end='');
      else:
            print(stu_name," is not in the list");
            print(dashed);
           
      
def display():
      'display the operation of admin'
      prompt='''
*******************************************************************
*        1-Create Student Account(C)
*        2-Delete Student Account(D)
*        3-Update Student Details(U)
*        4-Dispaly Student details (S)
*        5-Search Student  Details(T)
*        6-Exit(E)
* 
*******************************************************************
'''
      print(prompt);

def create_std_acc():
      count=0
      print("*********Create Student Account*********\n");
      while True:
            print(end=" ")
            stu_name=str(input('Enter Name:')).upper();
            if stu_name=='':
                   continue
            print(end="\t")
            stu_dept=str(input('Department:'));
            print(end="\t\t ")
            while True:
                  try:
                        stu_year=str(input('Year:'));
                  except ValueError:
                        print("Enter the integer value");
                  break;
                  
            print(end="\t\t  ");
            try:
                  stu_cgpa=str(input('\tCGPA:'));
            except ValueError:
                  stu_cgpa=str(input("CGPA::"));
            v=store(stu_name,stu_dept,stu_year,stu_cgpa);
            print("<------------------------------------------------------------->")
            
            passwd='A'
            while passwd not in ['Y','N']:
                  passwd=input("if you like to set password for this account(Y/N):").upper();
            if passwd=='Y':
                  create_password(stu_name);

            if v:
                  print(dashed)
                  print("\nStudent Account has been Created\n");
                  print(dashed);
                  count=count+1;
                  gogame(count);
            else:
                  print("Your Account not create :")
                  continue
            
            decide='A';
            while decide not in ['Y','N']:
                  decide=str(input("Do you want create another Account(Y/N):")).upper();
                  
            if decide=='Y':
                  continue
            else:
                  break
def gogame(count):
      if count in [2,4,6]:
            choice=str(input("Are you Tired(Y/N):  ")).upper();
            if choice=='Y':
                  print("ok lets go for game")
                  choice1=str(input("1-DragonRealm\n2-Find word"));
                  print(dashed);
                  if choice1=='1' or choice1=='D' or choice=='d':
                        try:
                              import DragonRealm.py;
                        except ImportError:
                              print(dashed);
                              pass
                        
                  elif choice1=='2' or choice1=='F' or choice=='f':
                        try:
                              import findword.py;
                        except ImportError:
                              print(dashed);
                              pass
                              
                              
            else:
                  pass;
            
def store(stu_name,stu_dept,stu_year,stu_cgpa):
      name.append(stu_name);
      dep.append(stu_dept);
      year.append(stu_year);
      cgpa.append(stu_cgpa)
      return True

def create_password(stu_name):
      print("Student Name:"+stu_name);
      password='A';
      while len(password) <=7:
             password=str(input("password:"));
             if len(password)<7:
                   print("Password contain atleast 7 character")
      data_base[stu_name]=password;
      print("This account had been password protected..");

def del_std_acc(admin_password):
      while True:
            stu_name=input('Enter Student Name:').upper();
            for key in data_base.keys():
                  if stu_name==key:
                        print("This student Account is password protected:");
                        password=input("Enter the password:");
                        if data_base[stu_name]==password or admin_password==password:
                              del data_base[stu_name];
                        else:
                              print("password incorrect Try or Enter Admin password")
                              continue
            else:           
                
                  print(stu_name,'Account was deleted')
                  check_account(stu_name);
                  break;
                        
def check_account(stu_name):
         if stu_name in name:
               index=name.index(stu_name);
               del name[index];
               del dep[index];
               del year[index];
               del cgpa[index];

def update_std_acc(admin_password):
      print("********UpdateStudent Details********")
      boolian1=True
      while boolian1:
            password=input("Enter Admin Password:");
            if password==admin_password:
                  stu_name=input("Enter student name to update:").upper();
                  if stu_name in name:
                        index=name.index(stu_name);
                        print("Name:",name[index],'\tDepartment:',dep[index],'\nYear:',year[index],'\tCGPA:',cgpa[index]);
                
                  
                        boolian=True
                        while boolian:
                              update_display();
                              choice='A'
                              while choice not in ['1','2','3','4','5','E','e','N','D','Y','C','n','d','y','c']:
                                    choice=str(input("Enter Your Choice:")).upper()

                              if choice=='1' or choice=='N':
                                    print("*********Update Name*********")
                                    stu_name=str(input('Enter Name:')).upper();
                                    name[index]=stu_name;
                              elif choice=='2' or choice=='D':
                                    print("*******Update Department*****");
                                    stu_dep=str(input("Enter Department"));
                                    dep[index]=stu_dep;
                              elif choice=='3' or choice=='Y':
                                    print("*********Update Year***********");
                                    stu_year=int(input("Enter Year:"));
                                    year[index]=stu_year;
                              elif choice=='4' or choice=='CGPA':
                                    print("*********Update CGPA********")
                                    stu_cgpa=float(input("Enter CGPA"));
                                    cgpa[index]=stu_cgpa;
                        
                              else:
                                    print("Name:",name[index],'\tDepartment:',dep[index],'\nYear:',year[index],'\t\tCGPA:',cgpa[index]);
                                    boolian=False;
                                    boolian1=False;
                        
            else:
                  print("password is incorrect");
                  continue            
                  
def update_display():
      prompt='''
****************************************************
      1-Name(N)
      2-Department(D)
      3-Year(Y)
      4-CGPA(C)
      5-Exit(E)

***************************************************
      '''

      print(prompt);         
def display_database(admin_password):
      password=str(input("Enter the admin password"));
      print("\t\t********Student Database********\n\n")
      if password==admin_password:
            print("Name\t\tDepartment\tYear\tCGPA\tpassword\n");
            length=len(name);
            for i in range(0,length):
                  print(name[i],"\t\t",dep[i],"\t\t",year[i],"\t",cgpa[i],end='\t');
                  
                  for j in data_base.keys():
                        if name[i]==j:
                            print(data_base[j],end='');
            print("\n");     
      
      else:
                  print("password is incorrect:")
            
def  write_file():
      print("Enter the file name");
      try:
            filename=str(input(""));
      except KeyboardInterrupt:
            print("--):   KeyBoard Interrupt")
            filename='student.txt';
      file=open(filename,'w');
      file.write("\t\t**********Student Management System**********\n\n\n")
      file.write(dashed);
      file.write("\nName\tDepartment\tYear\tCGPA\tpassword\n");
      file.write(dashed);
      
      for i in range(0,len(name)):
            file.write(name[i]);
            file.write('\t');
            file.write(dep[i]);
            file.write('\t\t');
            file.write(year[i]);
            file.write('\t');
            file.write(cgpa[i]);
            if name[i]==data_base.keys():
                  file.write(data_base[name[i]])
            file.write('\n\n')
            
      file.close();

def search_stu_acc():
      while True:
            stu_name=str(input("Enter name to search details:")).upper();
            if stu_name in  name:
                  index=name.index(stu_name);
                  print("Name:",name[index],'\tDepartment:',dep[index],'\nYear:',year[index],'\tCGPA:',cgpa[index]);
                  break;
            else:
                  print(stu_name," is not in the list");
                  break;
            print(dashed);
            
            
      
def store_admin(admin_name,admin_password):
      try:
            file=open("admin.txt",'w');
      except :
            file_name=str(input("Enter file name to store the Admin details"));
            file=open(filename,'w');
      file.write(admin_name);
      file.write("\n");
      file.write(admin_password);
      file.close();

def read_admin():
      file=open("admin.txt",'r');
      name=file.readlines(1);
      namee=file.readlines(2)
      a_name=name[0];
      admin_password=namee[0];
      admin_name=a_name[0:len(a_name)-1]
      print('AdminName:',admin_name,'\npassword:',admin_password);
      file.close();
      return admin_name,admin_password;  
      
def   admin_acc():
      print(dashed)
      admin_name=str(input("Enter Admin Name  :"));
      choice1=True;
      while choice1:
            admin_password=str(input("Enter Admin password  :"));
            if len( admin_password)<=7:
                  print("Enter password atleast 7 character..."); 
                  continue
            else:
                  break;
     
      return admin_name,admin_password;

def main():
      'main function control all of them'
      print("\t\t********Student Management System********\n\n\n");

      start();
      while True:
            c=str(input("You already have admin account(Y/N):"));
            if c=='Y' or c=='y':
                  admin_name,admin_password=read_admin();
                  break;
            else:
                  admin_name,admin_password=admin_acc();
                  break;
      print(dashed);
                  
      store_admin(admin_name,admin_password)
      choice=True;
      while choice:
            display();
            cmd='A'
            while cmd not in ['1','2','3','4','5','6','t','T','C','D','U','S','E','e','s','c','d','u']:
                  cmd=str(input("Enter option:"));

            if cmd=='1' or cmd=='c' or cmd=='C':
                  'Call create student account function'
                  create_std_acc();
                  print(dashed);
            elif cmd=='2' or cmd=='D' or cmd=='d':
                  'Call delete student account function'
                  del_std_acc(admin_password);
            elif cmd=='3' or cmd=='U' or cmd=='u':
                  update_std_acc(admin_password);
            elif cmd=='4' or cmd=='S' or cmd=='s':
                  display_database(admin_password);
            elif cmd=='5' or cmd=='T' or cmd=='t':
                  search_stu_acc();
            elif cmd=='6' or cmd=='E' or cmd=='e':
                  write_file()
                  print("All details are stored in the form of documentation:");
                  choice==False;
                  break;
      input();

#************************************************************************************************************
                                                #MAIN FUNCTION
#********************************************************************************************************
      
'Declear the global variables'
data_base={};
name=[];
dep=[];
year=[ ];
cgpa=[ ];
dashed='*' * 67;
main();

      
            
            
                  

                  
                  
                  
                  
                  
            
                  

                  
                  
                  

      
      
      


      

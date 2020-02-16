import sqlite3
import sys

class healthcare:
    def __init__(self):
        self.conn = sqlite3.connect('HealthCare.db')
        self.cur = self.conn.cursor()

        self.name = ""
        self.age = ""
        self.gender = ""
        self.height = ""
        self.weight = ""
        self.city = ""
        self.usrid = ""
        self.usrpass = ""
        self.usr_id = ""
        self.usr_pass = ""
        self.loc = 0
        self.L = []
        self.flag = 0
        

    def create_table(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS LoginDetails (Name TEXT, Age NUMERIC, Gender TEXT, Height NUMERIC, Weight NUMERIC, City TEXT, Loginid TEXT, Password TEXT)')

    def dynamic_data_entry(self,c,d,e,f,g,h,i,j):
        self.cur.execute("INSERT INTO LoginDetails(Name, Age, Gender, Height, Weight, City, Loginid, Password) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",(c,d,e,f,g,h,i,j))
        self.conn.commit()

    def symptoms_search(self,s):
        self.cur.execute("SELECT * FROM Symptoms ")
        data = self.cur.fetchall()
        
        for i in range (len(data)):
            if s in data[i][0]:
                self.loc = i
                self.L.append(self.loc)
                self.flag = 1
                
            

        if self.flag==1:
            print("symptoms\t\tYou may have\t\tRecommended medicines")

            print(s+"\t\t"+data[self.L[0]][1]+"\t\t"+data[self.L[0]][2])
            
            for i in range(1,len(self.L)):
                print("        "+"\t\t"+data[self.L[i]][1]+"\t\t"+data[self.L[i]][2])
            
        else:
            print("No severe symptom. A simple bed rest is recommended!")

    def get_data(self):
        print("CareTalk")
        print("\t\tSay it with Health!")
        print("1.Login\n2.Create account")
        login_options= {
                1:'Login',
                2:'Create account'
        }
        ch=int(input('PLease enter your choice:'))
        if ch==1:
            print("........LOGIN........")
            self.usr_id = input('User ID : ')
            self.usr_pass = input('password : ')
            self.login(self.usr_id,self.usr_pass)
        elif ch==2:
            print("Please enter following details")
            self.name=input('Name:')
            self.age=int(input('Age:'))
            self.gender=input('Gender:')
            self.height=float(input('Height:'))
            self.weight=float(input('Weight:'))
            self.city=input('city:')
            self.usrid=input('Create User ID:')
            self.usrpass=input('Create Password:')
            self.create_table()
            self.dynamic_data_entry(self.name,self.age,self.gender,self.height,self.weight,self.city,self.usrid,self.usrpass)
            print("\nAccount created successfully!")
            self.get_data()
    
    def login(self,usr_id,usr_pass):
        self.cur.execute("SELECT * FROM LoginDetails ")
        data = self.cur.fetchall()
        
        for i in range(len(data)):
            if data[i][6] == usr_id and data[i][7] == usr_pass:
                flag = 1
                break
            else:
                flag = 0
        if flag==1:
            print("Login Successfull")
            self.logged_in()
        else:
            print("Username or Password Incorrect")


    def logged_in(self):
        while(True):
            print("")
            print("Welcome to CareTalk")
            print("\n\nSelect What you want to do.")
            print("1.Chat with doctor.\n2.How are you feeling today?\n3.calculate your BMI.\n4.Your Profile.\n5.Logout")
            performance_options={
                1:'Chat with Doctor',
                2:'How are you feeling today?',
                3:'Calculate your BMI',
                4:'Your Profile',
                5:'Logout'
            }
            ch=int(input('please enter your choice:'))
            if ch==1:
                print("Please select your city or nearest city")
                print("a.Mumbai.\nb.Pune>\nc.Gujrat>\nd.Chennai\ne.Nashik.")
                city_options={
                    1:'Mumbai',
                    2:'Pune',
                    3:'Gujrat',
                    4:'Chennai',
                    5:'Nashik'
                }
                ch1=str(input(print('Enter your choice:')))
                if ch1==1:
                    print("Select the hospital")
                    print("1.Hinduja Hospital\n2.Nanavati hospital.\n3.Ruby Hospital\n4.Fortis Hospital.\n5.KEM Hospital.")
                    Hospital_options = {
                    1:'Hinduja Hospital',
                    2:'Nanavati HOspital',
                    3:'Ruby Hospital',
                    4:'Fortis Hospital',
                    5:'KEM Hospital', }
                    int(input(print('Enter your choice:')))
                elif ch1==2:
                    print("Select the hospital")
                    print("1.Sancheti Hospital.\n2.Oasis Hospital.\n3.Noble Hospital.\n4.Jupiter Hospital.\n5.Phoenix Hospital"),
                    Hospital_options1={
                    1:'Sancheti Hospital.',
                    2:'Oasis Hospital.',
                    3:'Noble Hospital.',
                    4:'Jupiter Hospital.',
                    5:'Phoenix Hospital'}
                    int(input(print('Enter your choice:')))
                elif ch1==3:
                    print("Select the Hospital")
                    print("1.Zydus Hospital\n2.Icon Hospital\n3.Wings Hospital\n4.Max Hospital\n5.Unity Hospital"),
                    Hospital_options2={
                    1:'Zydus Hospital',
                    2:'Icon Hospital',
                    3:'Wings Hospital',
                    4:'Max Hospital',
                    5:'Unity Hospital'}
                    int(input(print('Enter your choice:')))
                elif ch1==4:
                    print("Select the hospital")
                    print("1.SIMS Hospital.\n2.Trimed Hospital\n3.Saraswathy Hospital.\n4.ProMed Hospital.\n5.Apollo Hospital."),
                    Hospital_options3={
                    1:'SIMS Hospital.',
                    2:'Trimed Hospital',
                    3:'Saraswathy Hospital.',
                    4:'ProMed Hospital',
                    5:'Apollo Hospital.'}
                    int(input(print('Enter your choice:')))
                else:
                    print("Select the hospital")
                    print("1.Mercury Hospital.\n2.Apex Hospital.\n3.Civil Hospital.\n4.SMBT Hospital.\n5.Wockhard Hospital."),
                    Hospital_options4={
                    1:'Mercury Hospital.',
                    2:'Apex Hospital.',
                    3:'Civil Hospital.',
                    4:'SMBT Hospital.',
                    5:'Wockhard Hospital.'}
                    int(input(print('Enter your choice:')))
                    k=chr
            if ch==2:
                print("How are you feeling today?")
                input('Body temperature(approximate):')
                bmi=float(input('BMI:'))
                k=str(input('Symptoms:'))
                print("Your report is!!!")
                print("Name:",self.name)
                self.symptoms_search(k)

            if ch==3:
                METER=100
                height = float(input("Enter your height in Centimeters: "))
                weight = float(input("Enter your weight in Kg: "))
                temp = height / METER
                bmi = weight / (temp * temp)
                print("Your Body Mass Index is: ", bmi)
            if ch==4:
                
                self.cur.execute("SELECT * FROM LoginDetails ")
                data = self.cur.fetchall()
                for i in range (len(data)):
                    if data[i][6]==self.usr_id:
                        self.loc = i
                        break
                print("******Profile******"+"\n")
                print("Name : "+data[self.loc][0])
                print("Age : ",data[self.loc][1])
                print("Gender : "+data[self.loc][2])
                print("Height :",data[self.loc][3])
                print("Weight :",data[self.loc][4])
                print("City :"+data[self.loc][5])
                print("User ID"+data[self.loc][6])
                

            if ch==5:
                print("Are you sure?")
                exit_options={
                        1:'Yes',
                        2:'No'
                }
                print(exit_options)
                exit_ch = int(input('Enter your choice:'))
                if exit_ch==1:
                    self.get_data()
                    break

health = healthcare()
health.get_data()



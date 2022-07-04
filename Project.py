class Clerk:
    def create(self):
        self.uid=int(input("enter the id:"));
        self.name=input("enter the name:");
        self.age=int(input("enter the age:"));
        self.salary=25000;
        self.desig="Clerk";
    def display(self):
        print("..........................................")
        print("ID:",self.uid);
        print("Name:",self.name);
        print("Age:",self.age);
        print("Salary:",self.salary);
        print("Designation:",self.desig);
    def raisesalary(self):
        print("..........................................")
        old=self.salary;
        self.salary=old+(old*5/100);
        print("Raised Salary:",self.salary);
    def options(self):
        print("..........................................")
        print("Choose the below Option number to perform the certain task");
        print("1.Create")
        print("2.Display")
        print("3.Raise Salary")
        print("4.exit")

class Manager:
    def create(self):
        self.uid=int(input("enter the id:"));
        self.name=input("enter the name:");
        self.age=int(input("enter the age:"));
        self.salary=80000;
        self.desig="Manager";
    def display(self):
        print("..........................................")
        print("ID:",self.uid);
        print("Name:",self.name);
        print("Age:",self.age);
        print("Salary:",self.salary);
        print("Designation:",self.desig);
    def raisesalary(self):
        print("..........................................")
        old=self.salary;
        self.salary=old+(old*20/100);
        print("Raised Salary:",self.salary);
class Tester:
    def create(self):
        self.uid=int(input("enter the id:"))
        self.name=input("enter the name:");
        self.age=int(input("enter the age:"));
        self.salary=40000;
        self.desig="Tester";
    def display(self):
        print("..........................................")
        print("ID:",self.uid);
        print("Name:",self.name);
        print("Age:",self.age);
        print("Salary:",self.salary);
        print("Designation:",self.desig);
    def raisesalary(self):
        print("..........................................")
        old=self.salary;
        self.salary=old+(old*10/100);
        print("Raised Salary:",self.salary);
class Developer:
    def create(self):
        self.uid=int(input("enter the id:"));
        self.name=input("enter the name:");
        self.age=int(input("enter the age:"));
        self.salary=60000;
        self.desig="Developer";
    def display(self):
        print("..........................................")
        print("ID:",self.uid);
        print("Name:",self.name);
        print("Age:",self.age);
        print("Salary:",self.salary);
        print("Designation:",self.desig);
    def raisesalary(self):
        print("..........................................")
        old=self.salary;
        self.salary=old+(old*15/100);
        print("Raised Salary:",self.salary);
c=Clerk();
m=Manager();
t=Tester();
d=Developer();
counter=0;
print("Choose the below Option number to perform the certain task");
print("1.Create");
print("2.Display");
print("3.Raise Salary");
print("4.exit");

while True:
    counter+=1;
    n=int(input("enter your choice number:"));
    if(n==1):
        print("1.Clerk");
        print("2.Manager");
        print("3.Tester");
        print("4.developer");
        n1=int(input("choose the option number to create:"));
        if(n1==1):
            print("enter the clerk details")
            c.create();
            c.options()
            
            
        elif(n1==2):
            print("enter the Manager details")
            m.create();
            c.options()
            
           
        elif(n1==3):
            print("enter the Tester details")
            t.create();
            c.options()
            
        elif(n1==4):
            print("enter the Developer details")
            d.create();
            c.options()
            
            
        else:
            print("wrong selection......:(");
            
        
    if(n==2):
        print("1.Clerk");
        print("2.Manager");
        print("3.Tester");
        print("4.developer");
        n2=int(input("choose the option number to display:"));
        if(n2==1):
            print("clerk details")
            c.display();
        elif(n2==2):
            print("Manager details")
            m.display();
        elif(n2==3):
            print("Tester details")
            t.display();
        elif(n2==4):
            print("developer details")
            d.display();
        else:
            print("wrong option")
        c.options()
        
    if(n==3):
        print("1.Clerk");
        print("2.Manager");
        print("3.Tester");
        print("4.developer");
        n3=int(input("choose the option number to Raise salary of:"));
        if(n3==1):
            print("clerk")
            c.raisesalary();
        elif(n3==2):
            print("Manager")
            m.raisesalary();
        elif(n3==3):
            print("Tester")
            t.raisesalary();
        elif(n3==4):
            print("developer")
            d.raisesalary();
        else:
            print("wrong option")
        c.options()
        
    if(n==4):
        print("thank you.....:)");
        break
        

       

class staff:
    def code_name(self):
        self.name=input("Enter the name : ")
        self.code=int(input("Enter the code :"))
        print("Name : ",self.name)
        print("code : ",self.code)              
                      
class teacher(staff):
    def subject(self):
        self.subject="Maths"
        print("Subject : ",self.subject)
    def publication(self):
        self.publication="Arihant"
        print("Publication : ",self.publication)
    def display_teacher(self):
        self.code_name()
        self.subject()
        self.publication()

class typist(staff):
    def speed(self):
        self.speed=60
        print("Speed in(words per minute): ",self.speed)
        
class officer(staff):
    def grade(self):
        self.grade="A"
        print("Grade : ",self.grade)
    def display_officer(self):            
        self.code_name()
        self.grade()

class regular(typist):
    def salary(self):
        self.salary=12000
        print("Salary : ",self.salary)
    def display_regular(self):
        self.code_name()
        self.salary()
        self.speed()

class casual(typist):
    def daily_wages(self):
        self.salary=200 
        print("Salary per hour : ",self.salary)
    def display_casual(self):
        self.code_name()
        self.daily_wages()
        self.speed()


while True:
    print("Enter choice")
    print("1.Teacher")
    print("2.Officer")
    print("3.Regular Typist")
    print("4.Casaul typist")
    print("5.Exit")
    choice = int(input("Enter the number : "))
    if choice == 1:
        c1 = teacher()
        c1.display_teacher()
    if choice == 2:
        c1 = officer()
        c1.display_officer()
    if choice == 3:
        c1 = regular()
        c1.display_regular()
    if choice == 4:
        c1 = casual()
        c1.display_casual()
    if choice == 5:
        print("EXIT")
        break        
        
    
        
    
        
                      

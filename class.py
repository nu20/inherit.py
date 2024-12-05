class person( object ) :
    def __init__(self , name , idnumber) :
       self.name = name
       self.idnumber = idnumber
    def display(self) :
        print(self.name)
        print(self.idnumber)

class employe(person) :
    def __init__(self , name , idnumber , post , salary) :
        self.salary = salary
        self.post = post
        person.__init__(self , name , idnumber)

a = employe('rahul' , 88012 , 'intern' , 4335)
a.display()
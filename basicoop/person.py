class Person:
    def __init__(self,name,gender,profession) -> None:
        self.name = name
        self.gender = gender
        self.profession = profession
        self.study = 0
        
   
    def work(self):
        print(f'{self.name} working as a {self.profession}')
    
    def study(self,hours):
        self.study = hours
   
    def show(self):
        print(f'Name:{self.name} Gender:{self.gender} Profession:{self.profession} Study:{self.study}')
        

#person1
jessa = Person('Jessa','Female','Software Engineer')
jessa.work()
jessa.show()

#person2
jon = Person('Jon','male','Doctor')
jon.work()
jon.study = 15
jon.show()

#person3
Lisa = Person('Lisa','Female','Korean Singer')
Lisa.study = 10
Lisa.work()
Lisa.show()

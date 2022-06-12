class Person:
    def __init__(self,name:str,gender:str,profession:str,study:str) -> None:
        self.name = name
        self.gender = gender
        self.profession = profession
        self.study = study
        
   
    def work(self):
        print(f'{self.name} working as a {self.profession}')
    
    
   
    def show(self):
        print(f'Name:{self.name} Gender:{self.gender} Profession:{self.profession} Study:{self.study}')
        

#person1
jessa = Person('Jessa','Female','Software Engineer',0)
jessa.work()
jessa.show()

#person2
jon = Person('Jon','male','Doctor',15)
jon.work()
jon.show()

#person3
Lisa = Person('Lisa','Female','Korean Singer',10)
Lisa.work()
Lisa.show()

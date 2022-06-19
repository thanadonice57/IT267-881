class Student:
    def __init__(self,id:str,name:str,major="IT") -> None:
        self.id = id
        self.name = name 
        self.major = major
        
    def printdisplay_detail(self):
        print(f"Id: {self.id}")
        print(f"Name: {self.name}")
        print(f"Major: {self.major}")
        
    def __del__(self):
        print("Object was destroyed")
        
if __name__ == "__main__":
    
    #Jessica
    Jessica = Student("111","jessica","IT")
    Jessica.printdisplay_detail()
    
    #John
    John = Student("112","John","MKT")
    John.printdisplay_detail()
    
    James = Student("113","james",)
    James.printdisplay_detail()
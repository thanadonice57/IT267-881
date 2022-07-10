
class Horse:
    def __init__(self,max_height,name,color,age,weight) -> None:
        super().__init__()
        self.max_height = max_height
        self.name = name
        self.color = color
        self.age = age 
        self.weight = weight
    def run(self,runn):
        self.run = runn
        print(f'{self.run} Khan Khan is running')
        
    def show_name(self):
        print(f'{self.name} Khan Khan')
        
    def show_info(self):
        print('***** Mumu Info*****')
        print(f'Name:{self.name}')
        print(f'Color:{self.color}')
        print(f'Max height:{self.max_height}')
        print(f'Age:{self.age}')
        print(f'Wehight:{self.weight}')
    
    
       
    
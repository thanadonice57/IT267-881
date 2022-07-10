
class Donkey:
    def __init__(self, max_height, name, color, age, weight) -> None:
        self.max_height =max_height
        self.name = name
        self.color = color
        self.age = age
        self.weight = weight
        
        
        
    def sound(self):
        print(f'Donkey Makes eeyore sound')
        
    def show_info(self):
        print(f"*****Meme Info*****")
        print(f'Donkey Makes eeyore sound')
        print(f'Name:{self.name}')
        print(f'Color:{self.color}')
        print(f'Max height:{self.max_height}')
        print(f'Age:{self.age}')
        print(f'Wehight:{self.weight}')
    
        
        
        
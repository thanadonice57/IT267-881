
class Mule:
    def __init__(self) -> None:
        pass
    def run(self):
        print(f'Mule is running')
    def show_info(self):
        pass
    
from horse import Horse  
mule1 = Horse(200,'Mumu ','Blue-eyed cream',3,200)
mule1.show_info()

from donkey import Donkey
mule2 = Donkey(200,'Meme','Palomino',1,120.7)
mule2.show_info()


    

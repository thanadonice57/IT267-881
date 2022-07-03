class Area:
    
    def __init__(self) -> None:
        self.__base = 0
        self.__high = 0
    
    @property #getter ของ base
    def base(self):
        return self.__base
    
    #setter ของ base
    @base.setter
    def base(self,value):
        self.__base = value
        
    @property #getter ของ high
    def high(self):
        return self.__high
    
    #setter ของ high
    @high.setter
    def high(self,value):
        self.__high = value #self.high = value
        
    def compute_aera(self):
        return 0.5 * self.base * self.high
      #return 0.5 * self__base * self.__high
        
    
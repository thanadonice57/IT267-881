class Account:
    def __init__(self) -> None:
        self.acc_type = ''
        self.acc_no = ''
        self.acc_balance = 0
        
    
    def open_account(self,acc_name,acc_type,acc_no,acc_balance=100):
        self.acc_name = acc_name
        self.type = acc_type
        self.acc_no = acc_no
        self.acc_balance = acc_balance
        
    
    def display_balance(self):
        return f'{self.acc_name} has {self.acc_balance} baht'
    
    
    
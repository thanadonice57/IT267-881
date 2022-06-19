class Item:
    def __init__(self,name:str,price:float,quantity = 1) -> None:
        #ตรวจสอบ price,quantity ว่าต้อง > 0
        assert price > 0,f"Price {price} must great than 0"
        assert quantity > 0,f"Quanyiyt {quantity} must great than 0"
        
        self.name = name
        self.price = price
        self.quantity = quantity
        
        
    #instance method ต้องมีคำว่า self เสมอ
    #จะเรียกใช้ method นี้ได้ต้องมีการสร้าง oblect
    def total_price(self):
        return self.price * self.quantity
    
    def __del__(self):
        print("Object was destroyed")
        
if __name__ == "__main__":
    item1 = Item("Monitor",5600,)
    item2 = Item("Mouse",1500,2)
    print("=== Total Price ===")
    print(f"{item1.name} : {item1.total_price():,.2f} : {item1.quantity}")
    print(f"{item2.name} : {item2.total_price():,.2f} : {item2.quantity}")
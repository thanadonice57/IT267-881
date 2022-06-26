#เรียกใช้ package เพื่อเข้าถึงคลาส Customer, Account
from bank.account import Account
from bank.customer import Customer


#สร้าง object ของ customer ที่ชื่อ Paul
paul = Customer()
paul.new_customer()

#สร้าง object ของ account เพื่อเปิดบัญชีใหม่ให้กับ Paul
paul_acc = Account()
paul_acc.open_account(paul.name,'Saving','0123-4578',500)


#แสดง ข้อมูลของ customer Paul
print(paul.cus_info())

#แสดงข้อมูลเงินควเหลือในบัญชีของ Paul
print(paul_acc.display_balance())

    
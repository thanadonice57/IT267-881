#สร้างพนักงานแผน IT
from empit import EmpIT

mike = EmpIT('001','Mike','60000')
mike.add_skill('Python,JavaScript')
mike.add_experience(5)
mike.emp_detail()
mike.it_salary()

#สร้างพนักงานแผน MKT
from empmkt import EmpMKT
Anna = EmpMKT('002','Anna','35000')
Anna.emp_detail()
Anna.mkt_salary()

#Jess 003 เงินเดือน 45000 ทำวานอยู่ที่ chiang Mai ได้คอมมิชชั่น35%
Jess = EmpMKT('003','Jess',45000)
Jess.add_location('Chiang Mai')
Jess.add_commission(35)
Jess.emp_detail()
Jess.mkt_salary()

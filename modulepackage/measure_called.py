#วิธีที่1
from measure import Measure

if __name__ == '__main__':
    mobj = Measure()
    #ให้ user เลือกได้ว่าต้องการแปลงค่าเป็น inch หรือ cm
    choice = input('Choose menu (1:inch, 2:cm):')
    #รับค่าตัวเลขจาก user ได้
    number = float(input('Enter number'))
    
    if choice == '1':
        print(f'{number} cm = {mobj.cm_inch(number):.2f} inch')
    elif choice == '2':
        print(f'{number} inch = {mobj.inch_cm(number):.2f} cm')
    else:
        print('Choose wrong menu')
    
    
    #print(f' cm = {mobj.cm_inch():.2f} inch')
    #print(f' cm = {mobj.inch_cm():.2f} cm')
    


    
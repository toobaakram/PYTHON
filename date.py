def date():
    a=input("Enter date : ")
    if a[-2]== 'A':
        print(a)
    else:
        b=int(a[0:2])+12
        str(b)
        print(b,a[2:8])
        
date()

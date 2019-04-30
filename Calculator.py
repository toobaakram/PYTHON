def calc():
    a = int(input("Enter 1 Number :"));
    b = int(input("Enter 2 Number :"));
    c = int(input("Enter Any Operation , 1 for addition ,2 sub , 3 mult , 4  for div"));

    if (c==1) :
        print(a+b);
    elif (c==2) :
        print("The Answer Of Subtraction Is :" +str(a) + "-" +str(b) +" = " +str(a-b));
    elif (c==3) :
        print(a*b);
    elif (c==4) :
        print(a/b);
    else :
        print("Select Correct Option");


def again():
    d=input("If you want to continue or not to continue please press Y or N");
    if(d == 'Y'):
        calc();
    else :
        exit();
  

calc();
again();


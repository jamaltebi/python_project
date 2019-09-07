import sys

class CalculError(Exception) : # exception of Error  
    "class for Exception Error"
class Calculator:

    def add(self,a,b):
        return a+ b


    def sub(self, a , b):
        return a-b


    def div(self,a,b):
        try:
            return a / b
        except  ZeroDivisionError :
            raise CalculError("impossible to devide  zero(0)")



if __name__ == '__main__' :

    print("option of Operation")
    calc_objt = Calculator()
    operation_option = [
        calc_objt.add,
        calc_objt.sub,
        calc_objt.div
    ]
    
    while True :
        for c, operation in enumerate(operation_option,1):
            print("{}.{}".format(c,operation.__name__))

        print("q.Quit")
        ope= input("enter your operation to test : \n")
        if ope == "q":
            print("bye")
            sys.exit()
        while int(ope) > c :
            ope= input("enter a valid choice: \n")
    
        a=float(input("enter the number a \n"))
        b=float(input("enter the number b \n"))

        ###call operation to test#####
        op=int(ope)-1    # list begin with 0 , we dont have zero as choice
        try :

            print("the result is :\n",operation_option[op](a,b))

        except CalculError as err:
            print(err)
            
            b=float(input("enter  number > 0 \n "))
            while b<=0 :
                b=float(input("enter  number > 0 \n "))

            print("the result is :\n",operation_option[op](a,b))
        
        print("=============================================")

    


#print add two numbers
def numEnter():
    while 1==1:
        print('enter a number')
        num = input()
        try:
            if type(int(num)) == int:
                return num
                break
        except:
            print('you have to enter a number only')
       

num1 = numEnter()
num2 = numEnter()
print(num1 + '+' + num2 + '=' + str(int(num1)+int(num2)))


'''
Multiples
Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.

Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.
'''

def multiples_partI(num):
    for i in range(0,num):
        if (i%3==1):
            print i

multiples_partI(1001)


def multiples_partII(num):
    for i in range(0,num):
        if (i%5==1):
            print i

multiples_partII(1000001)

'''
Sum List
Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
'''

def badd():
    r=[1, 2, 5, 10, 255, 3]

    for i in range(0,len(r)):
        
        total=r[0]+r[1]+r[2] +r[3]+ r[4] + r[5] 
        print total
        break
badd()




'''
Average List
Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
'''
def average():
    a = [1, 2, 5, 10, 255, 3]
    for i in range(0,len(a)):
        total=0
        total=(a[0]+a[1]+a[2] +a[3]+ a[4] + a[5])/6
        print total
        break
average()


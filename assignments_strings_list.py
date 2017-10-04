'''
Find and Replace
In this string: words = "It's thanksgiving day. It's my birthday,too!" print the position of the first instance of the word "day". Then create a new string where the word "day" is replaced with the word "month".
'''

words="It's thanksgiving day. It's my birthday too!"
print words
print words.find("day")

print words
print words.replace("day","month")

'''
Min and Max
Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.
'''
x = [2,54,-2,7,12,98]
print min(x)
print max(x)

'''
First and Last
Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the first and last values in the original list. Your code should work for any list.

'''
y = ["hello",2,54,-2,7,12,98,"world"]

if y[0]:
   print y[0]

if y[7]:
   print y[7]

   '''
   New List
Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!
   '''

z = [19,2,54,-2,7,12,98,32,10,-3,6]

z.sort()
v=[z[0],z[1],z[2],z[3],z[4]]
e=[z[5],z[6],z[7],z[8],z[9],z[10]]
for i in range(0, len(z)):
    if z[i] != -1:
       print '[','[', z[0],z[1],z[2],z[3],z[4],']',z[5],z[6],z[7],z[8],z[9],z[10],']'
       break
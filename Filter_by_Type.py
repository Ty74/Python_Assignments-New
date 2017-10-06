
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

print "Integer If the integer is greater than or equal to 100, print 'That's a big number!" "If the integer is less than 100, print That's a small number"
def filter_by_type(num):
      if num>=100:
          print "That's a big number"
      else:
          print "That's a small number"
              
   
filter_by_type(mI)
print 'String If the string is greater than or equal to 50 characters print "Long sentence." If the string is shorter than 50 characters print "Short sentence."'


def long_and_short(sS):   
   r= sS.split()
   
   for i in range(0,len(r),1):
       total=0
       total=i+1
       if total>=50:
          print "long Sentence"
       elif total<=50:
          print "short Sentence"
          break  
long_and_short(sS)


def long_and_shortII(bS):  
    p=bS  
    for q in range(len(p),0,-1):
        
        if q>=50:
           print "Long Sentence"
           break
        
long_and_shortII(bS)



print 'List If the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values print "Short list.'
def equal_greater_10():
    ten=[1,2,3,4,5,6,7,8,9,10]
    five=[1,2,3,4,5]

    for i in ten: 
        if i>=10:
            print "Big List"
            
    for i in five:
        if i<=10:
            print "Short List"
            break

equal_greater_10()

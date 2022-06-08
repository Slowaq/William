num_of_dig=[]
counted_dig=[]
num_of_dig1=[]
seq_in_dig=[]
previous, current = 0, 1
previous1, current1 = 0, 1

"""
Finding the nth number of fibonacci series
"""
##while True:
##    def fib_seq(n):
##       for _ in range(2,n):
##            previous,current=current,previous+current
##
##        return current
##    nput = int(input("please enter desired n-th number of Fibonacci sequence: "))
##    print(fib_seq(nput))


print("-------------- \nExample of Fibonacci Series \n--------------")
for _ in range(2,21):       #counting number of digits in each number
    previous1,current1=current1,previous1+current1
    print(current1-previous1,"+",previous1,"=", current1)
    current1_str=str(current1)
    #print(current1,"=",len(current1_str))
    num_of_dig1.append(len(current1_str))
print("...")

print("\n-------------- \nCounting Digits in Each Number \n--------------")
print("1 1 1 1 1|2 2 2 2 2|3 3 3 3 3|4 4 4 4 ...")

for _ in range(2,1000):       #counting number of digits in each number
    previous,current=current,previous+current
    #print(current-previous,"+",previous,"=", current)
    current_str=str(current)
    #print(current,"=",len(current_str))
    num_of_dig.append(len(current_str))
    #print(*num_of_dig, sep = ",")


print("\n-------------- \nCounting Quantity of Identical Number of Digits \n--------------")
for i in range(0,63):        #looking for a pattern in number of digits in a number
    counted_dig.append(num_of_dig.count(1+i))
print("5, 5, 5, 4, 5, 5, 5, 4, 5, 5, 5, 5, 4 ...") # the same as print in line 46 but with fewer elements
#print(*counted_dig, sep = ", ")


print("\n-------------- \nLooking For Repeating Pattern \n\nWhere: #-count of ""5"" \n       ""|""-represents ""4""          \n--------------")
e=-1

if counted_dig[0] == 5:
    e+=1

for u in range(0,62):
    if counted_dig[u] == 5 and counted_dig[u+1] == 5:
        e+=1
            
    elif counted_dig[u] == 5 and counted_dig[u+1] == 4:
        e+=1
        
    elif counted_dig[u] == 4:
        seq_in_dig.append(e)
        seq_in_dig.append("|")
        e=0
        
print(*seq_in_dig,"...")
    
    

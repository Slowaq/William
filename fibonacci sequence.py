num_of_dig=[]
counted_dig=[]
previous, current = 0, 1

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


for _ in range(2,299):       #counting number of digits in each number
    previous,current=current,previous+current
    #print(current-previous,"+",previous,"=", current)
    current_str=str(current)
    #print(current,"=",len(current_str))
    num_of_dig.append(len(current_str))
    #print(*num_of_dig, sep = ",")

for i in range(0,63):        #looking for a pattern in number of digits in a number
    counted_dig.append(num_of_dig.count(1+i))
    print(*counted_dig, sep = ",")
    
    
    

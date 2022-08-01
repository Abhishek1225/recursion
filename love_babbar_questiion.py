##if we have 412 and we have to print "Four","one","Two"..


def sayDigit(n,Arr):
//base cases
    if n==0:
        return
    else:
        digit = n%10
        n = n//10
         recursive call
        return sayDigit(n,Arr)
        print(Arr[digit])
        
        
        
        
        
##drier code

n = int(input())
Arr = ["zero","one","Two","three","four","five","six","seven","eight","Nine"]
sayDigit[n,Arr]
 return 0       

 

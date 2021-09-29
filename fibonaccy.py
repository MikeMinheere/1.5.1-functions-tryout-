def FibReeks(n):  
   if n <= 1:  
       return n  
   else:  
       return(FibReeks(n-1) + FibReeks(n-2))  
cijfer = int(input("hoeveel keer wilt u een Fibonacci nummer zien? "))
  
if cijfer <= 0:
   print("type alstublieft een positief nummer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(cijfer):  
       print(FibReeks(i))
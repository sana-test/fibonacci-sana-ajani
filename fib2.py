numTerms = int(input("How many terms of Fibonacci sequence to print? "))

def fibonnaci(n):
   if n <= 1:
       return n
   else:
       return(fibonnaci(n-1) + fibonnaci(n-2))

# check if the number of terms is valid
if numTerms <= 0:
   print("Please enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(numTerms):
       print(fibonnaci(i))

         

#Function takes in a number input and will return a list of all even numbers between 0 and that number (inclusive)
def evenNumbers(num):
  i = 0
  output = []

  #While loop will go through every number
  while i <= num:
        #If the number is even then it will be added to the output variable (even number / 2 will have no remainder)
        if i % 2 == 0:
            output.append(i)
        i = i + 1
  return output
            
            
            
        

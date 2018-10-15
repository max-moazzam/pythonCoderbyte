#Function takes in a number as a parameter and returns the factorial of that number
def FirstFactorial(num):

  #Converts parameter into an integer
  num = int(num)
  #Creates a factorial variable that will be returned
  factorial = 1

  #While loop will keep multipying a number to the number 1 less than it until 1 is reached
  while num > 1:
    factorial = factorial * num
    num = num - 1
  return factorial
  
#May need to change to raw_input to just input depending on which version of Python used
print(FirstFactorial(raw_input()))

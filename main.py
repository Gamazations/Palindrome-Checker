#Imports OS
import os

binaryOrPalindrome = input('Would you like to do binary or palindromes? ')

if binaryOrPalindrome == "palindrome" or binaryOrPalindrome=="Palindrome":
    #Prints a statement explaining what a palindrome is
  print('A palindrome is just a word that reads the same backwards and forwards.')
  
  #Creates a function used to see if a name is a palindrome
  def questionTwo(nameInput):
    
    #Sets the input of the name to all lowercase 
    nameInput = nameInput.lower()
    #Finds the length of nameInput
    length = len(nameInput)
  
    #if length is less than 2, it will automatically set it to true as a palindrome
    if length < 2: 
      return True
  
    #Checks to see if within the input of the first character (nameInput[0]) and the last character (nameInput[length - 1]) are equal to the same
    elif nameInput[0] == nameInput[length - 1]:
      #If they are, it will continue the process with recursive functions, removing the first and last character from the prior string and checking the trueness
      return questionTwo(nameInput[1: length - 1])
    #If it eventually returns false, it will result in it being deemed not a palindrome.
    else:
      return False
  
  #Gets the name input from the user
  print("The family tree for the Zahir's is: Ava, Hannah, Racecar, Elle, Aziza, Abdullah, Amalia, Aya, and Zayan. ")
  nameInput = input("Input a name that you want to check: ")
  #Sets the answer of it being true (palindrome) or not to the variable palindromeOrNot by setting the function's output to the variable
  palindromeOrNot = questionTwo(nameInput)
  
  #If the value is true, then it will print that it is a palindrome
  if palindromeOrNot:
    print(nameInput, "is a palindrome!")
  #If the value is false, then it will print that it wasn't a palindrome
  else:
    print(nameInput, "is not a palindrome!")
    #It will also create a new name, for if it was a palindrome and print it out for the user
    newName = nameInput + nameInput[::-1]
    print("If it was a palindgfurome, it would be", newName)
  
  #Initially runs the function to start the code
  questionTwo(nameInput)

if binaryOrPalindrome == 'binary' or binaryOrPalindrome == 'Binary':
  #Creates a list used to store all of the values found to be in the binary sequence as individual indexes, as well as defines a binaryValue & sumOfValues value to be used later. 
  list = []
  binaryValue = 0
  sumOfValues = 0
  
  #Creates a function used to convert decimal values into binary
  def questionOne(number): 
    #If the number value is greater than or equal to 1, it will run.
    if number >= 1:
      #It reruns the function in a recursive manner with floor diving by two
      questionOne(number // 2)
      #Appends the number value with a floor division of two and converts to a string to the "list" list
      list.append(str(number % 2))
  
  #creates variable for users input of values for binary function
  amountOfTimes = int(input("How many numbers do you want to input: "))
  
  #takes numbers that the user inputs and asks them to input numbers they want to convert
  for i in range(amountOfTimes):
    numberInput = str(input('Input a numerical value you would like to convert to binary: '))
    #Tries to turn value into a number
    try:
      sumOfValues+=int(numberInput)
      #If not possible, prints an error message
    except ValueError:
      print("One of the values in your file could not be processed due to the fact that it was not a number.")
      #If possible, continues
    else:
      mean = sumOfValues/amountOfTimes
      #This adds the values to the file "input_numbers.txt"
      numberInputFile = open("input_numbers.txt", "a")
      numberInputFile.write(" " + numberInput)
      #numberInputFile = open("input_numbers.txt", "r")
      #numberRead = numberInputFile.read()
      #print(numberRead)
      numberInputFile.close()

  #reads content within the file
  numberInputFileRead = open("input_numbers.txt", "r")
  #sets the contents to a variable and splits it into a list
  numberInputFileContents = numberInputFileRead.read()
  numbers = numberInputFileContents.split()
  #creates a value for n to be used in the reiteration
  n=-1
  #for the amount of times given by the user, it will repeat the Try, Except, Else operation
  for i in range(amountOfTimes):
    #starts by adding 1 to the index value, starting with an index of 0
    try:
      n+=1
      number = numbers[n]
    #if an index error occurs (which occurs when inputting a string value instead of a number), it will let the user know of the error.
    except IndexError:
      print("One of the values in your file could not be processed due to the fact that it was not a number.")
    #tries to convert the input into a number
    try:
      number = int(number)
    #if the input cannot be converted, it will cause an error
    except ValueError:
      print("One of the values in your file could not be processed due to the fact that it was not a number.")
    #If it can, it will run the function to convert the number to binary
    else:
      questionOne(number)
      #combines the values of the list into one line
      binaryValue = "".join(list)
      binaryInputFile = open("binary_results.txt", "a")
      #writes the binary input into the file
      binaryInputFile.write(binaryValue)
      binaryInputFile.close()
      #prints the binary value
      print("Your number was converted to", binaryValue)
      #resets the binary value to be used again
      binaryValue = 0
      list = []
  #prints a thank you message
  print("The mean of your inputted values is", mean)
  numberInputFileClear = open("input_numbers.txt","w").close()
  print("Thank you for using our convertor!")
    

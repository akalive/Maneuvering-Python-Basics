# "Fizz buzz" is a basic Word Game 
# A program that takes a positive integer and returns: 
#       "Fizz Buzz" if the number is divisible by 3 and by 5;
#       "Fizz" if the number is divisible by 3;
#       "Buzz" if the number is divisible by 5; 
#       The number as a string for other cases.

def FizzBuzz(number):
   if number%3==0 and number%5==0:
       print(str("Fizz Buzz"))
   elif number%3==0:
       print(str("Fizz"))
   elif number%5==0:
       print(str("Buzz"))
   else:
       print(str(number))



usermenu=True
while usermenu:
    print ("""
    1.Play    
    2.Exit/Quit
    """)
    usermenu=input("Please select an option: ") 
    if usermenu=="1": 
      number=int(input("Please Enter a Positive Integer: "))
      FizzBuzz(number)
    elif usermenu=="2":
      print("\n Thank you for Playing!")
      usermenu=False
    elif usermenu !="":
      print("\n Not Valid Choice Try again.")  
       


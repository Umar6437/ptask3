# Python Input/Output

## 1. Taking Input in Python

For taking input from user we can use input command in python which is used to take input value from user and save it in assigned variable.
The code for input is as following:

    #Input
    a = input()
    #Output
    print(a)

In the above code we take the value from user and print as it is.

## 2. Taking Input From console in Python

Console is command-line interpreter which take input from user and used in the program. This also work same as stated above.

    #Input
    a = input()
    #Output
    print(a)

## 3. Taking Multiple Inputs

We can take input by using input() command in python for single variable but in the case of multiple inputs taken from users we use split() command which helps in taking more than one values from user at the same time which saves time. 

    #code for multiple input
    X, Y, Z = input("Enter three values: ")
    print(X)
    print(Y)
    print(Z)

## 4. Output Using print() function

Just like the other programing language we can see our result or the output which we want to see can be possible by using print()command. It take every value as an object and value given in double inverted comma as a string.

    #code for print variable
    a = 10
    print(a)

    #code for print any string
    print("This is my code")

## 5. Print without New line

We can simply use \n for adding new line in single print() command, which creates new line in the output

    print("Hi! I am Umar Farooq \n This is my program")

## 6. Python end parameter in print()

End parameter add the two print commands in one line as if we two different print() commands and wants to list that value in single we use end parameter

    # Using End parameter
    print("This is called", end = ' ')
    print("End Parmeter", end = ' ')

## Python sep parameter in print()

sep parameter seperates the objects of print by using the given value in the sep parameter. The code for this is given below:

    # Using sep parameter
    print("G","H","I", sep = '')
    print("27","05","2001", sep = '-')
    print("Umar","gmail", sep = '@')

## Python Output formatting

We can set the format of output by using many ways like modulo operator and also format() method. But now in python 3.7 and above there is new terminology introduce which is called fstring. Below the 3.7 python we use format() parameter helps us in putting the missing letter in the string.

    quest = "Hey My name is {}, I live in {}"
    name = "Umar"
    city = "Lahore"
    #Print using format() parameter
    print(quest.format(name,city))
    #Print using fstring
    print(f"Hey, My name is {name}, I live in {city}")

Now we can also use floating point to our periorities, we can use number of decimal places we want. It can be stated through an example

    price = 48.9999
    #using fstring
    txt = f"The price to bulb is {price: .2f}"
    print(txt)
    txt1 = "The price of bulb is {price: .2f}"
    print(txt1)










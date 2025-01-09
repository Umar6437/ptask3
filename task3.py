# Code for input
a = input("Enter the value of a = ")
print(a)

# Code for multiple input
x, y, z = input("Enter three values= ").split()
print(x)
print(y)
print(z)

# Code for Print()function
# for value of variable
print(a)
# for string
print("This is task 02")

# Print multiple line
print("The is line one \n This is line two")

# End parameter
print("How are", end= ' ')
print("You", end= ' ')

# Sep Parameter
print("A","B","C", sep=',')
print("01","01","2025", sep='-')
print("Umar","gmail", sep='@')

# Output Format
# using format()
intro = "My Name is {}, I live in {}"
name = "Umar"
city = "Lahore"
print(intro.format(name, city))
txt = "The price of the bulb is {price:.2f}"
print(txt.format(price = 43.05685))

#using fstring
para = f"Your live in {city}"
print(para)
value = 45.5345
txt1 = f"Only on {value:.2f} ruppees"
print(txt1)
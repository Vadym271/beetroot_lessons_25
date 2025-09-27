#task 1
string = 'helloworld'
if len(string) < 2: print('too short')
else: print(string[:2], string[-2:], sep = "")

#task 2
string2 = '1239204922'
if (len(string2) == 10) & (string2.isdigit()): print("it is a phone number")
else: print("it is not a phone number")

#task 3
result = input("2*3=")
if result == '6': print("that's correct, good job")
else: print("incorrect, try again")

#task 4
name = 'vadym'
name_input = input("enter your name:")
if name == name_input.lower(): print(True)
else: print(False)

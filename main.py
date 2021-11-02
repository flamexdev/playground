class colors:
  HEADER = '\033[95m'
  ENDC = '\033[0m'


age = input(colors.HEADER + "Age calculator\n" + colors.ENDC + "What's your age in years? ")
print("you are " + age + " years old.")
years = input("Enter a number of years and I'll tell you how many minutes that is ") #The input of the user will be stored as variable years
if years != str():
    print('Please rerun program and enter an integer')
else:
    print('Calculating')
years = int(years) #forces the variable year as an integer
days = years * 365 #Takes the variable years multiplied by 365 and saves it as variable days
hours = days * 24 #Takes the variable days multiplied by 24 and saves it as variable hours
minutes = hours * 60 #Takes the variable hours multiplied by 60 and saves the result as minutes
print(years, 'years is', minutes, "minutes") #prints the result within the sentece ie: '2 years is 1051200 minutes' 

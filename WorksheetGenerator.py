import random

#ToDo
#Find out all question types from Mason
#Implement all question types
#Figure out Databases
#Implement Databases
#Work on output formatting
#Work on difficulty Scaling
#Work on reasonable probability between procedural and database problems
#Fix bugs
#Fix bugs
#Learn Python
#Learn how I will be retrieving data(not a priority)

def main():
    returner = ""
    typeDict = {0: baseConversion,
                1: 'etc function',
                2: 'etc'}
    containsInput = True;
    counter = 1
    while containsInput:
        problemType = 'input'
        difficulty = 'input'
        amount = 'input'
        #this should do the format
        #1.
        #Problem
        #
        #2.
        #Problem       
        for i in range(amount):
            returner += counter++ + ".\n" + typeDict[problemType](difficulty) + "\n"
    return returner
#Begining of Helper Functions
#a function that allows me to convert a number from base 10 to base x(2-16) because apparently python doesn't have this already?
def baseConverter(self, num, x):
	ans = ""
	key = "0123456789ABCDEF"
	while num < x:
		ans = key[num % x] + ans
		num = num/x
	return ans

#End of Helper Functions

#Begining of Generation Functions
#problemType 0    
def baseConversion(self, difficulty):
	if difficulty == 1:
		operators = "+-"
		bases = [2, 8, 10]
		base1 = bases[random.randInt(0, 2)];
		base2 = bases[random.randInt(0,2)];
		return baseConverter(random.randInt(2, 32), base1) + "_" + base1 + " " + operators[random.randInt(0,1)] + " " + baseConverter(randomInt(2,32), base2) + "_" + base2
	elif difficulty == 2:
		operators = "+-"
		bases = [2, 8, 10, 16]
		base1 = bases[random.randInt(0, 3)];
		base2 = bases[random.randInt(0,3)];
		return baseConverter(random.randInt(2, 256), base1) + "_" + base1 + " " + operators[random.randInt(0,1)] + " " + baseConverter(randomInt(2,256), base2) + "_" + base2
	elif difficulty == 3:
		operators = "+-*/"
		bases = [2, 8, 10, 16]
		base1 = bases[random.randInt(0, 3)];
		base2 = bases[random.randInt(0,3)];
		return baseConverter(random.randInt(2, 1024), base1) + "_" + base1 + " " + operators[random.randInt(0,3)] + " " + baseConverter(randomInt(2,32), base2) + "_" + base2
	elif difficulty == 4:
		operators = "+-*/"
		bases = [2, 8, 10, 16]
		base1 = bases[random.randInt(0, 3)];
		base2 = bases[random.randInt(0,3)];
		base3 = bases[random.randInt(0,3)];
		return baseConverter(random.randInt(2, 32768), base1) + "_" + base1 + " " + operators[random.randInt(0,3)] + " " + baseConverter(randomInt(2,32768), base2) + "_" + base2 + operators[random.randInt(0,3)] + " " + baseConverter(randomInt(2,32768), base3) + "_" + base3
	else
		operators = "+-*/"
		base1 = random.randInt(2,16);
		base2 = random.randInt(2,16);
		base3 = random.randInt(2,16);
		return baseConverter(random.randInt(2, 1048576), base1) + "_" + base1 + " " + operators[random.randInt(0,3)] + " " + baseConverter(randomInt(2,1048576), base2) + "_" + base2 + operators[random.randInt(0,3)] + " " + baseConverter(randomInt(2,1048576), base3) + "_" + base3
		
def stringWkst(self, difficulty):
	pass
    
#problemType 1

#etc...    
              

#End of Generation Functions			  

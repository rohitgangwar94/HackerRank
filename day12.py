class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self,firstNme,lastName,idNumber,scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
     
    # Write your function here
    def calculate(self):
        avg = sum(scores)/len(scores)
        if avg >= 90:
            return "O"
        if avg >= 80:
            return "E"
        if avg >= 70:
            return "A"
        if avg >= 55:
            return "P"
        if avg >= 40:
            return "D"
        return "T"

        '''
        if a < 40:
            return('T')
        if 40<= a<55:
            return('D')
        if 55<=a<70:
            return('P')
        if 70<=a<80:
            return('A')
        if 80<=a<90:
            return('E')
        if 90<=a<=100:
            return('O') 
'''
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())

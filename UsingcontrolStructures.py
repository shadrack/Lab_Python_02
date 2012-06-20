
theInput = raw_input("Enter an integer: ")
#Your code here
theInput=int(theInput)
if (theInput%2==0):
	print "Even Number"
else:
	print "Odd Number"

print "Question 6"	
primarySchoolAge=6
legalvotingAge=18
AgeofBecomingPresident=45
RetirementAge=60
Person_Age= raw_input("Enter your Age: ")
# A person's age 
Person_Age = int(Person_Age)
if (Person_Age<primarySchoolAge):
	print "Too Young to start primary school"
elif(Person_Age>legalvotingAge):
	print "Remember to vote for Atta Mills in the coming Election"
if(Person_Age>=AgeofBecomingPresident):
	print "Vote for Me"
else:
    print " You can't be President"
if(Person_Age>RetirementAge):
		print "Too Old"

print "question 7"
i=40
while (i>0):
	i=i-1
	if (i%3==0):
		print i
	



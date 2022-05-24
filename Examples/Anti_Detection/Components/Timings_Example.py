#Import Random Abiltys
import random 

#User_Interaction_Times Var Set To A Random Number Between .20 And 2
UIT = float(random.randrange(20, 200))/100

#Print User_Interaction_Times
print(UIT)

#Example Outputs (0.20, 0.21, 0.95, 1.50, 1.05, 2)
#We Use These Numbers When We Wait Between Actions To Make It Seem Like A User Is Thinking Or Doing Things Instead Of Instant Clicking And Such (This Is Decimal Accurate)

# Make a program that that ask for four bimesters grates
# Make the average and show it

# Plus: Sets an aleatory average 
# If the average of the student is bigger right "approved"
# Otherwise, if is smaller right "disapproved"

import random

note1 = random.randfloat(0,10)
note2 = random.randint(0,10)
note3 = random.randint(0,10)
note4 = random.randint(0,10)

Studentaverage = 1/4*(note1 + note2 + note3 + note4)
print("Student Average:", Studentaverage)

average = random.randint(3,7)
print("Average:", average) 

if Studentaverage >= average:
    print("Approved")
else:
    print("disapproved")


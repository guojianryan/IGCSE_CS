import random
import os
with open(os.path.join(os.path.join(os.getcwd(), "prerelease/yields.in")), "w") as myfile:
    for i in range(140):
        myfile.write(str(random.randint(3,10))+"\n")
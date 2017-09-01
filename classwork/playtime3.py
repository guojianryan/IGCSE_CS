"""
Your parents only allow you to play video games 
when you have finished your homework or played piano. 
Please complete the following programme 
to print whether you are allowed now using an IF statement. 
"""

hw_completed = input("Have you finished your homework?  (Y/N)")
piano_played = input("Have you played  piano?  (Y/N)")

if hw_completed == "Y" or piano_played == "Y":
    print("Yes, you may.")
else:
    print("No, you cannot!")
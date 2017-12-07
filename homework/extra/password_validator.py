import random
recent_passwords = list()

for counter in range(12):
	s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
	p =  "".join(random.sample(s,8))
	recent_passwords.append(p)

print(recent_passwords)

password = ""

while password in recent_passwords or len(password) != 8:
	password = input("Please enter your password")

del recent_passwords[0]
recent_passwords.append(password)

print(recent_passwords)

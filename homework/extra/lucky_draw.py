from random import randrange

names = ["Leo","Dylan","Shaurya","Zachary","Matthew","Leroy","Noah","Kristy","Valerie","Arul","Charlotte", "Nisha","Isabella"]
genders = ["M","M","M","M","M","M","M","F","F","M","F","F","F",]
winners = list()

while len(winners) < 3:
    winner_idx = -1
    while winner_idx== -1 or winner_idx in winners:
        winner_idx = randrange(len(names))
    winners.append(winner_idx)
    
for idx in winners:
    print(names[idx], genders[idx])




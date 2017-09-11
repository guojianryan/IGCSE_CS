def scramble(s1,s2):
    for c in s2:
        if c not in s1:
            return False
        else:
            s1 = s1.replace(c,"",1)
    return True

print(scramble('scriptjava','javascript'))
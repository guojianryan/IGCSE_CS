from collections import Counter

def duplicate_count(text):
    text = text.lower()
    count = 0
    unique = set(text)
    for char in unique:
        if text.count(char)>1:
            count = count + 1
    return count

def duplicate_count2(text):
    return len([ v for k, v in Counter(text.lower()).items() if v > 1])

print(duplicate_count2("abcdeaB"))
        



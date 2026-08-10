s = "aaca"
t = "ccac"

if len(s) == len(t):
    for letter2 in s:
        for letter in t:
            if word.count(letter) == word.count(letter2):
                if (letter in s):
                    continue
                else:
                    return False
            else:
                return False

    return True
        

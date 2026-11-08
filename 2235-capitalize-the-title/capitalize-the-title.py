import re

class Solution(object):
    def capitalizeTitle(self, title):
    #first we extract all the words from sentence and add them in a list
    #now we check the length of each word by iterating over the list
    #if the length is >2 then we capitalize its first letter and lower case the others
        res = []
        title = re.sub(r'[^\w\s]', '', title)

        words = title.split()

        for word in words:
            if len(word) > 2:
                word = word.capitalize()
                res.append(word)
            else:
                res.append(word.lower())
                
        return ' '.join(res)
            
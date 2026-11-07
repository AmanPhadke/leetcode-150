class Solution(object):
    def checkIfPangram(self, sentence):
        alpha = 'abcdefghijklmnopqrstuvwxyz'


        for char in alpha:
            if char not in sentence:
                return False


        return True
        
class Solution(object):
    def isCircularSentence(self, sentence):
        words = sentence.split(' ')

        if len(words) < 2:
            first = words[0][0]
            last = words[0][-1]

            if first != last:
                return False
            

        for i in range(1, len(words)):
            if i-1 == 0:
                first = words[0][0]
                last = words[-1][-1]

                if first != last:
                    return False

            last = (words[i-1][-1])
            first = (words[i][0])

            if first != last:
                return False

        return True
            
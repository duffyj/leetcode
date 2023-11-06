class Solution:
    def fullJustify(self, words: List[str], maxWidth: int):
        justifiedText = []
        lines = [[]]
        curLen = 0
        for word in words:
            if curLen != 0:
                curLen +=1 
            if curLen + len(word)> maxWidth:
                curLen = 0
                lines.append([])
            curLen += len(word)
            lines[-1].append(word)
        lineSpacing = []
        for line in lines[:-1]:
            print(line)
            wordLen = sum(len(w) for w in line)
            spacesLen = [1] * (len(line) - 1)
            padding = maxWidth - sum(spacesLen) - wordLen
            p = 0
            while spacesLen and padding > 0:
                spacesLen[p] += 1
                p +=1
                if p == len(spacesLen):
                    p = 0
                padding -=1
            if spacesLen:
                lineSpacing.append([0] + spacesLen)
            else:
                lineSpacing.append([0, maxWidth -wordLen] )   
        lineSpacing.append([0] + ([1] * (len(lines[-1]) - 1)))
        

        for lineNum,(words,spaces) in enumerate(zip(lines,lineSpacing)):
            justifiedLine = []
            for word,nspaces in zip_longest(words,spaces):
                for _ in range(nspaces):
                    justifiedLine.append(' ')
                if word:
                    justifiedLine.append(word)
            if lineNum ==len(lines) -1:
                trailingSpaces = maxWidth - sum((len(x) for x in justifiedLine))
                for _ in range(trailingSpaces):
                    justifiedLine.append(' ')
            justifiedText.append(''.join(justifiedLine))
        return justifiedText
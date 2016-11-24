#6. ZigZag Conversion*
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
    		return s
    	length=len(s)
    	wordlist=[""]*numRows
    	charclass=[0]*length               #初始化很赞
    	for i in range(length):
    		charclass[i] = i%(2*numRows-2)
    		if charclass[i] > numRows-1:
    			charclass[i]=2*numRows-2-charclass[i] 
    	for i in range(length):
    		wordlist[charclass[i]]+=(s[i])
    	return "".join(wordlist)
#6. ZigZag Conversion*  更好理解时间也短
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) < 2: return s
        rows = ["" for _ in range(numRows)]
        i, right = -1, True
        for ch in s:
            i = i + 1 if right else i - 1
            rows[i] += ch
            right = False if i == numRows-1 else True if i == 0 else right
        return "".join(rows)  
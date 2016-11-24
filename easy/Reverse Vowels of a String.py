#345. Reverse Vowels of a String    翻转字符串中的元音字母
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        li = []
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                li += [i]       #先找出元音字母的位置
        j, k = 0, len(li)-1
        sli = list(s)
        while j < k:
            sli[li[j]], sli[li[k]] = sli[li[k]], sli[li[j]]
            j += 1
            k -= 1
        return ''.join(sli)

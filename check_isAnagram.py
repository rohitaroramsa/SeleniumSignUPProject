def isAnagram(word1, word2):
    if len(word1) == len(word2):
        ans = 'is Anagram'
        for each in word1:
            if word1.count(each) != word2.count(each):
                ans = 'not Anagram'
        return ans
    else:
        return 'not Anagram'


################     test  ############
reply = isAnagram('potter', 'retoop')
print(reply)

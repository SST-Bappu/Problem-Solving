class Solution:
    def LongestSubString(self,str): #Sliding Window Technique
        hashtable= dict()
        substr = 0
        cnt = 0
        left = 0
        for i in range(len(str)):
            val = hashtable.get(str[i])
            if val is None or int(val)<left:
                hashtable.update({str[i]:i})
                cnt+=1
            else:
                left = int(val)+1
                cnt = i-int(val)
                hashtable.update({str[i]:i})

            substr=max(substr,cnt)
        return substr


if __name__=="__main__":
    str = "dvdf"
    x = list(str)
    result = Solution()
    print(result.LongestSubString(x))
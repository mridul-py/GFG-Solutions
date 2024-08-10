
class Solution:
    def Maximize(self, arr): 
        # Complete the function
        Sum=0
        Mod=(10**9)+7
        arr.sort()
        for i in range(len(arr)):
            Sum+=arr[i]*i
        return Sum%Mod

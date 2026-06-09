class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x="".join(map(str,digits))
        ans=int(x)+1
        fans=list(map(int,str(ans)))
        return fans
        
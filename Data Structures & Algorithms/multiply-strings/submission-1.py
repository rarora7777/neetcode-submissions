class Solution:
    def parseInt(self, num: str) -> int:
        n: int = 0
        for ch in num:
            n *= 10
            n += int(ch)
        
        return n
    
    def toString(self, n: int) -> str:
        s = ''
        while n > 0:
            s = str(n % 10) + s
            n = n // 10
        
        return s
    
    def multiply(self, num1: str, num2: str) -> str:
        n1: int = self.parseInt(num1)
        n2: int = self.parseInt(num2)

        n = n1 * n2

        if n==0:
            return '0'

        return self.toString(n)

        
        
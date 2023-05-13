class Solution:
    def reverse(self, x: int) -> int:
        sign_value = 1

        # Checks if x is positive or negative
        if x < 0:
            sign_value = -1

        # Working with absolute value of x
        x = abs(x)
        num = 0

        # The loop will take the ones digit of x through mod, and store it in remainder
        while x > 0:
            remainder = x % 10
            # After ones digit is taken, it will modify x by removing ones digit
            x = x // 10
            # Modifies the variable num by adding remainder to it
            num = (num * 10) + remainder
        
        # This is a constraint of the problem, which has not been clearly identified in the problem description
        if (num > (2**31) - 1):
            return 0
            
        # Returns the reversed integer considering positive or negative value
        return (num * sign_value)
    
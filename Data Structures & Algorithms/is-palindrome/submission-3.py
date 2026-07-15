class Solution:
    def isPalindrome(self, s: str) -> bool:

        n_s = "".join(filter(str.isalnum, s))
        new_s = n_s.lower()
        
        l, r = 0, len(new_s) - 1 

        while l < r:
            if new_s[l] == new_s[r]:
                l += 1
                r -= 1
            else:
                return False

        return True



            
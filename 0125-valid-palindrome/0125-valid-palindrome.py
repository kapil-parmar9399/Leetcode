class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""

        for ch in s:
            if ch.isalnum():
                new = new + ch.lower()

        reverse = ""

        for ch in new:
            reverse = ch + reverse

        if new == reverse:
            return True
        else:
            return False
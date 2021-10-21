class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_ = "".join(re.findall("[a-zA-Z0-9]+", s))
        s_ = s_.upper()

        return s_ == s_[::-1]

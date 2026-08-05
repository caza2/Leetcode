class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(n) time and space
        dict_signature_s: dict[str, int] = {}
        for string in s:
            if string not in dict_signature_s:
                dict_signature_s[string] = 1
            else:
                dict_signature_s[string] += 1
                
        dict_signature_t: dict[str, int] = {}
        for string in t:
            if string not in dict_signature_t:
                dict_signature_t[string] = 1
            else:
                dict_signature_t[string] += 1
        return dict_signature_s == dict_signature_t
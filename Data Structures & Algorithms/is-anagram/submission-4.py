class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s, dict_t = {}, {}
        for string in s:
            if string not in dict_s:
                dict_s[string] = 1
            else:
                dict_s[string] += 1
        for string in t:
            if string not in dict_t:
                dict_t[string] = 1
            else:
                dict_t[string] += 1
        return dict_s == dict_t
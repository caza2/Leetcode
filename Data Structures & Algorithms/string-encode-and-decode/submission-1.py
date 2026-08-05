class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "è"
        encoded = []
        for s in strs:
            encoded.append([])
            encoded[-1].append("".join(chr(ord(char) + 1) for char in s))
            encoded[-1] = "".join(encoded[-1])
        return "é".join(encoded)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]
        if s == "è":
            return []
        decoded = []
        i = 0
        while i < len(s):
            decoded.append([])
            while i < len(s) and s[i] != "é":
                decoded[-1].append(str(chr(ord(s[i]) - 1)))
                i += 1
            if decoded[-1] == []:
                decoded[-1] = ""    
            else:
                decoded[-1] = "".join(decoded[-1])
            i += 1
        if s[-1] == "é":
            decoded.append("")
        return decoded
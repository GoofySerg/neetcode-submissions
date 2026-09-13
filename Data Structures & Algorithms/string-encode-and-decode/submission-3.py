class Solution:

#so the trick is to encode using the length and then a hashtag to signal end of number 
    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        for word in strs:
            encoded_string.append(f"{len(word)}#{word}")
        return "".join(encoded_string)

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0

        while i < len(s):
            first = s.index('#', i)
            number = int(s[i:first])
            decoded_strs.append(s[first+1:number+1+first])
            i = first + number + 1

        return decoded_strs


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        dic = {}
        for word in strs:
            sortedWord = "".join(sorted(word))
            if dic.get(sortedWord) is not None:
                dic[sortedWord].append(word)
            else:
                dic[sortedWord] = [word]
        
        for key, values in dic.items():
            answer.append(values)
        return answer


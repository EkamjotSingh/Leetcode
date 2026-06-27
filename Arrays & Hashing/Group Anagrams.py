from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        complete = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for letters in word:
                count[ord(letters) - ord("a")] += 1

            complete[tuple(count)].append(word)

        return list(complete.values())
    
strs = ["act","pots","tops","cat","stop","hat"]
print(Solution().groupAnagrams(strs))

       

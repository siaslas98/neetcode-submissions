class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # iterate throught the list and sort each string. 
        # check in dictionary if the string already exists,
        # if exists, append the string to the sublist of that key in the dictionary
        # else, create new entry in the dictionary and append the sorted version of the string


        strings_dict = {}
        res = []

        for s in strs:
            sorted_str = "".join(sorted(s))
            if sorted_str in strings_dict:
                strings_dict[sorted_str].append(s)
            else: strings_dict[sorted_str] = [s]
        
        for k, v in strings_dict.items():
            res.append(v)

        return res


        
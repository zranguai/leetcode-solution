# 2024-7-24 v0.1
# https://leetcode.cn/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-100-liked
# tag:哈希


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashdict = dict()
        
        for str_ in strs:
            sort_str = "".join(sorted(str_))  # 需要"".join()一下，如果是直接sorted(str) "ate"出来的是'a','t','e'
            if sort_str not in hashdict.keys():
                hashdict[sort_str] = [str_]
            else:
                hashdict[sort_str].append(str_)

        return hashdict.values()  # 自动用列表把里面的值包括起来 所以不用外面单独加列表
    

if __name__ == "__main__":
    solution = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    res_str = solution.groupAnagrams(strs)
    print(res_str)

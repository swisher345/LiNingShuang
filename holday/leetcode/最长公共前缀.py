# 14.
# 最长公共前缀
# 简单
# 相关标签
# premium
# lock
# icon
# 相关企业
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串
# ""。
#
#
#
# 示例
# 1：
#
# 输入：strs = ["flower", "flow", "flight"]
# 输出："fl"
# 示例
# 2：
#
# 输入：strs = ["dog", "racecar", "car"]
# 输出：""
# 解释：输入不存在公共前缀。
#
#
# 提示：
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i]
# 如果非空，则仅由小写英文字母组成
# 逐个比较
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break
        return prefix
    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]

#入口函数
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
    # from typing import List, Dict, Tuple, Optional
    #
    # # 字符串列表
    # names: List[str] = ["Alice", "Bob", "Charlie"]
    #
    # # 整数列表
    # numbers: List[int] = [1, 2, 3, 4, 5]
    #
    # # 浮点数列表
    # floats: List[float] = [1.1, 2.2, 3.3]
    #
    # # 布尔值列表
    # flags: List[bool] = [True, False, True]
    #
    # # 字典列表
    # students: List[Dict[str, str]] = [
    #     {"name": "Alice", "grade": "A"},
    #     {"name": "Bob", "grade": "B"}
    # ]
    #
    # # 元组列表
    # coordinates: List[Tuple[int, int]] = [(0, 0), (1, 1), (2, 2)]
    #
    # # 可选整数列表（列表中的元素可以是整数或None）
    # optional_numbers: List[Optional[int]] = [1, 2, None, 4]
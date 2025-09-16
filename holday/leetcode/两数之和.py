class Solution:
    def twoSum(self, nums, target):
        hashmap = {}  #使用哈希表（hashmap）记录已遍历数字的下标；
        for i, num in enumerate(nums): #使用enumerate函数遍历列表nums，同时获取数字的下标i和值num。
            diff = target - num   # 计算目标值diff。
            if diff in hashmap:   # 判断diff是否在hashmap中。
                return [hashmap[diff], i]  # 返回结果 。
            hashmap[num] = i      # 将数字num添加到hashmap中，并记录其下标i。

# 示例测试代码
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(solution.twoSum(nums, target))  # 输出：[0, 1]
#哈希表：哈希映射HashMap 是一种数据结构，用于存储键值对，并允许快速查找、插入和删除。通过hash function 把键银蛇到数组的索引位置从而快速定位
#
# from typing import List
#
#
# def twoSum(nums: List[int], target: int) -> List[int]:
#     n = len(nums)
#     hashtable = {}
#
#     for i, num in enumerate(nums):
#         result = target - num
#         if result in hashtable:
#             return [hashtable[result], i]
#         else:
#             hashtable[num] = i
#
#     return []
#
#
# def isPalindrome(x: int) -> bool:
#     if x < 0:
#         return 0
#     else:
#         strx = list(str(x))
#         lengh= len(strx)
#         for i in range(lengh):
#             if i>=lengh/2:
#                 break
#             if strx[i]==strx[lengh-i-1]:
#                 continue
#             else:
#                 return 0
#         return 1
#
#
#
#
#
# def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#     prehead=ListNode(-1)
#     prev =prehead
#     while l1 and l2:
#         if l1.val<l2.val:
#             prev.next=11
#             l1=l1.next
#         else:
#             prev.next=l2
#             l2=l2.next
#         prev=prev.next
#     prev.next=l1 if l1 is not None else l2
# if __name__ == "__main__":
#     print(isPalindrome(121))
#     ret = twoSum([1, 2, 3, 4, 5, 6], 5)
#     print(ret)

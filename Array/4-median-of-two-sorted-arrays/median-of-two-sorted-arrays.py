class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        finalArr = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                finalArr.append(nums1[i])
                i+=1
            else:
                finalArr.append(nums2[j])
                j+=1
        while i < len(nums1):
            finalArr.append(nums1[i])
            i+=1
        while j < len(nums2):
            finalArr.append(nums2[j])
            j+=1
        
        if len(finalArr)%2 == 0:
            d = len(finalArr)//2
            sum = finalArr[d-1]+finalArr[d]
            return sum/2
        else:
            d = len(finalArr)//2
            return finalArr[d]
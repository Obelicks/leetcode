def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i,j = 0 , 0
    while(i < (m+n) and j < n):
        if nums1[i] > nums2[j]:
            nums1.insert(i, nums2[j])
            nums1.pop(-1)
            j += 1
            m += 1
        elif(nums1[i]==0 and i >= m):
            nums1[i] = nums2[j]
            j += 1
            i += 1
        else:
            i += 1 
    print(nums1)

nums1 =[-1,3,0,0,0,0,0]
nums2 = [0,0,1,2,3]
merge(nums1,2,nums2,5)
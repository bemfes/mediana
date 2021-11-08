nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
def medians(nums1,nums2):
    nums_new = nums1 + nums2
    nums_new.sort()
    length=len(nums_new)
    if length % 2 != 0:
        mediana1 = nums_new[int((length+1)/2 - 1)]
        print(float(mediana1))
        print("Объединенный список = ",nums_new,", медиана - ",mediana1)
    else:
        mediana2 = (nums_new[int(length/ 2 - 1)] + nums_new[int(length/ 2)]) / 2
        print(float(mediana2))
        print("Объединенный список = ",nums_new,", медиана - ",mediana2)
medians(nums1,nums2)

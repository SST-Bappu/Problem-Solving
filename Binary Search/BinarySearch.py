def BinarySearch(arr,t,left=0,right=None):
    if right==None:
        right=len(arr)-1
    if left>right:
        return None
    mid = (left+right)//2
    if arr[mid]==t:
        return mid
    if t>arr[mid]:
        return BinarySearch(arr,t,mid+1,right)
    else:
        return BinarySearch(arr,t,left,mid-1)
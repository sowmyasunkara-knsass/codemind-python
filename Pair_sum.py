def pair_sum(dict, arr, sum):
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]+arr[j]==sum:
                    return True
        return False

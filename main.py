def merge_sort(A):
    if len(A) > 1:
        mid = len(A) // 2
        left = A[:mid]
        right = A[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1
            
    return A

def triplesum2zero(L: list[int]) -> [(int, int, int)]:
    L = merge_sort(L)
    res = []
    for i in range(len(L) - 2):
        if i > 0 and L[i] == L[i-1]:
            continue
        l, r = i + 1, len(L) - 1
        while l < r:
            if l != i and r != i and L[l] != L[i] and L[r] != L[i]:
                s = L[i] + L[l] + L[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res.append((L[i], L[l], L[r]))
                    while l < r and L[l] == L[l+1]:
                        l += 1
                    while l < r and L[r] == L[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
            else:
                if L[l] == L[i]:
                    l += 1
                else:
                    r -= 1
    return res


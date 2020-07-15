def Solution(arr,K):
    maxLength = 0
    windowStart = 0
    maxOnes = 0
    for windowEnd in range(len(arr)):
        if arr[windowEnd] == 1:
            maxOnes += 1
            print(f'Max Ones: {maxOnes}')
        if (windowEnd-windowStart+1-maxOnes) > K:
            print(f'Greater then K:{windowEnd-windowStart+1-maxOnes}')
            print(f'End:{windowEnd},Start:{windowStart},MaxOnes:{maxOnes}')
            if arr[windowStart] == 1:
                maxOnes -= 1
                print(f'Im one:{maxOnes}')
            windowStart += 1
        maxLength = max(maxLength, windowEnd-windowStart+1)
        print(f'End:{windowEnd}, Start:{windowStart}, max length:{maxLength}')

    return maxLength

print(Solution([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1],3))
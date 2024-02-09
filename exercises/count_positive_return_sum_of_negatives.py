'''
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.
Example

For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
'''



def count_positives_sum_negatives(arr):
    pos = 0
    sum = 0
    if arr:
        for i in arr:
            if i > 0:
                pos +=1
            else:
                sum += i
        return [pos , sum]
    else:
        return []
    
# refactor
    
def count_positives_sum_negatives1(arr):
    count_positive = sum(1 for i in arr if i>0)
    sum_negative = sum(i for i in arr if i<0)
    return [count_positive , sum_negative] if arr else []


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
print(count_positives_sum_negatives1(arr))
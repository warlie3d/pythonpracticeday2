#Write a Python function called max_num()to find the maximum of three numbers.
def max_num(*nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return max(nums[0], max_num(*nums[1:]))
    
#example
print('max number in 1, 2, 3 is ', max_num(1, 2, 3))
print('max number in 7, 8, 9 is ', max_num(7, 8, 9))
print('max number in 10, 2, 13 is ', max_num(10, 2, 13))


#Write a Python function called mult_list() to multiply all the numbers in a list.
def multi_list(my_list):
    #base case
    if not my_list:
        return 1
    else:
        return my_list[0] * multi_list(my_list[1:])
    
#example
numbers = [2, 3, 4, 5]
result = multi_list(numbers)
print(f'The product of {numbers} is {result}')

#Write a Python function called rev_string() to reverse a string.
def rev_string(input_str):
    if len(input_str) <= 1:
        return input_str
    else:
        return input_str[-1] + rev_string(input_str[:-1])
    
#example
original_str = "Hello All!"
reversed_str = rev_string(original_str)
print(f'The reversed string of "{original_str}" is: "{reversed_str}"')
    

# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

def num_within(num, start, end):
    if start <= num <= end:
        return True
    elif start > end:
        return False
    else:
        return num_within(num, start + 1, end)

#example
print(num_within(3, 2, 4)) #Returns True
print(num_within(3, 1, 3)) #Returns True
print(num_within(10, 2, 5)) #Returns False

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.

def pascal(n, triangle=None):
    if n <= 0:
        return []
    
    if triangle is None:
        triangle = [[1]]

    if len(triangle) == n:
        return triangle
    else:
        last_row = triangle[-1]
        new_row = [1] + [last_row[i] + last_row[i + 1] for i in range(len(last_row) - 1)] + [1]
        triangle.append(new_row)
        return pascal(n, triangle)
    
def print_pascal_triangle(n):
    triangle = pascal(n)
    for row in triangle:
        print(row)

#example
print_pascal_triangle(5)
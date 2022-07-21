# nums = [i for i in range(1,1001)]
# string = 'Practice probs to drill list comprehension in your head.'

# #print every number divisible by 8
# q1 = [num for num in nums if num %8==0]

# #print every number including '6'
# q2 = [num for num in nums if '6' in str(num)]

# #print amount of spaces in the string
# q3 = len([c for c in string if c ==' '])

# #print all letters that aren't vowels
# q4 = ''.join([i for i in string if i not in 'aeiou'])

# #print all words shorter than 5 chars
# words=string.split()
# q5 = [word for word in words if len(word)<5]

# #print a dictionary counting the length of words
# q6 = {word:len(word) for word in words}

# #print all numbers divisible by 2-9
# q7 = [num for num in nums if True in [True for divisor in range(2,10) if num % divisor ==0]]

# #print a dictionary with GCD from 1-10
# q8 = {num:max([divisor for divisor in range(1,10) if num % divisor == 0]) for num in nums}

# arr=[]
# for i in map(int, input().split()):
#     arr.append(i**2)
# print(*arr)


# print(*[i**2 for i in map(int, input().split())])



arr=[i for i in range(1, 1001)]
# str = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# print(*[i for i in str.split(' ') if i.isdigit()])


# numbers = range(20)
# print(['odd' if i % 2 != 0 else 'even' if i != 0 else 'zero' for i in numbers])


# a = [1,2,3,4,5,6,7,8,9]
# b = [2,7,1,12]
# print(*[(aVal, bVal) for aVal in a for bVal in b if aVal == bVal])

# print(*[i for i in str.split() if len(i) < 4 and i.isalpha()])

# print(''.format([i for i in arr if True in [True for x in range(2,10) if i % x == 0]]))

print({num:max([divisor for divisor in range(1,10) if num % divisor == 0]) for num in arr})
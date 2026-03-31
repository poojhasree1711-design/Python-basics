# 1. Dynamic Horizontal Pyramid
# Print a horizontal pyramid where stars expand and then shrink:
#  * * * * * * *
#   * * * * *
#     * * *
#       *
#     * * *
#   * * * * *
# * * * * * * *
n=7
#Top part (shrinking)
for i in range(n,0,-2):
    spaces=(n-i)//2
    print(" "*spaces+"* "*i)
# Bottom part (expanding)
for i in range(3,n+1,2):
    spaces=(n-i)//2
    print(" "*spaces+"* "*i)


# 2. Custom Sorting (Logic + Lambda)
# Write a function to sort a list of tuples based on:
# First: sum of elements
# If tie: sort by second element descending
# input = [(1, 3), (2, 2), (1, 2), (3, 1)]
# output = [(1, 3), (2, 2), (1, 2), (3, 1)]
data = [(1, 3), (2, 2), (1, 2), (3, 1)]
result = sorted(data,key=lambda x:(x[0]+x[1],-x[1]))
print(result)


# 4. Matrix Rotation (In-place)
# Rotate a square matrix by 90° clockwise without using extra space.
def rotate(matrix):
    n=len(matrix)
    #Transpose
    for i in range(n):
        for j in range(i,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    #Reverse each row
    for row in matrix:
        row.reverse()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
print(matrix)


# 5. Flatten Nested Dictionary
# Convert a nested dictionary into a single-level dictionary using dot notation.
# input = {"a": {"b": {"c": 1}}, "d": 2}
# output = {"a.b.c": 1, "d": 2}
def flatten(d,parent_key='',sep='.'):
    items={}
    for k, v in d.items():
        new_key=parent_key+sep+k if parent_key else k
        if isinstance(v,dict):
            items.update(flatten(v,new_key))
        else:
            items[new_key]=v
    return items
data = {"a": {"b": {"c": 1}}, "d": 2}
print(flatten(data))


# 6. Group Words by Frequency Pattern
# Group words that have the same frequency pattern.
# input = ["abb", "mee", "aab", "xyz", "xyy"]
# output = [["abb", "mee", "aab", "xyy"], ["xyz"]]
from collections import Counter, defaultdict

def group_words(words):
    groups=defaultdict(list)
    for word in words:
        pattern=tuple(sorted(Counter(word).values()))
        groups[pattern].append(word)
    return list(groups.values())
print(group_words(["abb", "mee", "aab", "xyz", "xyy"]))


# 7. Longest Substring Without Repeating Characters
# Find the length of the longest substring without repeating characters.
# input = "abcabcbb"
# output = 3
def longest_substring(s):
    seen=set()
    left=0
    max_len=0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left+=1
        seen.add(s[right])
        max_len=max(max_len,right-left+1)
    return max_len
print(longest_substring("abcabcbb")) 
 

# 8. Build Your Own JSON Parser (Mini Version)
# Convert a simple JSON string into a Python dictionary (no json module allowed).
# Example:
# '{"name": "John", "age": 30}'
def simple_json_parser(s):
    s=s.strip('{} ')
    result={}
    pairs=s.split(',')
    for pair in pairs:
        key,value=pair.split(':')
        key=key.strip().strip('"')
        value=value.strip()
        if value.isdigit():
            value = int(value)
        else:
            value=value.strip('"')
        result[key]=value
    return result
print(simple_json_parser('{"name": "John", "age": 30}')) 


# 9. Detect Cycle in Linked List
# Create a linked list and detect if it contains a cycle.
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
def has_cycle(head):
    slow=fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    return False

#Example case
a=Node(1)
b=Node(2)
c=Node(3)
a.next=b
b.next=c
c.next=a  #cycle
print(has_cycle(a))
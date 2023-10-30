Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
batches=["20cys", "21cys", "23cys"]
for x in batches
SyntaxError: incomplete input
batches=["20cys", "21cys", "23cys"]
print(len(batches))
SyntaxError: multiple statements found while compiling a single statement
batches=["20cys", "21cys", "23cys"]
print(len(range(batches)))
SyntaxError: multiple statements found while compiling a single statement
branches=[1,2,3]
print(len(branches))
3
batch=["20cys", "21cys","23cys","24cys"]
print(batch[:1])
['20cys']
print(batch[1:3])
['21cys', '23cys']
print(batch[2:])
['23cys', '24cys']
print(batch[:2])
['20cys', '21cys']
batch[1]="apple"
print(batch)
['20cys', 'apple', '23cys', '24cys']
del batch[1]
print(batch)
['20cys', '23cys', '24cys']
del batch[1:3]
print(batch)
['20cys']
print(batch)
['20cys']
num=[1,2,5,7,4,9,3,6,1,2,5]
num.count="2"
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    num.count="2"
AttributeError: 'list' object attribute 'count' is read-only
num.count("2")
0
num.count(2)
2
num.sort()
print(num)
[1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 9]
print(num)
[1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 9]
num.reverse()
print(num)
[9, 7, 6, 5, 5, 4, 3, 2, 2, 1, 1]
num.sort(reverse=True)
print(num)
[9, 7, 6, 5, 5, 4, 3, 2, 2, 1, 1]

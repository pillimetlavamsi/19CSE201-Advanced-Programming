Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
rollno=[46,47,48]
students=["pardhu","vamsi","roopak"]
print(len(students))
3
print(students[0])
pardhu
print(students[1])
vamsi
print(students[2])
roopak
print(students)
['pardhu', 'vamsi', 'roopak']
students.insert(0,"varshit")
print(students)
['varshit', 'pardhu', 'vamsi', 'roopak']
students.append("pavan")
print(students)
['varshit', 'pardhu', 'vamsi', 'roopak', 'pavan']
#removing by using pop()
students.pop(0)
'varshit'
print(students)
['pardhu', 'vamsi', 'roopak', 'pavan']
# removing by using remove
students.remove("pavan")
print(students)
['pardhu', 'vamsi', 'roopak']
#ascending order by using sort()
students.sort()
print(students)
['pardhu', 'roopak', 'vamsi']

#reversing elements by using reverse
students.reverse()
print(students)
['vamsi', 'roopak', 'pardhu']

#arranging elements in descending order by using listname.sort(reverse=True)
students.sort(reverse=True)
print(students)
['vamsi', 'roopak', 'pardhu']

#adding name through insert
print(students)
['vamsi', 'roopak', 'pardhu']
students.insert(3,"kishan")
print(students)
['vamsi', 'roopak', 'pardhu', 'kishan']

#removing name by using del
print(students)
['vamsi', 'roopak', 'pardhu', 'kishan']
del students[3]
print(students)
['vamsi', 'roopak', 'pardhu']
print(students)
['vamsi', 'roopak', 'pardhu']
students.clear()
print(students)
[]
#here we cleared the elements in the list by using clear()
print(students)
[]
del students
print(students)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print(students)
NameError: name 'students' is not defined


#Hence i deleted the students list ,students list is not printed.
from django.test import TestCase

# Create your tests here.
x = -50

with open('ibra.txt', 'w') as f:
    lst = []
    lst.append(x)
    for i in range(100):
        lst.append(i+x)
    f.write(str(lst))
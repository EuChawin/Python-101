Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
box = []
box.append
<built-in method append of list object at 0x000001F5B9D58F00>
(
box.append('pen')
box.append('pencil')
box.append('eraser')
print(box)
['pen', 'pencil', 'eraser']
print(box[0])
pen
print(box[-1])
eraser
print(box[2])
eraser
brand = {'burger':['Mcdonalds','Burger King',"Wendy's"],'pizza':['Pizza Hut','Pizza Company',"Domino's Pizza"]}
print(brand)
{'burger': ['Mcdonalds', 'Burger King', "Wendy's"], 'pizza': ['Pizza Hut', 'Pizza Company', "Domino's Pizza"]}
print(brand['burger'])
['Mcdonalds', 'Burger King', "Wendy's"]
print(brand['burger'][1])
Burger King
>>> print(brand['pizza'][-1])
Domino's Pizza
>>> print(len(brand))
2
>>> print(len(box))
3
>>> print(brand.keys())
dict_keys(['burger', 'pizza'])
>>> print(brand.values())
dict_values([['Mcdonalds', 'Burger King', "Wendy's"], ['Pizza Hut', 'Pizza Company', "Domino's Pizza"]])
>>> for b in box:
...     print(b)
... 
pen
pencil
eraser
>>> for br in brand:
...     print(br)
... 
burger
pizza
>>> for br in brand.values():
...     print(br)
... 
['Mcdonalds', 'Burger King', "Wendy's"]
['Pizza Hut', 'Pizza Company', "Domino's Pizza"]
>>> for br in brand.items():
...     print(br)
... 
('burger', ['Mcdonalds', 'Burger King', "Wendy's"])
('pizza', ['Pizza Hut', 'Pizza Company', "Domino's Pizza"])
>>> len(brand)
2

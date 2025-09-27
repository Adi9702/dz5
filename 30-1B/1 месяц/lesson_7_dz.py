##1 

square = (lambda num: num ** 2)
print(square(3)) 

## 2 

num = [1, 2, 3, 4, 5]
squares = list(map(lambda num: num ** 2, num))
print(list(squares))

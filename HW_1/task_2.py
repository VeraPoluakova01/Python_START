"""
Докажите, что выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно для всех значений предикат.

Вывод: единственное значение типа bool (True либо False)
"""
result = []
for x in True, False:
    for y in True, False:
        for z in True, False:
            result.append(not (x or y or z) == (not x and not y and not z))
print(all(result))

# print(all(
#     (not (x or y or z) == (not x and not y and not z) for x in range(2) for y in range(2) for z in range(2))
# ))


# Еще один способ с внешней библтотекой
# from itertools import product

# print(all(not (x or y or z) == (not x and not y and not z) for x, y, z in product(*((True, False),) * 3, )))

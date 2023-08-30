from array2D import slice_me
family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]
print("\n      TEST 1\n")
print(slice_me(family, 0, 2))
print("\n      TEST 2\n")
print(slice_me(family, 1, -2))
print("\n      TEST 3\n")
family = 10
print(slice_me(family, 0, 2))
print("\n      TEST 4\n")
family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5, 2.15],
          [1.88, 75.2]]
print(slice_me(family, 0, 2))
print("\n      TEST 5\n")
family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]
print(slice_me(family, "a", 2))

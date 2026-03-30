rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("* " * i)




# Alphabet Pyramid

rows = 5

for i in range(rows, 0, -1):
    print(" " * (rows - i), end="")
    
    for j in range(i):
        print(chr(65 + j), end=" ")
    
    print()
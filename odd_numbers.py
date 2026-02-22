odd = []

for i in range(1, 101):
    if i % 2 != 0:
        odd.append(i)

print("Odd Numbers:", odd)
print("Minimum:", min(odd))
print("Maximum:", max(odd))
print("Sum:", sum(odd))




# Odd numbers between 1 to 50

odd_numbers = []

for num in range(1, 51):
    if num % 2 != 0:
        odd_numbers.append(num)

print("List of odd numbers:", odd_numbers)

print("Total three minimum odd numbers:",
      sum(sorted(odd_numbers)[:3]))

print("Total three maximum odd numbers:",
      sum(sorted(odd_numbers)[-3:]))

print("Average of odd numbers:",
      sum(odd_numbers) / len(odd_numbers))
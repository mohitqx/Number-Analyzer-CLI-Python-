even_count = odd_count = count = total = 0
largest_num = smallest_num = None

all_numbers = []
even_numbers = []
odd_numbers = []

while True:
    a = input("Enter value (type 'stop' to terminate): ")

    if a.lower() == "stop":
        break

    if not a.lstrip("-").isdigit():
        print("Invalid input. Please enter a valid number.")
        continue

    b = int(a)
    all_numbers.append(b)

    if b % 2 == 0:
        print("Even")
        even_count += 1
        even_numbers.append(b)
    else:
        print("Odd")
        odd_count += 1
        odd_numbers.append(b)

    total += b
    count += 1

    if largest_num is None or b > largest_num:
        largest_num = b

    if smallest_num is None or b < smallest_num:
        smallest_num = b


print("\n--- Program Terminated ---")
print(f"All numbers      : {all_numbers}")
print(f"Even numbers     : {even_numbers}")
print(f"Odd numbers      : {odd_numbers}")
print(f"Even count       : {even_count}")
print(f"Odd count        : {odd_count}")
print(f"Total sum        : {total}")
print(f"Total entries    : {count}")
print(f"Largest number   : {largest_num}")
print(f"Smallest number  : {smallest_num}")

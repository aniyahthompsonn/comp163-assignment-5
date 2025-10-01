# CHALLENGE 1
print ("=== Challenge 1: Collatz Conjecture ===")

current_number = int(input("Enter starting number: "))
step_count = 0

print ("Sequence:", current_number, end=" ")

while current_number != 1:
    if current_number % 2 == 0:
        current_number = current_number // 2
    else:
        current_number = (current_number * 3) + 1
    print (current_number, end=" ")
    step_count += 1

print ()
print ("Steps:", step_count)
print ()


# CHALLENGE 2
print ("=== Challenge 2: Prime Number Checker ===")

input_num = int(input("Enter a number: "))
print (f"Testing divisors from 2 to {input_num - 1}...")

is_prime = True

for i in range (2, input_num):
    if input_num % i == 0:
        print (f"{input_num} is not prime (divisible by {i})")
        is_prime = False
        break

if is_prime:
    print (f"{input_num} is prime!\n")
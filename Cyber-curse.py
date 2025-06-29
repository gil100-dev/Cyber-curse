def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def number_to_digit_array(number):
    return [int(d) for d in str(number)]

def count_digits_recursive(arr, digit, idx=0, count=0):
    if idx == len(arr):
        return count
    if arr[idx] == digit:
        count += 1
    return count_digits_recursive(arr, digit, idx + 1, count)

def main():
    binary_input = input("Enter a binary number: ")
    decimal_number = binary_to_decimal(binary_input)
    digits_array = number_to_digit_array(decimal_number)
    print("Array:", digits_array)
    for d in range(10):
        count = count_digits_recursive(digits_array, d)
        print(f"Digit {d} appears {count} times")

if __name__ == "__main__":
    main()
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

def decimal_to_binary(n, number_sibiut):
    if n >= 0:
        return format(n, f'0{number_sibiut}b')
    else:
        return format((1 << number_sibiut) + n, f'0{number_sibiut}b')

def main():
    decimal_input = int(input("Enter a decimal number: "))
    number_sibiut = int(input("Enter number of bits: "))

    binary_twos_complement = decimal_to_binary(decimal_input, number_sibiut)

    print(f"Two's complement ({number_sibiut}-bit): {binary_twos_complement}")

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()

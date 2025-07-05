import sys

def word_freqrequency_counter(file_name, top_n):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return

    words = text.split()

    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    sorted_list = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)
    sorted_list = sorted_list[:top_n]
    for item in sorted_list:
        print("Word: " + item[0] + " Appears " + str(item[1]) + " Times")

file_path = "C://Users//GIL//OneDrive//Desktop//Curse cyber//Cyber-curse-clean//words.txt"

try:
    n = int(input("Enter how many top words to display: "))
except ValueError:
    print("You must enter a number.")
    sys.exit(1)

word_freqrequency_counter(file_path, n)

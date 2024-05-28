import sys
def sum_of_digits(n):
    total = 0
    while n > 0:
        total, n = total + n % 10, n // 10
    return total

def longest_unique_sum_sequence_from_file(file_path):
    maxLen = 0
    temp = {}
    i = 0
    j = 0  # Using j as the index
    with open(file_path, 'r') as file:
        for line in file:
            number = int(line.strip())
            sum_digits = sum_of_digits(number)
            if sum_digits in temp and temp[sum_digits] >= i:
                i = temp[sum_digits] + 1
            temp[sum_digits] = j
            maxLen = max(maxLen, j - i + 1)
            j += 1
    return maxLen

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py name.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    print(longest_unique_sum_sequence_from_file(file_path))
numbers = list(map(int, input().split()))
def most_frequent(numbers):
    return max(set(numbers), key=numbers.count)

print(most_frequent(numbers))
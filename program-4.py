def count_multiples(input_list):
    # Initialize the dictionary with keys from 1 to 9 and values set to 0
    multiples_count = {i: 0 for i in range(1, 10)}
    
    # Iterate over the input list and check for multiples
    for num in input_list:
        for i in range(1, 10):
            if num % i == 0:
                multiples_count[i] += 1
    
    return multiples_count

# Example input
input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

# Get the count of multiples
result = count_multiples(input_list)

# Print the result
print(result)

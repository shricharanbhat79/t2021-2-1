def generate_series(a):
    series = []
    # Generate the first (a-1) odd numbers
    for i in range(a-1):
        series.append(2*i + 1)
    
    print(", ".join(map(str, series)))

# Take user input
a = int(input("Enter a number: "))

# Generate and print the series based on the input
generate_series(a)

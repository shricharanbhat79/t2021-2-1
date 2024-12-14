def generate_series(a):
    result = []
    for i in range(a):
        result.append(2 * i + 1)
    return result

# Example usage:
if __name__ == "__main__":
    a = int(input("Enter an integer value (a): "))
    series = generate_series(a)
    print("Generated series:", ", ".join(map(str, series)))

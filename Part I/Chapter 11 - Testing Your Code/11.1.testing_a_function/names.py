from name_function import get_formatted_name

divider = "-" * 25
print("Enter 'q' at any time to quit.")
while True:
    first = input(f"{divider}\nPlease give me a first name:\n\t")
    if first == 'q':
        break
    last = input("Please give me a last name:\n\t")
    if first == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")
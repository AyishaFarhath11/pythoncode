# python code for detecting possible dark patterns and issuing a warning message
import re
def detect_dark_pattern(text):
    dark_pattern_indicators = [
        r'\b(?:limited\s*time\s*offer|exclusive\s*deal|hidden\s*cost)\b',
        r'\b(?:subscribe|sign\s*up|buy\s*now)\b\s*for\s*free',
        # Add more patterns as needed
    ]

    flags = re.IGNORECASE | re.MULTILINE  # You can modify the flags as per your needs

    for pattern in dark_pattern_indicators:
        if re.search(pattern, text, flags=flags):
            return True

    return False

# Example usage:
user_input = input("Enter some text: ")

if detect_dark_pattern(user_input):
    print("Potential dark pattern detected. Please review your input.")
else:
    print("Input seems clean.")

# python detection code for basket sneaking
def count_items(shopping_list, user_order_limit):
    num_items = len(shopping_list)
    print(f"Number of items in the shopping list: {num_items}")

    if num_items > user_order_limit:
        print(f"Warning: You ordered {user_order_limit} items, but there are {num_items} items in your shopping list!")

# Example usage:
user_shopping_list = ['apple', 'banana', 'orange', 'grape']
user_order_limit = 3  # Set the user's order limit

count_items(user_shopping_list, user_order_limit)

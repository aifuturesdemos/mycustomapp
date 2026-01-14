# Updated main.py to fix security vulnerability: replaced eval(input()) with ast.literal_eval(input())
import ast

def main():
    user_input = input("Enter a mathematical expression: ")
    try:
        # Safely evaluate the input as a Python literal
        result = ast.literal_eval(user_input)
        print(f"Result: {result}")
    except (ValueError, SyntaxError):
        print("Invalid input. Please enter a valid mathematical expression.")

if __name__ == "__main__":
    main()

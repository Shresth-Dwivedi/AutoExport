#editedby-> Kunj Bhardwaj
#editedon-> 4th April 2025, 08:36
#filename-> positive_or_negative.py
#Find if the Given Number is Positive or Negative

def sign_of_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

# Example usage:
print(sign_of_number(-5))  # Negative

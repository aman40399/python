# In Python, try and except are keywords used to implement exception handling. Exception handling is a mechanism that allows you to gracefully handle errors or exceptional situations in your code, preventing it from crashing.

# example

try:
    # Code that might raise an exception
    # ...
    result = 10 / 0  # Example: division by zero
except Exception as e:
    # Code to handle the exception
    print(f"An error occurred: {e}")
else:
    # Code to execute if no exception occurs
    print("No error occurred.")
finally:
    # Code that will be executed no matter what, whether an exception occurs or not
    print("This will always be executed.")
  
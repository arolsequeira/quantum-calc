def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
                raise ValueError("Cannot divide by zero")
        return a / b

if __name__ == "__main__":
          while True:
                        try:
                                           expr = input("Enter expression (e.g., 2 + 3) or 'quit': ").strip()
                                                       if expr.lower() == 'quit':
                                                                   break
                                                       parts = expr.split()
                                                       if len(parts) != 3:
                                                                   print("Invalid format")
                                                                                   continue
                                                       x, op, y = parts
                                                       x = float(x)
                                                       y = float(y)
                                                       if op == '+':
                                                                   result = add(x, y)
                                                       elif op == '-':
                                                                   result = subtract(x, y)
                                                       elif op == '*':
                                                                   result = multiply(x, y)
                                                       elif op == '/':
                                                                   result = divide(x, y)
                                                       else:
                                                                   print("Unsupported operator")
                                                                                   continue
                                                       print("Result:", result)
                        except Exception as e:
                                            print("Error:", e)
class Calculator:
    def add(self, op1, op2):
        return op1 + op2

    def subtract(self, op1, op2):
        return op1 - op2

    def multiply(self, op1, op2):
        return op1 * op2

    def divide(self, op1, op2):
        return op1 // op2

    def minimum(self, op1, op2):
        return min(op1, op2)
    
    def average(self, op1, op2):
        return (op1 + op2) // 2

    def power(self, op1, op2):
        return op1 ** op2

    def max(self, op1, op2):
        return max(op1,op2)

    def factorial(self, op):
        if op == 0:
            return 1
        return op * factorial(op - 1)
class Counter:

    def __init__(self, type):
        self.type = type

    def count(self, numberA, numberB):
        if self.type == "+":
            result = numberA + numberB
            return result
        elif self.type == "-":
            result = numberA - numberB
            return result
        elif self.type == "*":
            result = numberA * numberB
            return result
        elif self.type == "/":
            result = numberA / numberB
            return result
        else:
            return None
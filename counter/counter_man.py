from counter import Counter

class CounterMan:
    
    def __init__(self, id, end):
        self.id = id
        self.end = end

    def greet(self):
        print(f"Hi, I am your personal counter man, {self.id}.")
        print("I will help you with complicated mathematical problems.")
        print("If you wish to end this session, press q. Let's start!")

    def take_input(self):
        print("Please present me the formula that I can help you with.")
        formula = input()
        return formula

    def use_counter(self):

        operator_type = " "
        operators = ["+", "-", "*", "/"]
        formula = self.take_input()

        if "q" not in formula:
            for letter in formula:
                for operator in operators:
                    if letter == operator:
                        operator_type = operator
                        break

            if operator_type in operators:
                formula_list = formula.split(operator_type)
                counter = Counter(operator_type)

                result = counter.count(float(formula_list[0]), float(formula_list[1]))
                return round(result, 2)

            else:
                return "ERROR - wrong operator!"
        else:
            self.end = True
            return "end of service."

    def help(self):

        result = self.use_counter()
        print(f"There is your result: {result}")
    

class Calculator:
    variables = dict()
 
    def calc(self, exp):
        exp = exp.replace('---', '-').replace('--', '+')
        exp = exp.replace('+++', '+').replace('++', '+')
        exp = self.change_vars(exp)
        if '//' in exp:
            return 'Invalid Expression'
        try:
            return eval(exp)
        except NameError:
            return 'Unknown variable'
        except Exception:
            if exp.startswith('/'):
                return 'Unknown command'
            return 'Invalid Expression'
 
    def change_vars(self, exp):
        for var in self.variables:
            if var in exp:
                exp = exp.replace(var, self.variables[var])
        return exp
 
    def var_contains_digit(self, var):
        return any(map(str.isdigit, var))
 
    def value_is_digit(self, value):
        return value.isdigit()
 
    def save_var(self, exp):
        exp = exp.replace(' ', '')
        index = exp.index('=')
        var = exp[:index]
        value = exp[index + 1:]
 
        if self.var_contains_digit(var):
            print('Invalid identifier')
            return
        if not value.isdigit() and value not in self.variables:
            print('Invalid assignment')
            return
        if value.isdigit():
            self.variables[var] = value
        else:
            self.variables[var] = self.variables[value]
 
    def main(self):
        while True:
            exp = input()
            if exp == '/help':
                print('The program adds and substtracts numbers')
            elif exp == '/exit':
                print('Bye!')
                break
            elif exp == '':
                continue
            elif '=' in exp:
                self.save_var(exp)
            else:
                result = self.calc(exp)
                if isinstance(result, float):
                    if str(result).split('.')[-1] == '0':
                        print(int(result))
                else:
                    print(result)
 
 
Calculator().main()

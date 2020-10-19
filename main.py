from math import log2


class CalculatorHelper:
    def entropy(self, a, b):
        """
            H[a+, b-] = a / (a + b) log2((a + b)/a) + b / (a + b) log((a + b) / b)
        """
        if a == 0 or b == 0:
            return 0
        if a == b:
            return 1
        return a / (a + b) * log2((a + b) / a) + b / (a + b) * log2((a + b) / b)

    def conditional_entropy(self, a, b, c, d, e, f):
        """ H nod | A = (c + d) / (a + b) * H[c+, d-] + (e + f) / (a + b) * H[e+, f-]"""
        if a == 0 or b == 0:
            return 0
        return (c + d) / (a + b) * self.entropy(c, d) + (e + f) / (a + b) * self.entropy(e, f)

    def ig(self, a, b, c, d, e, f):
        """
            IG = H[a+, b-] - (c + d) / (a + b) * H[c + d] - (e + f) / (a + b) H[e+, f-]
        """
        return self.entropy(a, b) - self.conditional_entropy(a, b, c, d, e, f)


if __name__ == '__main__':

    calc = CalculatorHelper()

    print(0.65 * 6/9)
    print(calc.conditional_entropy(2, 6, 1, 3, 1, 3))

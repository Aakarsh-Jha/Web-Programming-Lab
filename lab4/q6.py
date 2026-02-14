class Power:
    def pow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.pow(x, -n)
        return x * self.pow(x, n - 1)


x = int(input("Enter base value (x): "))
n = int(input("Enter exponent value (n): "))

obj = Power()
print("Result:", obj.pow(x, n))

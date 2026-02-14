class StringManipulation:
    def get_String(self):
        self.str = input("Enter a string: ")

    def print_String(self):
        print(self.str.upper())

obj = StringManipulation()
obj.get_String()
obj.print_String()

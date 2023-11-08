#!/usr/bin/python3
class MyInt(int):
    def __eq__(self, other):
        # Invert the behavior of the equality operator (==)
        return not super().__eq__(other)

    def __ne__(self, other):
        # Invert the behavior of the inequality operator (!=)
        return not super().__ne__(other)

# Example usage:
x = MyInt(5)
y = MyInt(5)

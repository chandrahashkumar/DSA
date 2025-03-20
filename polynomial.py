class Node:
    def __init__(self, coeff, expo):
        self.coeff = coeff    # Coefficient of the term
        self.expo = expo      # Exponent of the term
        self.next = None      # Pointer to the next term

class Polynomial:
    def __init__(self):
        self.head = None  # Start with an empty polynomial

    def add_term(self, coeff, expo):
        """
        Add a new term to the polynomial in descending order of exponent.
        If a term with the same exponent exists, update its coefficient.
        """
        new_node = Node(coeff, expo)
        # If the list is empty or the new term has a higher exponent than the head
        if self.head is None or self.head.expo < expo:
            new_node.next = self.head
            self.head = new_node
            return

        # Traverse to find the correct insertion point
        current = self.head
        prev = None
        while current and current.expo >= expo:
            # If a term with the same exponent is found, update the coefficient.
            if current.expo == expo:
                current.coeff += coeff
                return
            prev = current
            current = current.next

        # Insert the new term between prev and current
        new_node.next = current
        prev.next = new_node

    def evaluate(self, x):
        """
        Evaluate the polynomial for a given value of x.
        """
        result = 0
        current = self.head
        while current:
            result += current.coeff * (x ** current.expo)
            current = current.next
        return result

    def display(self):
        """
        Display the polynomial in human-readable form.
        """
        terms = []
        current = self.head
        while current:
            # Format the term (e.g., "3x^2", "5x", or "4")
            if current.expo == 0:
                term_str = f"{current.coeff}"
            elif current.expo == 1:
                term_str = f"{current.coeff}x"
            else:
                term_str = f"{current.coeff}x^{current.expo}"
            terms.append(term_str)
            current = current.next
        # Join terms with " + " while handling negative coefficients properly.
        polynomial_str = " + ".join(terms)
        # Optionally replace "+ -" with "- " for a cleaner look.
        polynomial_str = polynomial_str.replace("+ -", "- ")
        print(polynomial_str)

# Example usage:
if __name__ == "__main__":
    poly = Polynomial()
    # Suppose we want to represent the polynomial 3x^3 + 2x^2 - 5x + 6.
    poly.add_term(3, 3)
    poly.add_term(2, 2)
    poly.add_term(-5, 1)
    poly.add_term(6, 0)

    print("Polynomial:")
    poly.display()

    x_value = 2
    print(f"Value of polynomial at x = {x_value} is {poly.evaluate(x_value)}")

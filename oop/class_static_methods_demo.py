class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: performs addition without accessing class or instance data."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: performs multiplication and accesses a class-level attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

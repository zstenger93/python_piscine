class calculator:
    """
    belongs to a class rather than an instance of the class.
    It does not operate on the instance's state and does not
    have access to instance-specific data or methods.
    Static methods are often used for utility functions that
    are related to the class in some way but do not depend
    on instance-specific attributes.

    You can call it on the class itself without creating
    an instance of the class
    """
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculate and print the dot product of two vectors.
        """
        dot_product = 0.0
        for i in V1:  # Assuming V1 and V2 have the same length
            dot_product += i * V2[V1.index(i)]
        print(f"Dot product is: {int(dot_product)}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Add two vectors element-wise and print the result vector.
        """
        result = []
        for i in V1:  # Assuming V1 and V2 have the same length
            result.append(i + V2[V1.index(i)])
        print(f"Add Vector is : {[f'{val:.1f}' for val in result]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtract two vectors element-wise and print the result vector.
        """
        result = []
        for i in V1:  # Assuming V1 and V2 have the same length
            result.append(i - V2[V1.index(i)])
        print(f"Sous Vector is: {[f'{val:.1f}' for val in result]}")

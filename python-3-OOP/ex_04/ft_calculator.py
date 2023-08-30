class calculator:
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> float:
        """
        Calculate and print the dot product of two vectors.
        """
        dot_product = 0.0
        for i in V1:  # Assuming V1 and V2 have the same length
            dot_product += i * V2[V1.index(i)]
        print(f"Dot product is: {dot_product:.1f}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> list[float]:
        """
        Add two vectors element-wise and print the result vector.
        """
        result = []
        for i in V1:  # Assuming V1 and V2 have the same length
            result.append(i + V2[V1.index(i)])
        print(f"Add Vector is : {[f'{val:.1f}' for val in result]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> list[float]:
        """
        Subtract two vectors element-wise and print the result vector.
        """
        result = []
        for i in V1:  # Assuming V1 and V2 have the same length
            result.append(i - V2[V1.index(i)])
        print(f"Sous Vector is: {[f'{val:.1f}' for val in result]}")

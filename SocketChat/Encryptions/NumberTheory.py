import random


class NumberTheory:
    def __init__(self):
        pass

    def mod_inverse(self, a, m):
        """
        Calculates the modular inverse of a modulo m using either Fermat's Little Theorem
        or the Extended Euclidean Algorithm.

        Args:
            a: The integer for which to find the inverse.
            m: The modulus.

        Returns:
            The modular inverse of a modulo m, or None if no inverse exists.

        Raises:
            ValueError: If m is not a positive integer or if a and m are not coprime
                        (for Fermat's Little Theorem method).
        """

        if m <= 1:
            raise ValueError("Modulus (m) must be a positive integer greater than 1.")

        # Attempt using Fermat's Little Theorem (faster for prime modulus)
        try:
            return self.mod_inverse_fermat(a, m)
        except ValueError:
            pass  # Fallback to Extended Euclidean Algorithm

        # Use Extended Euclidean Algorithm for general cases
        return self.mod_inverse_eea(a, m)

    def mod_inverse_fermat(self, a, m):
        """
        Calculates the modular inverse of a modulo m using Fermat's Little Theorem.

        Args:
            a: The integer for which to find the inverse.
            m: The modulus (prime number).

        Returns:
            The modular inverse of a modulo m, or None if no inverse exists.

        Raises:
            ValueError: If m is not a prime number or if a and m are not coprime.
        """
        if m % 2 == 0 and a % 2 == 0:
            raise ValueError("No inverse exists if both a and m are even.")

        # Check if m is prime (more robust primality testing recommended)
        # You can replace this with a better primality test function
        if m == 3 or m == 2:
            return a
        if not m % 2 == 0 and not m % 3 == 0:
            d = m - 1
            while d % 2 == 0:
                d //= 2
        else:
            raise ValueError("Modulus (m) must be prime for this method.")

        # Fermat's Little Theorem: a^(m-1) ≡ 1 (mod m)
        inverse = pow(a, d, m)  # a^(m-1) calculated efficiently using pow
        return inverse

    def extended_euclidean_algorithm(self, a, b):
        """
        Implements the Extended Euclidean Algorithm to find GCD and Bezout coefficients.

        Args:
            a: The first integer.
            b: The second integer.

        Returns:
            A tuple containing the GCD (gcd), x coefficient (x), and y coefficient (y).
        """
        if b == 0:
            return a, 1, 0
        else:
            gcd, x, y = self.extended_euclidean_algorithm(b, a % b)
            return gcd, y, (x - (a // b) * y)

    def mod_inverse_eea(self, a, m):
        """
        Calculates the modular inverse of a modulo m using the Extended Euclidean Algorithm.

        Args:
            a: The integer for which to find the inverse.
            m: The modulus.

        Returns:
            The modular inverse of a modulo m, or None if no inverse exists.

        Raises:
            ValueError: If a and m are not coprime.
        """
        gcd, x, y = self.extended_euclidean_algorithm(a, m)
        if gcd != 1:
            raise ValueError("No modular inverse exists if a and m are not coprime.")
        return x % m  # Reduce x within the range of the modulus

    def gcd(self, a, b):
        """
        Calculates the greatest common divisor (GCD) of two integers.

        Args:
            a: The first integer.
            b: The second integer.

        Returns:
            The GCD of a and b.
        """
        while b != 0:
            a, b = b, a % b
        return a

    def get_coprime_number(self, m):
        """
        Calculates a coprime number less than m
        """
        x = m
        while self.gcd(x, m) != 1:
            x = random.randint(1, m - 1)
        return x

    def binary_exponentiation(self, a, b, mod):
        """
        Calculates a raised to the power of b efficiently using binary exponentiation.

        Args:
            a: The base number.
            b: The exponent (power).
            mod: The modulus.

        Returns:
            a raised to the power of b.
        """
        result = 1
        while b > 0:
            # Check if the least significant bit of b is 1
            if b & 1:
                result = (result * a) % mod  # Efficient multiplication with modulo

            # Square the base and right shift the exponent
            a = (a * a) % mod
            b >>= 1  # Same as b // 2, but faster

        return result

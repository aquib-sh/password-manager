import random
from string import ascii_letters


class OTPGenerator:
    """Generates OTP of alpha-numeric, numeric and character types."""

    def __init__(self, length=5):
        """
        Parameters
        ----------
        length: int
            Length of OTP to generate
        """
        self.OTP_LENGTH = length
        self.INT_START = 0
        self.INT_END = 10

    def generate_alpha_numeric_otp(self) -> str:
        """Generates alpha numeric otp

        Returns
        -------
        :str
            String of random alpha numeric characters.
        """
        otp = ""
        i = 0

        while i < self.OTP_LENGTH:
            result = random.randint(0, 2)
            # if result is 0 them add a random letter else add a random digit
            if result == 0:
                otp += random.choice(ascii_letters)
            else:
                otp += str(random.randint(self.INT_START, self.INT_END))
            i += 1

        return otp

    def generate_numeric_otp(self) -> str:
        """Generates numeric otp

        Returns
        -------
        :str
            String of random numeric characters.
        """
        otp = ""
        i = 0

        while i < self.OTP_LENGTH:
            otp += str(random.randint(self.INT_START, self.INT_END))
            i += 1

        return otp

    def generate_alpha_otp(self) -> str:
        """Generates alphabetic otp

        Returns
        -------
        :str
            String of random alphabetic characters.
        """
        otp = ""
        i = 0

        while i < self.OTP_LENGTH:
            otp += random.choice(ascii_letters)
            i += 1

        return otp

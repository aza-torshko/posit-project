import base64

class Credentials:
    """Stores test data, including encrypted credentials."""
    
    EMAIL = "azatorshko@gmail.com"  # Plain text email
    ENCRYPTED_PASSWORD = "QXphVmF6YTMzNzc="  # Base64 encoded password

    @staticmethod
    def decrypt_data(encrypted_value: str) -> str:
        """Decrypts Base64 encoded credentials."""
        return base64.b64decode(encrypted_value).decode("utf-8")

    @classmethod
    def get_email(cls):
        return cls.EMAIL

    @classmethod
    def get_password(cls):
        return cls.decrypt_data(cls.ENCRYPTED_PASSWORD)

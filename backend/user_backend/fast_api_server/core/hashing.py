import bcrypt

# bcrypt only reads the first 72 bytes; longer passwords are rejected, not truncated
MAX_PASSWORD_BYTES = 72


class Hasher:
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())

    @staticmethod
    def get_password_hash(password):
        password_bytes = password.encode()
        if len(password_bytes) > MAX_PASSWORD_BYTES:
            raise ValueError(f"Password is longer than {MAX_PASSWORD_BYTES} bytes")
        return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode()

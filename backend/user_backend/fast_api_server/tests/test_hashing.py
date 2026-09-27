import pytest

from core.hashing import Hasher, MAX_PASSWORD_BYTES

# Made by passlib 1.7.4 + bcrypt 4.0.1, the stack the old code used.
PASSLIB_HASH = "$2b$12$be.ucCfsjH/G2kuiW3HcS..yQhcs0qKwFKbwrpdj6olA.MaUsBQXG"


def test_hash_then_verify():
    hashed = Hasher.get_password_hash("secret-password")
    assert Hasher.verify_password("secret-password", hashed)


def test_wrong_password_fails():
    hashed = Hasher.get_password_hash("secret-password")
    assert not Hasher.verify_password("other-password", hashed)


def test_old_passlib_hash_still_verifies():
    assert Hasher.verify_password("fixture-password", PASSLIB_HASH)


def test_too_long_password_is_rejected():
    with pytest.raises(ValueError):
        Hasher.get_password_hash("x" * (MAX_PASSWORD_BYTES + 1))

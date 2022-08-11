import passphrase_generator
import pytest


def test_empty_random_passphrase():
    """Tests the passphrase_generator.random_passphrase() function to verify
    a string is returned.
    """

    random_passphrase = passphrase_generator.random_passphrase()

    if random_passphrase != "":
        assert True
    else:
        assert False


def test_empty_passphrase_strength():
    """Tests the passphrase_generator.passphrase_strength() function to verify
    a string is returned.
    """

    passphrase_strength = passphrase_generator.passphrase_strength("Test")

    if passphrase_strength != "":
        assert True
    else:
        assert False


if __name__ == "__main__":
    test_empty_random_passphrase()
    test_empty_passphrase_strength()

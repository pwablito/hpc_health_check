import pyotp


def get_totp_code(seed):
    return pyotp.TOTP(seed).now()

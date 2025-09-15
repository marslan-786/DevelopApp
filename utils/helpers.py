import random

def generate_otp(length: int = 6):
    return ''.join(random.choices('0123456789', k=length))

def format_datetime(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")
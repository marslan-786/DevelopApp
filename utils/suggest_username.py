import random
import string

def suggest_username(base_username: str, n: int = 3):
    suggestions = []
    for _ in range(n):
        suffix = ''.join(random.choices(string.digits, k=4))
        suggestions.append(f"{base_username}{suffix}")
    return suggestions
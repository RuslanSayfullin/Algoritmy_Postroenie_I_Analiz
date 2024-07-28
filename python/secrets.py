import secrets
import string

# From the docs
alphabet = string.ascii_letters + string.digits
password = "".join(secrets.choice(alphabet) for _ in range(10))

print(password)
print(secrets.token_urlsafe())
print(secrets.token_hex())

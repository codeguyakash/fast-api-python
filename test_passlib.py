from passlib.context import CryptContext

try:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    hashed = pwd_context.hash("testpassword")
    print(f"Hash successful: {hashed}")
    print(f"Verify successful: {pwd_context.verify('testpassword', hashed)}")
except Exception as e:
    print(f"Error: {e}")

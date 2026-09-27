def login(username, password):
    # authentication logic with hashing
    hashed = hash_password(password)
    if username == "admin" and hashed == HASHED_ADMIN_PW:
        return True
    return False
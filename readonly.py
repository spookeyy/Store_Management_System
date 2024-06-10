from store_mgt_CLI_app.readonly import ReadOnly

class Config:
    MAX_USERS = ReadOnly(100)
    MIN_AGE = ReadOnly(18)

# After assignment, MAX_USERS cannot be changed:
# config.MAX_USERS = 200  # This will raise an error
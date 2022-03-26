import os

# ======================= DATABASE FILE  =============================
DATA_DIR = os.path.join(os.getcwd(), "internal")
DB_FILE = "password_manager.db"
DB_PATH = os.path.join(DATA_DIR, DB_FILE)

# ======================= GOOGLE APIs =============================
GOOGLE_TOKEN_FILE  = "final_token.json"
CLIENT_SECRET_FILE = "client_secret.json"

CLIENT_SECRET_PATH    = os.path.join(DATA_DIR, CLIENT_SECRET_FILE)
GOOGLE_API_TOKEN_PATH = os.path.join(DATA_DIR, GOOGLE_TOKEN_FILE)

GOOGLE_API_SCOPE = ["https://www.googleapis.com/auth/gmail.modify"]

APP_EMAIL = "passvault.manager@gmail.com"
# ====================== FORMAT FOR OTP ===========================
OTP_MSG = "Hello {user} your OTP for Pass Vault is {otp}"

# ====================== DISPLAY MSGS ========================
ENTER_OTP_MSG = "OTP has been sent to {email},\nPlease enter OTP here."
INCORRECT_OTP_MSG = "Incorrect OTP!"
REG_SUCESS_MSG = "Sucessfully Registered on PassVault!,\nPlease close this window and proceeed with login"
PASSWORD_MISMATCH_MSG = "Passwords do not match, Please check the passwords and try again."

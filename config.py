import os

# ======================= DATABASE FILE  =============================
data_dir = os.path.join(os.getcwd(), "internal")
db_file = "password_manager.db"
db_path = os.path.join(data_dir, db_file)

# ======================= GOOGLE APIs =============================
google_token_file  = "final_token.json"
client_secret_file = "client_secret.json"

client_secret_path    = os.path.join(data_dir, client_secret_file)
google_api_token_path = os.path.join(data_dir, google_token_file)

google_api_scope = ["https://www.googleapis.com/auth/gmail.modify"]

# ====================== FORMAT FOR OTP ===========================
OTP_MSG = "Hello {user} your OTP for Pass Vault is {otp}"

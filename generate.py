# Script to generate a Google token
import config
from services.google.token import TokenGenerator

gtr = TokenGenerator()
creds = gtr.generate_google_api_token(
    client_secret=config.CLIENT_SECRET_PATH, scopes=config.GOOGLE_API_SCOPE
)

gtr.export_token(creds, config.GOOGLE_API_TOKEN_PATH)

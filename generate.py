# Script to generate a Google token
import config
from services.google.token import TokenGenerator

gtr = TokenGenerator()
creds = gtr.generate_google_api_token(
    client_secret=config.client_secret_path, scopes=config.google_api_scope
)

gtr.export_token(creds, config.google_api_token_path)

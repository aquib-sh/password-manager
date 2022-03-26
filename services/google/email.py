import base64
from services.google.google_services import GoogleServices
from email.mime.text import MIMEText
from googleapiclient import errors


class Gmail(GoogleServices):
    """Handles Gmail API events and methods.

    Inherited Parameters from GoogleService
    -----------------------------------------
    token
        Token of the current session.

    scope: list
        Scope of the current token.
    """

    def __init__(self, token, scope: list):
        super().__init__(token, scope)

    def start_service(self, version="v1"):
        """Builds Gmail Service."""
        super(Gmail, self).start_service("gmail", version)
        return self.service

    def create_message(self, sender, to, subject, message_text):
        """Create a message for an email.

        Parameters
        ----------
        sender: str
            Email address of the sender.

        to: str
            Email address of the receiver.

        subject: str
            The subject of the email message.

        message_text
            The text of the email message.

        Returns
        -------
        An object containing a base64url encoded email object.
        """
        message = MIMEText(message_text)
        message["to"] = to
        message["from"] = sender
        message["subject"] = subject
        raw = base64.urlsafe_b64encode(message.as_bytes())
        return {"raw": raw.decode()}

    def send_message(self, message, user_id="me", service=None):
        """Send an email message.

        Parameters
        ----------
        service   (Default=self.service)
          Authorized Gmail API service instance.

        user_id: str  (Default="me")
          User's email address. The special value "me"
          can be used to indicate the authenticated user.

        message
          Message to be sent, must be a base64url encoded object.

        Returns
        -------
        Sent Message.
        """
        if service == None:
            service = self.service

        try:
            message = (
                service.users().messages().send(userId=user_id, body=message).execute()
            )
            print("Message Id: %s" % message["id"])
            return message

        except errors.HttpError as error:
            print("An error occurred: %s" % error)

        except Exception as error:
            print("An error occurred: %s" % error)

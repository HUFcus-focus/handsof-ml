from slack_sdk import WebClient

from src.core import get_settings


class Worker:
    """
    Slack API Worker Class
    """

    def __init__(self) -> None:
        self.client: WebClient = WebClient(token=get_settings().SLACK_TOKEN)

    def oauth_access(self, auth_code: str):
        """ """
        response = self.client.oauth_v2_access(
            client_id=get_settings().SLACK_CLIENT_ID,
            client_secret=get_settings().SLACK_CLIENT_SECRET,
            code=auth_code,
        )

        return response

    def get_channels(self) -> list[dict[str, str]] | dict:
        """
        Get Slack Channels
        """
        response = self.client.conversations_list(
            types="public_channel,private_channel"
        )
        if response["ok"]:
            result: list[dict[str, str]] = []
            for channel in response["channels"]:
                result.append({"id": channel["id"], "name": channel["name"]})

            return result

        else:
            return response

    def get_users(self) -> list[dict[str, str]] | dict:
        """
        Get Users in Slack Channel
        """
        response = self.client.users_list()

        if response["ok"]:
            result: list[dict[str, str]] = []
            for user in response["members"]:
                if not user["is_bot"] and user["name"] != "slackbot":
                    result.append(
                        {
                            "id": user["id"],
                            "real_name": user["profile"]["real_name"],
                            "display_name": user["profile"]["display_name"],
                        }
                    )

            return result

        else:
            return response

    def send_message(self, destination: str, message: str):
        """
        Send Message to Slack
        """
        self.client.chat_postMessage(
            channel=destination,
            blocks=[
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "plain_text",
                            "text": "핸즈오프 앱으로 발송된 메세지입니다. :raised_hands:",
                            "emoji": True,
                        }
                    ],
                },
                {"type": "divider"},
                {
                    "type": "section",
                    "text": {"type": "plain_text", "text": message},
                },
            ],
        )

        return

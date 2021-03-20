import requests

class discord_webhook:

    def __init__(self, url):
        self.url = url
        self.webhook_data = {}

    def setContent(self, content):
        self.webhook_data["content"] = content

    def setName(self, name):
        self.webhook_data["username"] = name

    def setAvatar(self, avatar):
        self.webhook_data["avatar_url"] = avatar

    def setEmbed(self, title, description, color):
        self.webhook_data["embeds"] = [{"title": title,"description": description,"color": color}]

    def send(self):
        requests.post(self.url, json=self.webhook_data)

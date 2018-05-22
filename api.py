from linebot import (LineBotApi, WebhookHandler)

# https://developers.line.me/console/
# Channel Access Token
line_bot_api = LineBotApi('Channel access token')
# Channel Secret
handler = WebhookHandler('Channel secret')

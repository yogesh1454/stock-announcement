import requests

# Telegram bot token
bot_token = '6505130235:AAHMVIPUP5OE21SKr88Tpr_TAaw0ciuX_18'

def send_telegram_message(chat_id, text, parse_mode=None):
    """Function to send a message to Telegram"""
    api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': parse_mode
    }
    print('Sending msg to telegram', text)
    response = requests.post(api_url, data=params)
    return response.json()

def format_message(header, body, link_text, link_url):
    """Function to format a message with header, body, and hyperlink"""
    message = f"<b>{header}</b>\n\n{body}\n<a href='{link_url}'>{link_text}</a>"
    return message

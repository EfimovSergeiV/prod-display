"""
Mattermost notification
"""


import requests
from django.template import Template, Context
from main.conf import BOT_TOKEN, MATTERMOST_URL, CHANNEL_ID


headers = {
    'Authorization': f'Bearer {BOT_TOKEN}',
    'Content-Type': 'application/json'
}

def send_message(channel_id, message):
    url = f'{MATTERMOST_URL}/api/v4/posts'
    payload = {
        'channel_id': channel_id,
        'message': message
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        print("Сообщение успешно отправлено!")
    else:
        print(f"Ошибка отправки сообщения: {response.status_code} - {response.text}")



# Шаблоны сообщений

templates = {

"draw_completed" : """
**{{ now_time }}** - **{{ name }}** помечен как выполненный.
""",


"request_template" : """


""",


"message_template" : """


""",


"order_template" : """


""",
}


# Данные для сообщений для отладки

request_data = {}
message_data = {}
order_data = {}
one_click_order_data = {}


def mattermost_notification(template, data):
    context = Context(data)
    template = Template(templates[template])

    rendered_string = template.render(context)
    send_message(CHANNEL_ID, rendered_string)
""" Запуск приложений """
import os, requests
import subprocess

# Установка переменной окружения DISPLAY
os.environ["DISPLAY"] = ":0"

server_status = requests.get("http://mon1.local:8080/").status_code
client_status = requests.get("http://mon1.local/").status_code

print(server_status, client_status)

# subprocess.run(["firefox-esr --kiosk http://mon1.local"])
# Запускаем firefox в режиме 

# os.system("firefox-esr --kiosk http://mon1.local:8000")
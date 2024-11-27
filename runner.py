""" Запуск приложений """
import os, requests
import subprocess

# Установка переменной окружения DISPLAY
os.environ["DISPLAY"] = ":0"

server_status = requests.get("http://mon1.local:8080/").status_code
client_status = requests.get("http://mon1.local/").status_code

print('СТАТУС СЕРВЕРОВ: ', server_status, client_status)


if server_status == 200 and client_status == 200:
    
    subprocess.run(["firefox-esr --kiosk http://mon1.local"])







# os.system("firefox-esr --kiosk http://mon1.local:8000")
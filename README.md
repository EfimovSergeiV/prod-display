### Аппаратная часть

Микрокомпьютер Raspberry Pi 4 Model B
https://www.dns-shop.ru/product/a7af3b3d38283332/mikrokomputer-raspberry-pi-4-model-b/
13 499 ₽

БЛОК ПИТАНИЯ
выходное напряжение - 5.1В, выходной ток - 2.5А,

Карта памяти Kingston Canvas Select Plus microSDXC 64 ГБ
https://www.dns-shop.ru/product/28f87a399e421b80/karta-pamati-kingston-canvas-select-plus-microsdxc-64-gb-sdcs264gb/
750 ₽

Корпус для микрокомпьютера ACD RA460
https://www.dns-shop.ru/product/cedfb5afa14a2ff4/korpus-dla-mikrokomputera-acd-ra460-ra460-cernyj/
1 150 ₽

21.5" Монитор ASUS VT229H, 1920x1080, IPS, 1хHDMI
https://www.citilink.ru/product/monitor-asus-21-5-vt229h-chernyi-ips-16-9-hdmi-m-m-mat-250cd-touch-1363561/
27 890 ₽

== 43289 ₽



### Настройка ОС

```bash
# GNOME + GDM

# Для автоматического входа в GDM на Debian:
sudo nano /etc/gdm3/daemon.conf

# Найдите строку [daemon] и добавьте или измените следующие параметры:
AutomaticLoginEnable=true
AutomaticLogin=<your_username>

nano ~/.config/autostart/chrome-fullscreen.desktop

[Desktop Entry]
Type=Application
Exec=google-chrome --kiosk
Hidden=false
X-GNOME-Autostart-enabled=true
Name=Chrome Fullscreen
```






```bash
sudo nano /etc/lightdm/lightdm.conf

# Найдите секцию [Seat:*] и добавьте или измените строки:
autologin-user=<your_username>
autologin-user-timeout=0

mkdir -p ~/.config/autostart
nano ~/.config/autostart/firefox-fullscreen.desktop

[Desktop Entry]
Type=Application
Exec=firefox --kiosk
Hidden=false
X-LXDE-Autostart-enabled=true
Name=Firefox Fullscreen


sudo nano /etc/default/grub
GRUB_TIMEOUT=0

sudo update-grub
```



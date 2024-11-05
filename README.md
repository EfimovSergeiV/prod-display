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



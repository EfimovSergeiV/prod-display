Крепление для мониторов DEXP Fence LDT63-C012GL
https://www.dns-shop.ru/product/68280fe7e455d6b2/kreplenie-dla-monitorov-dexp-fence-ldt63-c012gl/
3 499 ₽


===
Бюджетное решение (управление мышью)

Mini PC Intel Pentium
https://aliexpress.ru/item/1005003096277756.html?sku_id=12000029991121971&spm=a2g2w.productlist.search_results.8.10b816b24mXadi
8 170 ₽

27" Монитор Digma Progress 27P404F черный
https://www.dns-shop.ru/product/692f3f1cb12b4a84/27-monitor-digma-progress-27p404f-cernyj/
11 299 ₽

Мышь беспроводная Acer OMR010 черный
https://www.dns-shop.ru/product/4326c510ee853332/mys-besprovodnaa-acer-omr010--cernyj/
500 ₽

23470 ₽
===

===
Бюджетное решение (Сенсорное управление) (требует аккуратного обращения)

Mini PC Intel Pentium
https://aliexpress.ru/item/1005003096277756.html?sku_id=12000029991121971&spm=a2g2w.productlist.search_results.8.10b816b24mXadi
8 170 ₽

21.5" Монитор ASUS VT229H, 1920x1080, IPS, 1хHDMI
https://www.citilink.ru/product/monitor-asus-21-5-vt229h-chernyi-ips-16-9-hdmi-m-m-mat-250cd-touch-1363561/
27 890 ₽

39560 ₽
===

===
IFC-521WC - промышленный панельный компьютер 21.5"
https://www.rusavtomatika.com/ifc/IFC-521WC/
1700 usd === 170 670руб

174300 ₽
===



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

```bash
#Настроить безпарольный доступ для конкретной команды

sudo visudo
username ALL=(ALL) NOPASSWD: /usr/sbin/shutdown

```
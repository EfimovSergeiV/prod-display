# API

## Base URL
http://mon1.local:8080


**URL:** `/d/draw/`
- **Методы:** `GET`, `POST`, `PUT`, `DELETE`

**Запрос:**

- **Method:** `GET`


**Ответ:**
- **Status Code:** `200 OK`
- **Content type:** `application/json`
```json
[
    {
        "uuid": "string",
        "name": "string",
        "status": "string",
        "created_at": "string",
        "link": null,
        "pdf": "string",
        "webp": "string",
        "webp_size": {
            "width": 0,
            "height": 0
        },
        "prw": "string"
    },
    {
        "uuid": "string",
        "name": "string",
        "status": "string",
        "created_at": "string",
        "link": null,
        "pdf": "string",
        "webp": "string",
        "webp_size": {
            "width": 0,
            "height": 0
        },
        "prw": "string"
    },
]

```

**Query Parameters:**
| Параметр    | Тип     | Обязательный | Автоматический | Описание                          |
|-------------|---------|--------------|----------------|-----------------------------------|
| `uuid`      | `str`   | Да           | Да             | Уникальный дентификатор документа |
| `name`      | `str`   | Да           | Да             | Отображаемое название документа   |
| `status`    | `str`   | Нет          | Да             | Статус объекта                    |
| `created_at`| `str`   | Нет          | Да             | Дата записи в базу данных         |
| `link`      | `str`   | Нет          | Нет            | Ссылка на PDF в хранилище         |
| `pdf`       | `str`   | Да           | Нет            | Путь до PDF документа             |
| `webp`      | `str`   | Да           | Да             | Путь до изображения               |
| `webp_size` | `obj`   | Да           | Да             | Размер изображения в пикселях     |
| `prw`       | `str`   | Да           | Да             | Путь до изображения превью        |



```bash
# POST
# Запись нового объекта в БД





```

```bash
# PUT
# Обновляет статус объекта




```

```bash
# DELETE
# Удаление объекта из БД




```


### Ошибки на промышленных ПК

```log
ACPI BIOS Error (bug): Could not resolve symbol [\_SB._OSC.CDW1].
AE_NOT_FOUND
ACPI Error: Aborting method \_SB._OSC due to previous error (AE_NOT_FOUND)
```

```bash
sudo nano /etc/default/grub

GRUB_DEFAULT=0
GRUB_TIMEOUT=0
GRUB_DISTRIBUTOR=`lsb_release -i -s 2> /dev/null || echo Debian`
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash loglevel=0"
GRUB_CMDLINE_LINUX=""

sudo update-grub
```
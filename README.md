# Mukammal Telegram Bot

Aiogram 3.x asosida yaratilgan mukammal, modular arxitekturali Telegram bot shablon (template).

## Texnologiyalar

- **Python** 3.10+
- **Aiogram** 3.x (asinxron Telegram Bot framework)
- **Environs** (muhit o'zgaruvchilarini boshqarish)
- **Cachetools** (throttling uchun kesh)

## Loyiha strukturasi

```
.
├── app.py                      # Asosiy ishga tushirish fayli
├── loader.py                   # Bot, Dispatcher, Storage yaratish
├── requirements.txt            # Kutubxonalar ro'yxati
├── .env.example                # Muhit o'zgaruvchilari namunasi
├── .gitignore                  # Git tomonidan e'tiborga olinmaydigan fayllar
│
├── data/
│   ├── __init__.py
│   └── config.py               # BOT_TOKEN, ADMINS sozlamalari
│
├── handlers/
│   ├── __init__.py             # Asosiy router
│   ├── users/
│   │   ├── __init__.py         # Users routerini yig'ish
│   │   ├── start.py            # /start buyrug'i
│   │   ├── help.py             # /help buyrug'i
│   │   └── about.py            # /about buyrug'i
│   ├── groups/
│   │   └── __init__.py         # Guruh handlerlari (kengaytirish uchun)
│   ├── channels/
│   │   └── __init__.py         # Kanal handlerlari (kengaytirish uchun)
│   └── errors/
│       ├── __init__.py
│       └── error_handler.py    # Barcha xatolarni ushlovchi handler
│
├── keyboards/
│   ├── __init__.py
│   ├── inline/
│   │   └── __init__.py         # Inline tugmalar
│   └── reply/
│       └── __init__.py         # Reply tugmalar
│
├── middlewares/
│   ├── __init__.py
│   └── throttling.py           # Spam himoyasi (throttling)
│
├── states/
│   └── __init__.py             # FSM holatlar (kengaytirish uchun)
│
├── filters/
│   └── __init__.py             # Maxsus filterlar (kengaytirish uchun)
│
├── database/
│   └── __init__.py             # Ma'lumotlar bazasi (kengaytirish uchun)
│
├── services/
│   └── __init__.py             # Biznes logika (kengaytirish uchun)
│
├── text/
│   └── __init__.py             # Matnlar va xabarlar (kengaytirish uchun)
│
└── utils/
    ├── __init__.py
    ├── notify_admins.py        # Adminlarga xabar yuborish
    ├── set_bot_commands.py     # Bot buyruqlarini o'rnatish
    └── misc/
        ├── __init__.py
        ├── logging.py          # Logger sozlamalari
        └── throttling.py       # rate_limit dekoratori
```

## O'rnatish

### 1. Repositoriyani klonlash

```bash
git clone https://github.com/nozim4716171/mukammal_telegram_bot.git
cd your-repo
```

### 2. Virtual muhit yaratish

```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows
```

### 3. Kutubxonalarni o'rnatish

```bash
pip install -r requirements.txt
```

### 4. Muhit o'zgaruvchilarini sozlash

`.env.example` faylini `.env` ga nusxalang va o'z ma'lumotlaringizni kiriting:

```bash
cp .env.example .env
```

`.env` fayl ichida:

```env
BOT_TOKEN=your_bot_token_here
ADMINS=123456789,987654321
```

- **BOT_TOKEN** — [@BotFather](https://t.me/BotFather) dan olingan token
- **ADMINS** — Admin foydalanuvchilar ID lari (vergul bilan ajratilgan)

### 5. Botni ishga tushirish

```bash
python app.py
```

## Bot buyruqlari

| Buyruq | Tavsif |
|--------|--------|
| `/start` | Botni ishga tushirish |
| `/help` | Yordam va buyruqlar ro'yxati |
| `/about` | Bot haqida ma'lumot |

## Asosiy xususiyatlar

- **Modular arxitektura** — har bir funksional qism alohida papkada
- **Throttling (spam himoyasi)** — foydalanuvchilar spamdan himoyalangan
- **Error handling** — barcha Telegram API xatolari ushlanadi va loglanadi
- **Admin notifikatsiyalar** — bot ishga tushganda/to'xtaganda adminlarga xabar
- **FSM (Finite State Machine)** — MemoryStorage orqali holatlarni boshqarish
- **rate_limit dekoratori** — har bir handler uchun alohida throttling limit

## rate_limit ishlatish

Handlerda throttling limitni sozlash:

```python
from utils.misc.throttling import rate_limit

@router.message(Command("catalog"))
@rate_limit(limit=3)  # 3 soniya limit
async def catalog_command(message: Message):
    await message.answer("Katalog...")
```

## Loyihani kengaytirish

| Papka | Qo'shish mumkin |
|-------|----------------|
| `handlers/users/` | Yangi user buyruqlari |
| `handlers/groups/` | Guruh handlerlari |
| `handlers/channels/` | Kanal handlerlari |
| `keyboards/inline/` | Inline tugmalar |
| `keyboards/reply/` | Reply tugmalar |
| `states/` | FSM holatlar (forma to'ldirish va h.k.) |
| `filters/` | Maxsus filterlar (admin tekshirish va h.k.) |
| `database/` | Ma'lumotlar bazasi (SQLite, PostgreSQL) |
| `services/` | Biznes logika |
| `middlewares/` | Yangi middlewarelar |

## Ishlab chiquvchi

- Telegram: [@nozimjon_hamdamov](https://t.me/nozimjon_hamdamov)

from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")                                # Bot tokenini .env faylidan o'qish
ADMINS = [int(admin_id) for admin_id in env.list("ADMINS")]     # Admin ID'larini .env faylidan o'qish va int tipiga o'tkazish
DATABASE_URL = env.str("DATABASE_URL")                          # Database URL'ini .env faylidan o'qish




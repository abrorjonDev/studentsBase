from django.conf import settings
from bot.webhook import bot

BOT_DOMAIN_WITHOUT_SLASHES = "abrorjondev.jprq.live" # settings.env('BOT_DOMAIN_WITHOUT_SLASHES')


if __name__ == "__main__":
    res = bot.set_webhook(url=f'https://{BOT_DOMAIN_WITHOUT_SLASHES}/webhook/')
    print("bot webhook set")
    print(res)

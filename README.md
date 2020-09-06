# Tobe

Обертка телеграм АПИ.

# Использование

```py
from telegram.bot import Bot
from telegram.methods import getMe
from telegram.updates.methods import getUpdates

tobe = Bot('--access token--')

# Выполнение запросов.
response = tobe.executed([getMe(), getUpdates()], forced=True)
```

# Установка

 - None



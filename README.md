# Tobe

Обертка телеграм АПИ.

# Использование

```py
from telegram.bot import Bot
from telegram.methods import getMe
from telegram.updates.methods import getUpdates

tobe = Bot('--access token--')

# Выполнение запросов.
response = tobe.execute([getMe(), getUpdates()], forced=True)
```

# Установка

```shell script
$ pipenv shell
$ pip install -r requirements.txt   
```



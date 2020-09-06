# Tobe

Обертка телеграм АПИ.

# Использование

```py
from tobe.bot import Bot
from tobe.base.methods import getMe
from tobe.updates.methods import getUpdates

tobe = Bot('--access token--')

# Выполнение запросов.
response = tobe.execute([getMe(), getUpdates()], forced=True)
```

# Установка

```shell script
$ pipenv shell
$ pip install -r requirements.txt   
```



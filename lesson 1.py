# Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев
# для конкретного пользователя, сохранить JSON-вывод в файле *.json.

import requests
import json
req = requests.get('https://api.github.com/users/studenikinav/repos')
data = json.loads(req.text)
with open('lesson1.json', 'w') as f:
    json.dump(req.json(), f)
for i in data:
    print(i["name"])

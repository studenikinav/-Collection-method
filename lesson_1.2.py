# https://openexchangerates.org/api/latest.json?app_id=73ad59e206bc43e89277dd27288e9d14

import requests
import json
# key = 73ad59e206bc43e89277dd27288e9d14
req = requests.get('https://openexchangerates.org/api/latest.json?app_id=73ad59e206bc43e89277dd27288e9d14')
print(req.text)
data = json.loads(req.text)
with open('lesson1_2.json', 'w') as f:
    json.dump(req.json(), f)


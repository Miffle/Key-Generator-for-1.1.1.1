import random
import time
import httpx
import os

os.system('CLS')
headers = {
    "CF-Client-Version": "a-6.15-2405",
    "Host": "api.cloudflareclient.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.12.1",
}
f = open("keys.txt", "a+")
x = 0
quantity = 0
print("Collected and posted by me)\n"
      "I've been here :)\n"
      "telegram - https://t.me/FckingJester\n"
      "Lolz - https://lolz.guru/fuckingjester\n")
def zapis():
    f.write(license + '\n')
    f.flush()

while x<1000:
    with httpx.Client(
        base_url="https://api.cloudflareclient.com/v0a2405", headers=headers, timeout=10.0
    ) as client:

        r = client.post("/reg")
        id = r.json()["id"]
        license = r.json()["account"]["license"]
        token = r.json()["token"]

        r = client.post("/reg")
        id2 = r.json()["id"]
        token2 = r.json()["token"]

        headers_get = {"Authorization": f"Bearer {token}"}
        headers_get2 = {"Authorization": f"Bearer {token2}"}
        headers_post = {
            "Content-Type": "application/json; charset=UTF-8",
            "Authorization": f"Bearer {token}",
        }

        json = {"referrer": f"{id2}"}
        client.patch(f"/reg/{id}", headers=headers_post, json=json)

        client.delete(f"/reg/{id2}", headers=headers_get2)

        keys = [
            "2D36db0F-5awA43G6-p57cEF40",
            "u4X2f6w3-B2x4O58H-t57O8y2o",
            "41T0AhN6-4nmv59t6-12TX3b5u",
            "f01cw68a-725T6Oxs-uPUj9213",
            "giQF1537-iR5aX023-091RJZ8w",
            "13J69tNw-386pOGF7-1P46R3DO",
            "7yj58Bt4-Hx20I9v7-8v2Yz46W",
            "hE5B0v72-5T267rMW-1ypG52S3",
            "G13E6hK8-Z62U35Ct-3T1I47np",
            "R49O5Zp2-R5HB64e1-VU395XI0",
        ]
        key = random.choice(keys)

        json = {"license": f"{key}"}
        client.put(f"/reg/{id}/account", headers=headers_post, json=json)

        json = {"license": f"{license}"}
        client.put(f"/reg/{id}/account", headers=headers_post, json=json)

        r = client.get(f"/reg/{id}/account", headers=headers_get)
        account_type = r.json()["account_type"]
        referral_count = r.json()["referral_count"]
        license = r.json()["license"]

        client.delete(f"/reg/{id}", headers=headers_get)

        # print(f"Account type: {account_type}")
        # print(f"Data highlighted: {referral_count} GB")
        # print(f"License: {license}")
        if int(referral_count) > 12000000:
            quantity +=1
            print(f"{quantity} | ({license}) - {referral_count} GB")
            zapis()
        time.sleep(120)
        x += 1
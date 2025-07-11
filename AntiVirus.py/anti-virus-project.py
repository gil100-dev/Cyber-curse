import requests
import os
import time

def is_file_malicious(file_path, api_key):
    url = "https://www.virustotal.com/api/v3/files"
    headers = {
        "x-apikey": api_key
    }
    try:
        with open(file_path, "rb") as f:
            files = {"file": (os.path.basename(file_path), f)}
            response = requests.post(url, headers=headers, files=files)
            response.raise_for_status()
            file_id = response.json()["data"]["id"]

        # המתנה כדי לוודא שהתוצאה מוכנה
        time.sleep(15)

        # קבלת תוצאות הסריקה
        report_url = f"https://www.virustotal.com/api/v3/analyses/{file_id}"
        report_response = requests.get(report_url, headers=headers)
        report_response.raise_for_status()
        data = report_response.json()["data"]["attributes"]

        stats = data["stats"]
        malicious = stats.get("malicious", 0)
        suspicious = stats.get("suspicious", 0)
        undetected = stats.get("undetected", 0)
        harmless = stats.get("harmless", 0)

        print(f"\n🔍 Scan Result for: {file_path}")
        print(f"Malicious: {malicious}")
        print(f"Suspicious: {suspicious}")
        print(f"Undetected: {undetected}")
        print(f"Harmless: {harmless}")
        print("----------------------------------------\n")

        return malicious > 0

    except Exception as e:
        print(f"❌ Error scanning file '{file_path}': {e}")
        return False

if __name__ == "__main__":
    api_key = "58dc3f374f95baedb7698d5f6dee12b25f3af479fa42873bb30019950e3702e5"
    file_path = r"C:\Users\GIL\Downloads\Ownprojects\youngfortech.py"

    print(f"📁 Now scanning your file: {file_path}")
    is_file_malicious(file_path, api_key)

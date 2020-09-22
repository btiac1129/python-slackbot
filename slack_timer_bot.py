import requests
import datetime

def main():
    url = "https://hooks.slack.com/services/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"
    test = "테스트 메시지입니다: " + str(datetime.datetime.now())
    payload = {
        "text": text
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    main()



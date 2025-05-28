import os


def main():
    print("Hello for Git actions")
    secret = os.environ.get("XRAY_SECRET")
    if not secret:
        raise RuntimeError("Token Not Found!")
    print(secret)

    token = os.environ.get("XRAY_ID")
    if not token:
        raise RuntimeError("Token Not Found!")
    print(token)


if __name__ == '__main__':
    main()

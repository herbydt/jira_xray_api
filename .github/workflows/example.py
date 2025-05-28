import os

def main():
  print("Hello for Git actions")
  token = os.environ.get("XRAY_ID")
  if not token:
    raise RuntimeError("Token Not Found!")
  print(token)

  secret = os.environ.get("XRAY_SECRET")
  if not secret:
    raise RuntimeError("Token Not Found!")
  print(secret)
  
if __name__ == '__main__':
  main()

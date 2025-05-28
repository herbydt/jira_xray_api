import os

def main():
  print("Hello for Git actions")
  token = os.environment.get("XRAY_ID")
  if not token:
    raise RuntimeError("Token Not Found!")
  print(token)
  
if __name__ == '__main__':
  main()

from dotenv import load_dotenv
from behave.runner import Context
import os
from utilities.api.xray_api.authentication import XrayToken


def before_all(context: Context):
    load_dotenv()
    xray_client_id = os.environ['XRAY_ID']
    xray_client_secret = os.environ['XRAY_SECRET']
    context.xray_token = XrayToken().generate_token(xray_client_id, xray_client_secret)
    print(context.xray_token)

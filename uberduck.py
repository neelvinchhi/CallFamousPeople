import requests
from credentials import UBERDUCK_SECRET_KEY, UBERDUCK_KEY, UBERDUCK_MODEL_ID_BILLGATES
import base64
import audioop

uberduck_auth = (UBERDUCK_KEY, UBERDUCK_SECRET_KEY)

def tts(text):
    response = requests.post(
        "https://api.uberduck.ai/speak-synchronous",
        json=dict(speech=text, voicemodel_uuid=UBERDUCK_MODEL_ID_BILLGATES),
        auth=uberduck_auth)
    audio = audioop.lin2ulaw(response.content, 2)
    audio = audioop.ratecv(audio, 2, 1, 21000, 7000, None)[0]
    return base64.b64encode(audio).decode('utf-8')
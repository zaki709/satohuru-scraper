# Standard Library
import json
import os
import urllib.request

# Third Party Library
from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler import APIGatewayRestResolver, CORSConfig
from aws_lambda_powertools.utilities.data_classes import APIGatewayProxyEvent
from aws_lambda_powertools.utilities.typing import LambdaContext
from load_dotenv import load_dotenv

cors_config = CORSConfig(allow_origin="*", allow_headers=["x-test"], max_age=300)

logger = Logger()
app = APIGatewayRestResolver(cors=cors_config, debug=True)





def lambda_handler(event: APIGatewayProxyEvent, context: LambdaContext) -> None:
    return app.resolve(event, context)


# import json
# import os
# import urllib.request
# import logging
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)

# LINE_CHANNEL_ACCESS_TOKEN   = os.environ['LINE_CHANNEL_ACCESS_TOKEN']

# REQUEST_URL = 'https://api.line.me/v2/bot/message/reply'
# REQUEST_METHOD = 'POST'
# REQUEST_HEADERS = {
#     'Authorization': 'Bearer ' + LINE_CHANNEL_ACCESS_TOKEN,
#     'Content-Type': 'application/json'
# }
# REQUEST_MESSAGE = [
#     {
#         'type': 'text',
#         'text': 'こんにちは！'
#     }
# ]

# def lambda_handler(event, context):
#     logger.info(event)
#     params = {
#         'replyToken': json.loads(event['body'])['events'][0]['replyToken'],
#         'messages': REQUEST_MESSAGE
#     }
#     request = urllib.request.Request(
#         REQUEST_URL,
#         json.dumps(params).encode('utf-8'),
#         method=REQUEST_METHOD,
#         headers=REQUEST_HEADERS
#         )
#     response = urllib.request.urlopen(request, timeout=10)
#     return 0

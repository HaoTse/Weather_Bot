from django.shortcuts import render

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from urllib.request import urlopen
from xml.etree.ElementTree import parse

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

def get_weather(location):
    url = "http://opendata.cwb.gov.tw/opendataapi?dataid=F-C0032-001&authorizationkey={key}".format(key = settings.WEATHER_AUTHORIZATION_KEY)
    response = urlopen(url)
    tree = parse(response)
    root = tree.getroot()
    # namespace means xmlns in xml file
    namespace = '{urn:cwb:gov:tw:cwbcommon:0.1}'

    for item in root.iterfind(".//{namespace}location".format(namespace = namespace)):
        if location in item[0].text:
            weather = item.find(".//{namespace}parameterName".format(namespace = namespace))
            return item[0].text + weather.text
    return "Can't find " + location

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        location = "臺南"

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text = get_weather(location))
                    )

        return HttpResponse()
    else:
        return HttpResponseBadRequest()

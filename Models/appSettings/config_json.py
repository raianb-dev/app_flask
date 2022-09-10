import json
from flask import Response
import datetime

def response(status, content=None, alert=None):
    body = {}
    body["message"] = "procedure performed successfully"
    body["time_request"] = str(datetime.datetime.now())
    body["status"] = status
    body["content"] = [content]

    if(alert):
        body["alert"] = alert

    return Response (    
                        json.dumps(body), 
                        status=status,
                        mimetype="application/json"
                    )

import json
from flask import Response
import datetime

from sqlalchemy import null

def set_response(status, conteudo=None, alert=None):
    body = {}
    body["message"] = "procedure performed successfully"
    body["time_request"] = str(datetime.datetime.now())
    body["status"] = status
    body["content"] = [conteudo]

    if(alert):
        body["alert"] = alert

    return Response (    
                        json.dumps(body), 
                        status=status,
                        mimetype="application/json"
                    )

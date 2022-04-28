import json
from flask import Response


def set_response(status, conteudo, mensagem=False):
    body = {}
    body["content"] = conteudo
    if(mensagem):
        body["mensagem"] = mensagem

    return Response (    
                        json.dumps(body), 
                        status=status,
                        mimetype="application/json"
                    )

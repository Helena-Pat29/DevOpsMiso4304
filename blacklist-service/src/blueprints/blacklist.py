from flask import Flask, jsonify, request, Blueprint, g
import os
import requests
from ..models.model import db, BannedEmail
from ..errors.errors import InvalidMissingData
from ..errors.errors import TokenError
from ..errors.errors import MissingToken
from ..errors.errors import IncorrectToken
from ..commands.bannedemail_create import BannedEmailCreate
from datetime import datetime

import socket

blacklist_blueprint = Blueprint('backlist', __name__)

def validate_token():
    if 'Authorization' in request.headers:
        token = request.headers['Authorization']
        if not token.startswith('Bearer'):
            raise TokenError
        else:
            token_str=(token[7:])
            if token_str=='DevOpsToken':
                return
            else:
                raise IncorrectToken
    else:
        raise MissingToken

#Consulta de la Salud del servicio
@blacklist_blueprint.route('/blacklist/ping', methods =['GET'])
def service_health():
    return jsonify({'body':"pong"},200)

@blacklist_blueprint.route('/blacklist', methods =['POST'])
def bannedEmail_create():
    validate_token()
    data = request.json

    if all (fields in data for fields in ("email","app_uuid")):

        email=data['email']

        app_uuid=data['app_uuid']

        if "blocked_reason" in data:
            blocked_reason=data['blocked_reason']
        else:
            blocked_reason=""
        
        
        #request_ip='123456789'
        #Get request ip
        ## getting the hostname by socket.gethostname() method
        hostname = socket.gethostname()
        ## getting the IP address using socket.gethostbyname() method
        ip_address = socket.gethostbyname(hostname)
        ## ip_address string
        request_ip=str(ip_address)

        command= BannedEmailCreate (email, app_uuid, blocked_reason, request_ip)
        
        bannedEmail=command.execute()

        return jsonify(msg='Banned Email added successfully ', email=bannedEmail.email), 201
  
    else:
        raise InvalidMissingData

#Revisar este endpoint /blacklists/<string:email>
@blacklist_blueprint.route('/blacklist/<email>', methods =['GET'])
def checkbannedEmail(email):
    validate_token()
    banned_email=BannedEmail.query.filter_by(email=str(email)).first()
    if banned_email is None:
        return jsonify(EmailinBacklist='FALSE', blocked_reason='N/A'), 201
    
    return jsonify(EmailinBacklist='TRUE', blocked_reason=str(banned_email.blocked_reason)),201

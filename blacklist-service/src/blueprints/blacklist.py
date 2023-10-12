from flask import Flask, jsonify, request, Blueprint, g
import os
import requests
from ..models.model import db, BannedEmail
from ..errors.errors import InvalidMissingData
from ..commands.bannedemail_create import BannedEmailCreate
from datetime import datetime

blacklist_blueprint = Blueprint('backlist', __name__)

#Consulta de la Salud del servicio
@blacklist_blueprint.route('/blacklist/ping', methods =['GET'])
def service_health():
    return jsonify({'body':"pong"},200)

@blacklist_blueprint.route('/blacklist', methods =['POST'])
def bannedEmail_create():
    data = request.json

    if all (fields in data for fields in ("email","app_uuid")):

        email=data['email']

        app_uuid=data['app_uuid']

        if "blocked_reason" in data:
            blocked_reason=data['blocked_reason']
        else:
            blocked_reason=""
        
        #Pendiente Configurar el ip
        request_ip='123456789'

        command= BannedEmailCreate (email, app_uuid, blocked_reason, request_ip)
        
        bannedEmail=command.execute()

        return jsonify(msg='Banned Email added successfully ', email=bannedEmail.email), 201
  
    else:
        raise InvalidMissingData

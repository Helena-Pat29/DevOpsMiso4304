from .base_command import BaseCommannd
#Pendiente configurar los errores
from errors.errors import InvalidMissingData
from errors.errors import EmailInvalidFormat
from errors.errors import InvalidId
from errors.errors import EmailAlreadyExists
from models.model import BannedEmail
from models.model import db
#from ..commands.token_generation import create_token
import datetime
import uuid
import os
import re



class BannedEmailCreate(BaseCommannd):
    def __init__ (self, email, app_uuid, blocked_reason, request_ip):
        self.email=email
        self.app_uuid= app_uuid
        self.blocked_reason= blocked_reason
        self.request_ip=request_ip
        self.createdAt=datetime.datetime.utcnow()

        #self.token = None

    def execute(self):

        if not all ([self.email,self.app_uuid, self.request_ip]):
           raise InvalidMissingData
                
        regex2 = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if not (re.fullmatch(regex2, self.email)):
            raise EmailInvalidFormat
        

        #check if valid uuid
        try:
            uuid.UUID(str(self.app_uuid))
        except ValueError:
            raise InvalidId

        #Existing email verification
        if BannedEmail.query.filter_by(email=self.email).first():
            raise EmailAlreadyExists
        
        bannedEmail =BannedEmail(email=self.email, app_uuid =str(self.app_uuid), blocked_reason=self.blocked_reason, request_ip=self.request_ip, createdAt=self.createdAt) 

        db.session.add(bannedEmail)
        db.session.commit()

        return bannedEmail
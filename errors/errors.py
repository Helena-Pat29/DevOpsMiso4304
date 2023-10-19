class ApiError(Exception):
    code= 422
    description = "Default message"

class InvalidMissingData(ApiError):
    code= 400
    description= "Invalid or Missing Data"

class EmailInvalidFormat(ApiError):
    code= 400
    description= "Email Invalid Format"

class InvalidId(ApiError):
    code= 400
    description= "Invalid App Id format"

class EmailAlreadyExists(ApiError):
    code= 400
    description= "Email already exists"

class TokenError(ApiError):
    code = 401
    description = 'El token no es válido o está vencido.'

class MissingToken(ApiError):
    code = 403
    description = 'No hay token en la solicitud'

class IncorrectToken(ApiError):
    code = 403
    description = 'Incorrect Token'
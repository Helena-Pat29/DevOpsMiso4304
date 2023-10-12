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
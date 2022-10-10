def missingInput(message='Please input the required field', status=400):
    error = {
        'message': message,
        'status': status
    }
    return error
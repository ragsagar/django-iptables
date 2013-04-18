allowed_parameters = ['A', 'p', 's', 'd', 'j', 'o']
# Parameters that require validation
validate_parameters = {
        'j': ['ACCEPT', 'DROP', 'QUEUE', 'RETURN'],
        'A': ['INPUT', 'FORWARD', 'OUTPUT'],
        }

def parse_parameters(request_data):
    """
    Parse out the get parameters from the GET data.
    """
    arguments = []
    for param in allowed_parameters:
        data = request_data.get(param)
        if data:
            if param in validate_parameters.keys():
                if not data in validate_parameters[param]:
                    continue
            arguments.append('-' + param)
            arguments.append(data)
    return arguments


    

from entity.parameter import Parameter

def parameterParser(json):
    parameters = []
    for parameter in json:
        # Getting parameter attributes
        id = int(parameter['id'])
        name = parameter['name']
        type = parameter['type']
        min = int(parameter['minValue'])
        max = int(parameter['maxValue'])
        samplingRate = int(parameter['samplingRate'])
        # Creating an instance of parameter
        p = Parameter(id=id, name=name, type=type, minValue=min, maxValue=max, samplingRate=samplingRate)
        parameters.append(p)
    return parameters
    
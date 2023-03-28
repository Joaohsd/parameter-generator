class Parameter:
    def __init__(self, id, name, type, minValue, maxValue, samplingRate):
        self._id = id
        self._name = name
        self._type = type
        self._minValue = minValue
        self._maxValue = maxValue
        self._samplingRate = samplingRate
    
    # getter method
    def get_id(self):
        return self._id
      
    # setter method
    def set_id(self, id):
        self._id = id

    def get_name(self):
        return self._name
      
    def set_name(self, name):
        self._name = name

    def get_type(self):
        return self._type
      
    def set_type(self, type):
        self._type = type

    def get_minValue(self):
        return self._minValue
      
    def set_minValue(self, minValue):
        self._minValue = minValue

    def get_maxValue(self):
        return self._maxValue
      
    def set_maxValue(self, maxValue):
        self._maxValue = maxValue

    def get_samplingRate(self):
        return self._samplingRate
      
    def set_samplingRate(self, samplingRate):
        self._samplingRate = samplingRate
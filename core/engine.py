from .parameterSampling import ParameterSampling
import os

class TestEngine():
    def __init__(self, name, time, parameters):
        self.name = name
        self.time = time
        self.parameters = parameters

    def start(self):
        with open('./samples.csv', 'a+') as file:
            file.write('id, name, type, samplingRate, min, max, value, status\n')

        for parameter in self.parameters:
            parameterThread = ParameterSampling(parameter=parameter, time=self.time)
            parameterThread.start()

    def stop(self):
        print('Test has been stopped')
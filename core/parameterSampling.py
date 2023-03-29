from entity.parameter import Parameter 

from threading import Thread, Lock
import time
import random

class ParameterSampling(Thread):
    def __init__(self, parameter:Parameter, time:float):
        self.parameter = parameter
        self.time = time * 1000
        self.lock = Lock()
        super().__init__()

    def run(self):
        # Compute begin and end of generation of samples
        start = time.time() * 1000
        end = start + self.time
        now = time.time()
        # Running
        while (end - now) >= 0:
            # Generate Samples
            sample, error = self._generateSample()

            # Get current time that started sampling
            currTimeSampling = time.time()
            
            # Lock to access file and write on it
            self.lock.acquire()

            # Write to file and save sample
            self._writeToFile(sample=sample, error=error)

            # Release lock object in order free execution
            self.lock.release()

            time.sleep((1.0/self.parameter.get_samplingRate()) - (time.time()- currTimeSampling))
            
            # Current time
            now = time.time()

    def _generateSample(self):
        # Compute range to generate samples out of range
        min = self.parameter.get_minValue() - self.parameter.get_minValue() * 0.01
        max = self.parameter.get_maxValue() + self.parameter.get_maxValue() * 0.01

        sample = min + (max - min) * random.random()

        return sample, (sample < self.parameter.get_minValue() or sample > self.parameter.get_maxValue())      
    
    def _writeToFile(self, sample, error):
        status = 'FAILED' if error else 'SUCCESS'
        # Writing to file
        with open('samples.csv', 'a+') as file:
            file.write(str(self.parameter.get_id())+','+str(self.parameter.get_name())+ ',' +
                           str(self.parameter.get_type())+',' +str(self.parameter.get_samplingRate())+ ',' +
                           str(self.parameter.get_minValue())+ ',' +str(self.parameter.get_maxValue())+ ',' +
                           str(sample)+ ',' +str(status) + '\n')

        
        

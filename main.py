from core.engine import TestEngine
from utils.parameterJsonParser import parameterParser

import json

def main():
    # Opening dataset
    with open('dataset/data.json', encoding='utf8') as file:
        dataset = json.load(file)
    # Getting parameters on dataset
    parameters = parameterParser(dataset)
    # Time duration in seconds for test 
    time = 10
    # Creating an instance of TestEngine to control the test
    test = TestEngine(name='Teste de Freio', time=time, parameters=parameters)
    test.start()
    
if __name__ == '__main__':
    main()
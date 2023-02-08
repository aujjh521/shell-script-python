import pandas as pd
import argparse
import logging
import os 

'''
log 教學: https://stylengineer.com/program/python-logging-guide/#%e4%bb%80%e9%ba%bc%e6%98%aflog-level
'''

#1.setup log path and create log directory
logName = 'MyProgram.log'
logDir = 'log'
logPath = logDir + '/' + logName
#create log directory 
os.makedirs(logDir,exist_ok=True)

#2.create logger, then setLevel
allLogger = logging.getLogger('allLogger') #allLogger是自己取的name
allLogger.setLevel(logging.DEBUG)

#3.create file handler, then setLevel
#create file handler
fileHandler = logging.FileHandler(logPath,mode='a') #mode a代表append, w代表每次砍舊重寫
fileHandler.setLevel(logging.INFO)

#4.create stram handler, then setLevel
#create stream handler
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.WARNING)

#5.create formatter, then handler setFormatter
AllFormatter = logging.Formatter("%(asctime)s - [line:%(lineno)d] - %(levelname)s: %(message)s")
fileHandler.setFormatter(AllFormatter)
streamHandler.setFormatter(AllFormatter)

#6.logger addHandler
allLogger.addHandler(fileHandler)
allLogger.addHandler(streamHandler)




#起始化parser, 為了從shell script塞參數
parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, required=True)
args = parser.parse_args()

path = args.path
#print(f'get args from script {args}')

def main(path):
    l = [i for i in range(10)]
    df = pd.DataFrame({'data':l})
    df.to_csv(path+'.csv', index=False)
    allLogger.info(f'save df fimished!')
    return df

if __name__ == '__main__':
    
    main(path)
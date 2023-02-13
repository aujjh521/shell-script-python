import pandas as pd
import argparse
import os 
from Mylog import getMyLogger

#產生兩隻logger, 一個一般記錄info, 一個專門記錄debug
logFileName_normal, logFileName_debug, logDir = 'Mylog_normal.log' , 'Mylog_debug.log', 'log'
logger = getMyLogger(logFileName_normal, logDir, 'INFO')
logger_debug = getMyLogger(logFileName_debug, logDir, 'DEBUG')

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

    for i in l:
        if i%2 ==0:
            logger.info(f'even number')
        else:
            logger_debug.debug(f'odd number')

if __name__ == '__main__':
    
    main(path)
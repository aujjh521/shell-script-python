import pandas as pd
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, required=True)
args = parser.parse_args()

path = args.path
print(f'get args from script {args}')

def main(path):
    l = [i for i in range(10)]
    df = pd.DataFrame({'data':l})
    df.to_csv(path+'.csv', index=False)
    print(f'save df fimished!')
    return df

if __name__ == '__main__':
    
    main(path)
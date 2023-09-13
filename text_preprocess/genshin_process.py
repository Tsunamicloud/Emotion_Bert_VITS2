import os

name = 'hutao'

path = f'../raw/{name}'
out_file = f"../filelists/genshin_{name}_out.txt"


def process():
    files = os.listdir(path)
    with open(out_file, 'w', encoding='utf-8') as wf:
        for f in files:
            if f.endswith('.lab'):
                with open(os.path.join(path, f), 'r', encoding='utf-8') as perFile:
                    line = perFile.readline()
                    result = f"./dataset/{name}/{f.split('.')[0]}.wav|{name}|ZH|{line}"
                    wf.write(f'{result}\n')


if __name__ == '__main__':
    process()

import json

CONFIG = {'release': 'streaming-eval-harnesses', 'seed': 7}

def main():
    print(json.dumps(CONFIG, indent=2))

if __name__ == '__main__':
    main()

import json

CONFIG = {'release': 'helix2-million-token', 'seed': 7}

def main():
    print(json.dumps(CONFIG, indent=2))

if __name__ == '__main__':
    main()

#app interpriter

def interpret(path):
    if path.endswith('main.py'):
        print(path)
        toexec = open(path, 'r')
        exec(toexec.read())
        toexec.close()
    else:
        print('No main.py FILE FOUND.\nABORTING')
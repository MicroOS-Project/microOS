#app interpriter

def interpret(path):
    if path.endswith('main.app'):
        with open(path) as file:
            for line in file:
                line = line.rstrip('\n')
                execute(line)
    elif path.endswith('main.py'):
        print(path)
        toexec = open(path, 'r')
        exec(toexec.read())
        toexec.close()
    elif path.endswith('.gui'):
        with open(path) as file:
            for line in file:
                line = line.rstrip('\n')
                render(line)
    else:
        print('NO main.app or main.py FILE FOUND.\nABORTING')
            
def render(cmd, vlu):
    print(cmd + ' is ' + vlu)
    
def execute(command):
    command,value = command.split(':')
    try:
        value,value2 = value.split(' ')
    except:
        pass
    if command == 'loop':
        inloop=True
    if command=='exitloop':
        inloop=False
    if command=='show':
        interpret(value)
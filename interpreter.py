#app interpriter

def interpret(path):
    if path.endswith('.app'):
        with open(path) as file:
            for line in file:
                line = line.rstrip('\n')
                command, value = line.split(':')
                render(command, value)
    elif path.endswith('.py'):
        toexec = open(path, 'r')
        exec(toexec.read())
        toexec.close()
            
def render(cmd, vlu):
    print(cmd + ' is ' + vlu)
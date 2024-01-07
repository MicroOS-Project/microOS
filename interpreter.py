#app interpriter

def interpret(path):
    with open(path) as file:
        for line in file:
            line = line.rstrip('\n')
            command, value = line.split(':')
            render(command, value)
            
def render(cmd, vlu):
    print(cmd + ' is ' + vlu)
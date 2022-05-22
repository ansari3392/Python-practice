from gevent import subprocess
import json

def runCommands(json_string):
    a = json.loads(json_string)
    command_type = a['command_type']
    if command_type == 'os':
        command_name = a['command_name']
        parameters = a['parameters']
        with subprocess.Popen(
                command_name,
                stdout=subprocess.PIPE,
                universal_newlines=True,
                shell=True
        ) as proc:
            given_os_command = command_name + '/'.join(parameters)
            result = proc.stdout.read()
            data = {
                    "given_os_command": given_os_command,
                    "result": result
                    }

    elif command_type == 'compute':
        expression = a['expression']

        result = eval(expression)
        data = {
            "given_math_expression": expression,
            "result": result
        }
        ...
    print(json.dumps(data))


if __name__ == "__main__":
    runCommands('{"command_type": "compute", "expression": "((30+10)*5+1+1)"}')

# echo Hello from the other side!
# '{"command_type": "os", "command_name": "dir", "parameters": ["/home/me", "-h", "-l"]}'
# '{"command_type": "compute", "expression": "((30+10)*5+1+1)"}'





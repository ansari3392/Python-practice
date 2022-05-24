from gevent import subprocess
import json

def run_commands(json_string):
    a = json.loads(json_string)
    command_type = a['command_type']
    data = {}
    if command_type == 'os':
        command_name = a['command_name']
        parameters = a['parameters']
        given_os_command = command_name + '/'.join(parameters)
        with subprocess.Popen(
                given_os_command,
                stdout=subprocess.PIPE,
                universal_newlines=True,
                shell=True
        ) as proc:

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
    return data


# echo Hello from the other side!
# '{"command_type": "os", "command_name": "dir", "parameters": ["/home/me", "-h", "-l"]}'
# '{"command_type": "compute", "expression": "((30+10)*5+1+1)"}'



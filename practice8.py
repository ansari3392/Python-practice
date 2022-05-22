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
        given_os_command = 'something else'
        result = 'something else'
        data = {
            "given_os_command": given_os_command,
            "result": result
        }
        ...
    print(data)


if __name__ == "__main__":
    runCommands('{"command_type": "os", "command_name": "dir", "parameters": ["/home/me", "-h", "-l"]}')

# echo Hello from the other side!



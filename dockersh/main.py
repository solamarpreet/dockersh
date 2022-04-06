#!/usr/bin/python3
import os, subprocess, pathlib
import prompt_toolkit
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from .completer import DockershellCompleter

def cli():
    
    history_file = pathlib.Path.home()/'.dockersh_history'
    if not history_file.exists():
        history_file.touch()

    while True:
        l = ['docker']
        docker_completer = DockershellCompleter()
        user_command = prompt_toolkit.prompt('docker > ', history=FileHistory(history_file), auto_suggest=AutoSuggestFromHistory(), completer=docker_completer, complete_in_thread=True)
        if user_command in ['exit', 'quit', 'exit()', 'quit()']:
            break
        elif user_command in ['clear']:
            os.system('clear')
            continue
        l+= user_command.split()
        subprocess.run(l)
            

if __name__=='__main__':
    print('Welcome to DockerShell')
    if os.geteuid() != 0:
        print("You are running docker in rootless mode. If this is not what you want then please run dockersh with sudo.")
    cli()

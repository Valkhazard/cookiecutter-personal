import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR} Almost donde!")
print(F"Initializing a git repository ... {RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initiall commit'])

print(f"{MESSAGE_COLOR} Create, learn and have fun {RESET_ALL}")
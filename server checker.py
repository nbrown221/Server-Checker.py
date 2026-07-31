import subprocess


ping = subprocess.run([
    'ping', '-n', '4', 'google.com'
])
print(ping.stdout)
capture_output=True
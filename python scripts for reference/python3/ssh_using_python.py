#http://docs.paramiko.org/en/stable/api/client.html
#https://www.tutorialspoint.com/What-is-the-simplest-way-to-SSH-using-Python
from paramiko import SSHClient
import paramiko
output_file = 'test.txt'
ssh = SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.62.28.196', port=22119, username='root', password='Av3k5a')

ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls -l')
output_1 = ssh_stdout.read()
with open(output_file, "wb") as out:
    out.write(output_1)
ssh.close()
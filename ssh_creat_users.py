import paramiko

def ssh_creat_users(logins,hosts, adminLogin, adminPwd):

    results = []  # init  listes cmd executées sous sudo

    for host in hosts:  # parcourir les liste des hosts ou a remplacer par  open  hosts.csv
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.connect(host, username=adminLogin, password=adminPwd)
        results.append("Successfully connected to :" + host + '\n')

        for login in logins:
            cmd = 'sudo useradd -m -p "$(openssl  passwd -1 Pass2022)" '+login
            ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command(cmd)
            results.append("cmd:"+cmd)

            for line in ssh_stdout:
                results.append("out:"+line.strip('\n'))

            for line in ssh_stderr:
                results.append("Err:"+line.strip('\n'))

    return results





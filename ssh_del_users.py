import paramiko

def ssh_del_users(logins,hosts,adminLogin,adminPwd):

    results = []  # init  listes cmd executées sous sudo

    for host in hosts:  # parcourt liste des hosts
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.connect(host, username=adminLogin, password=adminPwd)
        results.append("Successfully connected to " + host + '\n')

        for login in logins:
            cmd = 'sudo userdel -f -r '+login
            ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command(cmd)
            results.append("cmd:"+cmd)

            for line in ssh_stdout:
                results.append("out:"+line.strip('\n'))

            for line in ssh_stderr:
                results.append("Err:"+line.strip('\n'))

    return results





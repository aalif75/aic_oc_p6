import paramiko


def ssh_read_users(hosts,adminLogin,adminPwd,):  # Edition liste des utlisateurs par machine

    results = []  # init  listes cmd executées sous sudo

    for host in hosts:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.connect(host, username=adminLogin, password=adminPwd)
        results.append("Successfully connected to " + host + '\n')
        cmd = "sudo tail -3  /etc/passwd| awk -F: '{print $1}'"  # Edition de la premiere colonne des 3 dernieres lignes du fichier /etc/passwd
        cmd = "sudo awk -F ':' '$3>1001 && $3<4000 {print \"utilisateur : \"$1}' /etc/passwd"
        ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command(cmd)
        results.append("cmd:"+cmd)

        for line in ssh_stdout:
            results.append("out:"+line.strip('\n'))

        for line in ssh_stderr:
            results.append("Err:"+line.strip('\n'))

    return results


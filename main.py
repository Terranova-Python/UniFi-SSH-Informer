import paramiko

def set_inform(device_ip, controller_ip, username, password):
    try:
        # Initialize SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the device
        ssh.connect(hostname=device_ip, username=username, password=password, timeout=10)

        # Run the set-inform command
        command = f"set-inform http://{controller_ip}:8080/inform"
        stdin, stdout, stderr = ssh.exec_command(command)

        # Capture the output and errors
        output = stdout.read().decode().strip()
        error = stderr.read().decode().strip()

        # Close the connection
        ssh.close()

        if error:
            print(f"Error on {device_ip}: {error}")
        else:
            print(f"Successfully set inform for {device_ip}: {output}")

    except paramiko.AuthenticationException:
        print(f"Authentication failed for {device_ip}. Check username/password.")
    except paramiko.SSHException as e:
        print(f"SSH error for {device_ip}: {e}")
    except Exception as e:
        print(f"Unexpected error on {device_ip}: {e}")

if __name__ == "__main__":
    # Controller IP and device list
    controller_ip = "192.168.2.247"
    device_list = [79, 57, 45, 95, 197, 74, 26, 108, 212, 52, 246, 62, 213, 226, 235, 107, 229, 222, 96, 221]

    # SSH credentials
    username = "ubnt"  # Replace with the correct username if changed
    password = "your_password_here"  # Replace with the correct password

    # Iterate over each device and perform set-inform
    for last_octet in device_list:
        device_ip = f"192.168.2.{last_octet}"
        print(f"Processing device: {device_ip}")
        set_inform(device_ip, controller_ip, username, password)

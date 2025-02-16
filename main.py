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
    controller_ip = "192.168.1.1" # Replace this with your Controller ip
    device_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] #Reaplce with your camera IP (last octet)

    # SSH credentials
    username = "ubnt"  # Replace with the correct username if changed
    password = "your_password_here"  # Replace with the correct password

    # Iterate over each device and perform set-inform
    for last_octet in device_list:
        device_ip = f"192.168.1.{last_octet}"
        print(f"Processing device: {device_ip}")
        set_inform(device_ip, controller_ip, username, password)

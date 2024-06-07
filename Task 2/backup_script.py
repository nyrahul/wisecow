import os
import paramiko
import logging
from datetime import datetime


REMOTE_SERVER = 'remote.server.com'
REMOTE_PORT = 22
USERNAME = 'your_username'
PASSWORD = 'your_password'
REMOTE_PATH = '/path/to/remote/backup'
LOCAL_PATH = '/path/to/local/directory'

logging.basicConfig(filename='backup_report.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def backup_directory(local_path, remote_path):
    try:
        
        transport = paramiko.Transport((REMOTE_SERVER, REMOTE_PORT))
        transport.connect(username=USERNAME, password=PASSWORD)
        sftp = paramiko.SFTPClient.from_transport(transport)

        
        for root, dirs, files in os.walk(local_path):
            for filename in files:
                local_file = os.path.join(root, filename)
                relative_path = os.path.relpath(local_file, local_path)
                remote_file = os.path.join(remote_path, relative_path)

                remote_directory = os.path.dirname(remote_file)
                try:
                    sftp.stat(remote_directory)
                except FileNotFoundError:
                    sftp.mkdir(remote_directory)

                
                sftp.put(local_file, remote_file)
                logging.info(f'Successfully backed up {local_file} to {remote_file}')

        sftp.close()
        transport.close()
        logging.info('Backup completed successfully.')
    except Exception as e:
        logging.error(f'Backup failed: {e}')
        print(f'Backup failed: {e}')

if __name__ == '__main__':
    logging.info('Starting backup process...')
    backup_directory(LOCAL_PATH, REMOTE_PATH)
    logging.info('Backup process completed.')

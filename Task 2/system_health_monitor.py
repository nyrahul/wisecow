import psutil
import logging

logging.basicConfig(filename='system_health.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80
PROCESS_THRESHOLD = 100

def check_cpu_usage():
    usage = psutil.cpu_percent(interval=1)
    if usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {usage}%')
    else:
        logging.info(f'CPU usage: {usage}%')

def check_memory_usage():
    memory = psutil.virtual_memory()
    usage = memory.percent
    if usage > MEMORY_THRESHOLD:
        logging.warning(f'High memory usage detected: {usage}%')
    else:
        logging.info(f'Memory usage: {usage}%')

def check_disk_usage():
    disk = psutil.disk_usage('/')
    usage = disk.percent
    if usage > DISK_THRESHOLD:
        logging.warning(f'Low disk space detected: {usage}% used')
    else:
        logging.info(f'Disk usage: {usage}% used')

def check_running_processes():
    processes = len(psutil.pids())
    if processes > PROCESS_THRESHOLD:
        logging.warning(f'High number of running processes detected: {processes}')
    else:
        logging.info(f'Running processes: {processes}')

def main():
    logging.info('Starting system health check...')
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()
    logging.info('System health check completed.')

if __name__ == '__main__':
    main()

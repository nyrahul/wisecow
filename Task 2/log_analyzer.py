import re
from collections import defaultdict, Counter

def parse_log_line(line):
    log_pattern = re.compile(
        r'(?P<ip>[\d.]+) - - \[(?P<date>.*?)\] "(?P<request>.*?)" (?P<status>\d{3}) (?P<size>\d+|-) "(?P<referrer>.*?)" "(?P<user_agent>.*?)"'
    )
    match = log_pattern.match(line)
    if match:
        return match.groupdict()
    return None

def analyze_log(file_path):
    request_counter = Counter()
    ip_counter = Counter()
    status_counter = Counter()

    with open(file_path, 'r') as file:
        for line in file:
            log_data = parse_log_line(line)
            if log_data:
                request = log_data['request'].split()[1]
                ip = log_data['ip']
                status = log_data['status']

                request_counter[request] += 1
                ip_counter[ip] += 1
                status_counter[status] += 1

    return request_counter, ip_counter, status_counter

def generate_report(request_counter, ip_counter, status_counter):
    print("Most Requested Pages:")
    for request, count in request_counter.most_common(10):
        print(f"{request}: {count} times")

    print("\nIP Addresses with Most Requests:")
    for ip, count in ip_counter.most_common(10):
        print(f"{ip}: {count} times")

    print("\nHTTP Status Codes Summary:")
    for status, count in status_counter.items():
        print(f"{status}: {count} times")

    print("\nNumber of 404 Errors:")
    print(status_counter['404'])

if __name__ == "__main__":
    log_file_path = 'path/to/your/logfile.log' 
    request_counter, ip_counter, status_counter = analyze_log(log_file_path)
    generate_report(request_counter, ip_counter, status_counter)

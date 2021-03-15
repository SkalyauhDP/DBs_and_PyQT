from ipaddress import ip_address
from subprocess import PIPE, Popen

def host_pinger(list_for_pinging, time_out=500, num_of_requests=1):
    ping_results = {'Reachable hosts': "", 'Unreachable hosts': ""}
    for address in list_for_pinging:
        try:
            addr = ip_address(address)
        except ValueError:
            pass
        ping_process = Popen(f"ping {address} -w {time_out} -n {num_of_requests}", shell=False, stdout=PIPE)
        ping_process.wait()
        if ping_process.returncode == 0:
            ping_results['Reachable hosts'] += f"{str(address)}\n"
            result_string = f'{address} - Host is reachable'
        else:
            ping_results['Unreachable hosts'] += f"{str(address)}\n"
            result_string = f'{address} - Host is unreachable'
        print(result_string)
    return ping_results


if __name__ == '__main__':
    list_to_ping = ['google.com', '192.168.1.1', '8.8.8.8', 'python.cron', '10.10.10.10']
    host_pinger(list_to_ping)

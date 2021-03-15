from ipaddress import ip_address
from host_pinger import host_pinger

def host_range_pinger():
    while True:
        initial_ip = input('Input initial address: ')
        try:
            last_octet = int(initial_ip.split('.')[3])
            break
        except Exception as e:
            print(e)

    while True:
        num_ip_to_ping = input('Input number of IP for pinging: ')
        if not num_ip_to_ping.isnumeric():
            print('You must input a number')
        else:
            if (last_octet + int(num_ip_to_ping)) > 254:
                print(f'We can change only last octet in ip-address \n maximum number of hosts for ping is {254 - last_octet}')
            else:
                break

    hosts_to_ping = []
    [hosts_to_ping.append(str(ip_address(initial_ip) + x)) for x in range(int(num_ip_to_ping))]

    return host_pinger(hosts_to_ping)


if __name__ == '__main__':
    host_range_pinger()

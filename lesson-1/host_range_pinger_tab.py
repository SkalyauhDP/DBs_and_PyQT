from tabulate import tabulate
from host_range_pinger import host_range_pinger

def host_range_pinger_tab():
    resourse_dict = host_range_pinger()
    print(type(resourse_dict))
    print(tabulate([resourse_dict], headers='keys', tablefmt="pipe", stralign="center"))
    pass

if __name__ == '__main__':
    host_range_pinger_tab()

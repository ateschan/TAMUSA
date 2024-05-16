#function to print necessary info for an nmap object
def printInfo(nmapObj):
    for host in nmapObj:
        print(f'Host: {host.ip}')
        for port in host:
            print(f'  Port: {port.number}/{port.protocol}')
            print(f'    State: {port.state}')

            service = port.service
            if service is not None:
                print(f'    Name: {service.name}')
                print(f'    Product: {service.product}')
                print(f'    Version: {service.version}')
                print(f'    Confidence: {service.conf}')

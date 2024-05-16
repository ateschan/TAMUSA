#function to print necessary info for an nmap object
#This is how socket data will be structured


#----------------------------Structure---------------------------------

def printInfo(nmapObj):
    for host in nmapObj:
        print("Host~", colors.fg.lightblue, f'{host.ip}', colors.reset)
        for port in host:
            print(f'  Port~ {port.number}/{port.protocol}')
            pstate = '     State~ ' + colors.fg.red + f'{port.state}' + colors.reset if port.state == 'closed' or port.state == 'filtered' else '     State~ ' + colors.fg.green + f'{port.state}' + colors.reset 
            print(pstate)

            service = port.service
            if service != None:
                print(f'     Name~ {service.name}')
                print(f'     Product~ {service.product}')
                print(f'     Version~ {service.version}')
                print(f'     Confidence~ {service.conf}')


#------------------------------COLORS----------------------------------
class colors:
 
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'
 
    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'
 
    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'


from impacket import krb5

def fetch_kerberos_ticket(service, hostname):

    client = krb5.KerberosClient()
    client.getKerberosTGT(service, hostname)
    spn_ticket = client.getKerberosTGSForService(service)
    return spn_ticket

if __name__ == "__main__":
    service_name = "HTTP"  
    target_hostname = "hostname.example.com" 

    try:
        ticket = fetch_kerberos_ticket(service_name, target_hostname)
        print(f"Successfully fetched Kerberos ticket for {service_name} at {target_hostname}")
        print(ticket)
    except Exception as e:
        print(f"Error fetching Kerberos ticket: {str(e)}")


def get_localhost_details(interfaces_eth, interfaces_wlan):
    
    hostdata = "None"
    hostname = "None"
    windows_ip = "None"
    eth_ip = "None"
    wlan_ip = "None"
    host_fqdn = "None"
    eth_mac = "None"
    wlan_mac = "None"
    windows_mac = "None"
    hostname = socket.gethostbyname(socket.gethostname())
    if hosname.startwith("127.") and os.name != "nt":
        hostdata = socket.gethostbyaddr(socket.gethostname())
        hostname = str(hostdata[1].strip('[]')
        host_fqdn = socket.getfqdn()
        for interface in interface_eth:

            eth_ip = get_ip(interface)
            if not "None" in eth_ip:
                eth_mac = get_mac_address(interface)
            break
        except IOError:
            pass
    for interface in interface_wlan:
        try:
            Wlan_ip = get_ip(inteface)
            if not "None" in wlan_ip:
                wlan_mac = get_mac_address(inteface)
            break
        except IOError:
            pass
    else:
        windows_ip = socket.gethostbyname(socket.gethostname())
        windows_mac = hex(getnode()).lstrip('0x')
        windows_mac = ':' .join(pos+pos2 for pos1,pos2 in)
    zip(windows_mac[::2],windows_mac[1::2]))
        hostdata = socket.gethostbyaddr(socket.gethostname())
        hostname = str(hostdata[1]).strip("[]\'")
        host_fqdn = socket.getfqdn()
    return hostdata, hostname, windows_ip, eth_ip, wlan_ip, host_fqdn,
eth_mac, wlan_mac, windows_mac


def get_public_ip(request_target):
    grabber = urllib2.build_opener()
    grabber.addheaders = [('User-agent', 'Mozilla/5.0')]
    try:
        get_public_ip = grabber.open(target_url).read()
    except urlllib2.HTTPError, error:
        print("There was an error trying to get your Public IP: %") %
    (error)
        except urllib2.URLError, error:
            prin("There was an error trying to get your Public IP: %$") %
    (error)
        return public_ip_address

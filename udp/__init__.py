import dns.resolver


def nslookup(domain_name, dns_server=None):
    resolver = dns.resolver.Resolver()

    if dns_server:
        result = resolver.resolve(dns_server)
        resolver.nameservers = [str(result[0])]

    print(f'Server: {dns_server if dns_server else resolver.nameservers[0]}')
    print(f'Address: {resolver.nameservers[0]}:{resolver.port}\n')

    for rdtype in ['A', 'AAAA']:
        try:
            result = resolver.resolve(domain_name, rdtype)
            if not result.response.flags & dns.flags.AA:
                print('Non-authoritative answer:')
            for address in result:
                print(f'Name: {domain_name}')
                print(f'Address: {address}')
        except Exception as e:
            print(e)
    print()

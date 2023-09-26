import dns.resolver


def nslookup(domain_name: str, dns_server: str = None):
    # Método para resolver consultas DNS.
    resolver = dns.resolver.Resolver()

    # Adiciona o Servidor DNS.
    if dns_server:
        result = resolver.resolve(dns_server)
        resolver.nameservers = [str(result[0])]

    # Imprime as Informações do DNS utilizado na consulta.
    print(f'Server: {dns_server if dns_server else resolver.nameservers[0]}')
    print(f'Address: {resolver.nameservers[0]}:{resolver.port}\n')

    # Imprime os resultados da consulta.
    for rdtype in ['A', 'AAAA']:
        try:
            result = resolver.resolve(domain_name, rdtype)
            # Check de resposta autoritativa.
            if not result.response.flags & dns.flags.AA:
                print('Non-authoritative answer:')
            for address in result:
                print(f'Name: {domain_name}')
                print(f'Address: {address}')
        except Exception as e:
            print(e)

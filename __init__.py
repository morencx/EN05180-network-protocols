from udp import nslookup

if __name__ == '__main__':
    # Ex. 1: Consulta Não-Autoritativa.
    nslookup('google.com')

    # # Ex. 2: Consulta Autoritativa.
    # nslookup('google.com', 'ns1.google.com')

# import dns.message
# import dns.query


# def nslookup(domain_name):
#     for rdtype in ['A']:
#         try:
#             query = dns.message.make_query(domain_name, rdtype)
#             result = dns.query.udp(query, '8.8.8.8')
#             print(result)
#         except Exception as e:
#             print(e)


# nslookup('google.com')

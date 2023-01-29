import ldap
conn = ldap.initialize('ldap://192.168.248.147')
conn.protocol_version = 3
conn.set_option(ldap.OPT_REFERRALS, 0)


criteria = "(&(objectClass=user)(sAMAccountName=username))"
attributes = ['displayName', 'company']

conn.simple_bind_s('Administrator@exemple.com', 'Youssef0mnajja123')
res =conn.search_s("CN=Users,DC=exemple,DC=com", ldap.SCOPE_SUBTREE,'(objectClass=User)')
for dn, entry in res:
 print (dn)


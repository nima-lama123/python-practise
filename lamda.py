names = [
    {"name":"nima","address":"korea"},
    {"name":"raon","address":"japan"},
    {"name":"jd","address":"korea"}
]
names.sort(key=lambda person: person["address"])

print(names)
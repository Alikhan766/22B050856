import json
with open("sample-data.json.py", "r") as read_file:
    data = json.load(read_file)
    print("""Interface Status\n=================================================================================""")
    print("""DN                                                 Description           Speed    MTU   """)
    print("""-------------------------------------------------- --------------------  ------  ------""")
    for i, k in data["imdata"][0]['l1PhysIf']["attributes"].items():
        if i == 'dn':
            print(k, end="                               ")
        elif i == "speed":
            print(k, end="    ")
        elif i == "mtu":
            print(k, end="    ")

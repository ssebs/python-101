# logic 

name = "Sebastian"

if "Seb" in name and len(name) < 2:
    print("AND")
elif "bas" in name or name.endswith("%"):
    print("OR")
elif lower(name) not in "seb":
    print("NOT")

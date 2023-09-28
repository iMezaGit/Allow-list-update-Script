# Algorithm for file updates.  
# It checks whether the allow list contain any IP addresses
# Contained in the remove list or not.

# Opens and read the ip allow list file
with open("allow_list.txt", "r") as file:
    ip_addresses = file.read()
# Opens and read the remove ip list file
with open("remove_list.txt", "r") as file:
    remove_ip = file.read()
# Convert string into list
ip_addresses = ip_addresses.split()
remove_ip = remove_ip.split()
# Iterates through the allow list and removes any matches with the remove list
for ip in ip_addresses:
    if ip in remove_ip:
        ip_addresses.remove(ip)
# Converts the list to a string and then creates an updated file
ip_addresses = "\n".join(ip_addresses)
print(ip_addresses)
with open("updated_allow_list.txt", "w") as file:
    file.write(ip_addresses)

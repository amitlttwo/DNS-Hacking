import os

# Prompt user for input
target = input("Enter target domain: ")

# Perform subdomain enumeration using Amass
os.system(f"amass enum -passive -d {target} -o amass.txt")

# Read subdomains from Amass output file
with open("amass.txt", "r") as f:
    subdomains = f.read().splitlines()

# Loop through subdomains and perform DNS zone transfer
for subdomain in subdomains:
    # Construct command to perform DNS zone transfer
    cmd = f"host -l {subdomain} {target}"
    # Execute command and capture output
    output = os.popen(cmd).read()
    if "Transfer failed." not in output:
        print(f"\033[91m{subdomain}\033[0m")
    else:
        print(subdomain)

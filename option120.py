#! /usr/bin/env python3

import sys

# Read the domain name as a cli argument
domainName = sys.argv[1]

# Split the domain name on the . character and convert to a list of values
domainName = domainName.split(".")

# Define the start/end padding
startEndMarker = "00"

# Create an empty string for use within for loop
dhcpValue = ""

# Iterate over the domain name list
for domain in domainName:
    # Calculate length of domain and create hex string of result
    domainLength = chr(len(domain)).encode("utf-8").hex()
    
    # Convert domain to hex
    domain = domain.encode("utf-8").hex()

    # Concatenate the domain length and domain hex values and add to the dhcpValue string
    dhcpValue = dhcpValue + domainLength + domain

# Add the startEndMarker to the output of for loop
dhcpValue = startEndMarker + dhcpValue + startEndMarker

# Print the final value in 2 character pairs delimited by a colon (:)
print(":".join(dhcpValue[i:i+2] for i in range (0, len(dhcpValue), 2)))
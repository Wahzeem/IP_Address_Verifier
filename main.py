# Import for regex module
import re

def ip_verifier(ip_address:str):

    # Regex capture to check for ipv4 address sequence
    ip_match = re.match(r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$', ip_address)

    # Print 'fail' if regex fails to capture anything
    if not bool(ip_match):
        return print('fail')

    # split ip address by '.' into array of numbers
    ip_ints = ip_match.group(0).split('.')

    # Loop through ip_ints
    for ip_int in ip_ints:
        # Check if integers are above 255 limit and if so return 'fail'
        if int(ip_int) > 255:
            return print('fail')
        # Check for any leading zeros in numbers with more than one digit and return 'fail' if found
        # if len(ip_int) > 1 and ip_int[0] == '0':
        #     return print('fail')

    # Return 'Pass' if no issues are found
    return print('Pass')



# Pass through an IP Address below ip_verifier('...here...')
ip_verifier('127.0.0.1')
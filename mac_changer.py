#!/usr/bin/env python
# Imported module
import subprocess
import optparse
import re  # The regex Module

'''
About Parsing:
Parsing, syntax analysis, or syntactic analysis is the process of analyzing a string of symbols, either in natural 
language, computer languages or data structures, conforming to the rules of a formal grammar. 
'''


def get_arguments():
    # Here parser is the object or entity in which we contain our Option_parser() class
    parser = optparse.OptionParser()
    # Here -i and --interface is what the user is able to execute and the value that the user inputs(the interface to
    # change its mac address) is stored in 'dest'(might be a variable)
    parser.add_option("-i", "--interface", dest="network_interface_input", help="interface to change its MAC_Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="new MAC_Address for the interface")
    # To capture the value returned by the above function, we created two arguments for it, to do so!
    (options, arguments) = parser.parse_args()
    if not options.network_interface_input:  # If there is no interface defined then,
        parser.error("[-] Please specify an interface , use --help for more info")  # do this
    elif not options.new_mac:  # If there is no new mac specified defined then,
        parser.error("[-] Please specify a new MAC_Address , use --help for more info")  # do this
    else:
        return options


def change_mac(network_interface_input, new_mac):
    print("[+] Changing Mac Address for " + network_interface_input + " to " + new_mac)
    # The 1st argument is the command to process
    # The 2nd argument is the command to say that its using linux
    subprocess.call(["ifconfig", network_interface_input, "down"])
    subprocess.call(["ifconfig", network_interface_input, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", network_interface_input, "up"])


def get_current_mac(network_interface_input):
    mac_change_confirmation = subprocess.check_output(["ifconfig", network_interface_input])
    # -------------------------------------The rule to be stated - the variable containing output info
    filtered_mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", mac_change_confirmation)
    if filtered_mac_result:  # if the filtered_mac_address indeed found an interface with a mac address functionality
        return filtered_mac_result.group(0)  # Then do this stuff which returns to the current_ mac variable
    else:  # else do this stuff
        print("[-] Couldn't read any Mac Address to change")


options = get_arguments()  # calling 1st function

current_mac = get_current_mac(options.new_mac)  # calling 2nd function
print("Current Mac_Address is :" + str(current_mac))

change_mac(options.network_interface_input, options.new_mac)  # calling 3rd function

current_mac = get_current_mac(options.network_interface_input)
# Later we use an if statement to check if the "current_mac" holds the new mac value (which is in
# options.network_interface_inout) which the user inputs

if current_mac == options.new_mac:
    print("[+] The Mac address ha been successfully changed to " + current_mac)
else:
    print("[-] The mac address did not change!")

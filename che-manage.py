import os
import netifaces as ni

os.system('clear')

print('\n********************************\n*Eclipse Che Management Console*\n********************************\n')

modeopt = raw_input('Select your option:\n\n1. Run Eclipse Che Server\n2. Stop Eclipse Che Server\n3. Quit\n\nYour option: ')

if modeopt == '1':
    os.system('clear')
    option1 = raw_input('Select how you want to set the IP address of the Eclipse Che service:\n\n1. Auto-Detect IP address of given interface\n2. Auto-Detect the Interface that is used to connect to the Internet and obtain the IP address\n3. Manually enter the IP address\n4. Exit Program\n\nYour Option: ')

    if option1 == '1':
        os.system('clear')
        iface = raw_input('Enter Interface Name: ')
        ni.ifaddresses(iface)
        ip = ni.ifaddresses(iface)[ni.AF_INET][0]['addr']
        os.system('sudo docker run -it -e CHE_MULTIUSER=true -e CHE_HOST=' + ip + ' -v /var/run/docker.sock:/var/run/docker.sock -v ~/.che-multiuser:/data eclipse/che start')

    elif option1 == '3':
        os.system('clear')
        address = raw_input('\nEnter the IP Address you want to start Eclipse Che: ')
        os.system('sudo docker run -it -e CHE_MULTIUSER=true -e CHE_HOST=' + address + ' -v /var/run/docker.sock:/var/run/docker.sock -v ~/.che-multiuser:/data eclipse/che start')

    elif option1 == '4':
        os.system('clear')
        print('Quitting...')


elif modeopt == "2":
    os.system('clear')
    address = raw_input('\nEnter the IP Address you want to stop Eclipse Che: ')
    os.system('sudo docker run -it -e CHE_MULTIUSER=true -e CHE_HOST=' + address + ' -v /var/run/docker.sock:/var/run/docker.sock -v ~/.che-multiuser:/data eclipse/che stop --skip:graceful')

elif modeopt == "3":
    os.system('clear')
    print("\nQuitting...")

\else:
    print("\nYou did not enter a valid option. Exiting program...")

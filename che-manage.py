import os
import netifaces as ni
import socket
#This is a test
os.system('clear')

print('********************************\n*Eclipse Che Management Console*\n********************************\n')

modeopt = raw_input('Select your option:\n\n1. Run Eclipse Che Server\n2. Stop Eclipse Che Server\n3. Quit\n\nYour option: ')

if modeopt == '1':
    os.system('clear')
    netopt = raw_input('Are you connected to a network? (Y)es/(N)o: ')
    os.system('clear')

    if netopt == 'yes' or netopt == 'y' or netopt =='Y' or netopt == 'Yes':
        option1 = raw_input('Select how you want to set the IP address of the Eclipse Che service:\n\n1. Auto-Detect IP address of given interface\n2. Auto-Detect the Interface that is used to connect to the Internet and obtain the IP address\n3. Manually enter the IP address\n4. Exit Program\n\nYour Option: ')
        if option1 == '1':
            os.system('clear')
            iface = raw_input('Enter Interface Name: ')
            ni.ifaddresses(iface)
            ip = ni.ifaddresses(iface)[ni.AF_INET][0]['addr']
            os.system('clear')
            option2 = raw_input('Detected IP address is ' + ip + '. Do you wish to continue? (Y)es/(N)o: ')
            if option2 == 'Yes' or option2 == 'yes' or option2 == 'Y' or option2 == 'y':
                os.system('sudo docker run -it -e CHE_MULTIUSER=true -e CHE_HOST=' + ip + ' -v /var/run/docker.sock:/var/run/docker.sock -v ~/.che-multiuser:/data eclipse/che start')
            elif option2 == 'No' or option2 == 'no' or option2 =='N' or option2 == 'n':
                os.system('clear')
                ip2 = raw_input('Enter an IP address you wish to start Eclipse Che on: ')
                os.system('sudo docker run -it -e CHE_MULTIUSER=true -e CHE_HOST=' + ip2 + ' -v /var/run/docker.sock:/var/run/docker.sock -v ~/.che-multiuser:/data eclipse/che start')

        elif option1 == '2':
            os.system('clear')
            def get_ip_address():
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(("8.8.8.8", 80))
                return s.getsockname()[0]
            print('Detected IP address is: ' + get_ip_address())
            print('\nStarting Eclipse Che on Detected IP...\n')
            os.system('sudo docker run -it -e CHE_MULTIUSER=true -e CHE_HOST=' + get_ip_address() + ' -v /var/run/docker.sock:/var/run/docker.sock -v ~/.che-multiuser:/data eclipse/che start')

        elif option1 == '3':
            os.system('clear')
            address = raw_input('\nEnter the IP Address you want to start Eclipse Che: ')
            os.system('sudo docker run -it -e CHE_MULTIUSER=true -e CHE_HOST=' + address + ' -v /var/run/docker.sock:/var/run/docker.sock -v ~/.che-multiuser:/data eclipse/che start')

        elif option1 == '4' or option1 == 'exit':
            os.system('clear')
            print('Quitting...')
        else:
            print('\nYou entered an invalid option. Exiting...')
            
    if netopt == 'no' or netopt == 'n' or netopt =='N' or netopt == 'No':
        option1 = raw_input('Select how you want to set the IP address of the Eclipse Che service:\n\n1. Auto-Detect IP address of given interface\n2. Manually enter the IP address\n3. Exit Program\n\nYour Option: ')
        if option1 == '1':
            os.system('clear')
            iface = raw_input('Enter Interface Name: ')
            ni.ifaddresses(iface)
            ip = ni.ifaddresses(iface)[ni.AF_INET][0]['addr']
            os.system('sudo docker run -it -e CHE_MULTIUSER=true -e CHE_HOST=' + ip + ' -v /var/run/docker.sock:/var/run/docker.sock -v ~/.che-multiuser:/data eclipse/che start --fast')

        elif option1 == '2':
            os.system('clear')
            address = raw_input('\nEnter the IP Address you want to start Eclipse Che: ')
            os.system('sudo docker run -it -e CHE_MULTIUSER=true -e CHE_HOST=' + address + ' -v /var/run/docker.sock:/var/run/docker.sock -v ~/.che-multiuser:/data eclipse/che start')

        elif option1 == '3' or option1 == 'exit':
            os.system('clear')
            print('Quitting...')
        else:
            print('\nYou entered an invalid option. Exiting...')


elif modeopt == "2":
    os.system('clear')
    address = raw_input('Enter the IP Address you want to stop Eclipse Che: ')
    os.system('sudo docker run -it -e CHE_MULTIUSER=true -e CHE_HOST=' + address + ' -v /var/run/docker.sock:/var/run/docker.sock -v ~/.che-multiuser:/data eclipse/che stop --skip:graceful --fast')

elif modeopt == "3":
    os.system('clear')
    print("\nQuitting...")

else:
    print("\nYou did not enter a valid option. Exiting program...")

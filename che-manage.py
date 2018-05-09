import os

os.system('clear')
print('\n********************************\n*Eclipse Che Management Console*\n********************************\n')
modeopt = raw_input('Select your option:\n\n1. Run Eclipse Che Server\n2. Stop Eclipse Che Server\n3. Quit\n\nYour option: ')

if modeopt == "1":
    os.system('clear')
    address = raw_input('\nEnter the IP Address you want to start Eclipse Che: ')
    os.system('sudo docker run -it -e CHE_MULTIUSER=true -e CHE_HOST=' + address + ' -v /var/run/docker.sock:/var/run/docker.sock -v ~/.che-multiuser:/data eclipse/che start')

elif modeopt == "2":
    os.system('clear')
    address = raw_input('\nEnter the IP Address you want to start Eclipse Che: ')
    os.system('sudo docker run -it -e CHE_MULTIUSER=true -e CHE_HOST=' + address + ' -v /var/run/docker.sock:/var/run/docker.sock -v ~/.che-multiuser:/data eclipse/che stop --skip:graceful')

elif modeopt == "3":
    os.system('clear')
    print("\nQuitting...")

else:
    print("You did not enter a valid option. Exiting program...")

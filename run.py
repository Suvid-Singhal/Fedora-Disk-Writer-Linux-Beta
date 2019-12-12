import wget
import os
import requests
dir=os.getcwd()

def verifyISO(loc):
	print("\nVerifying ISO...")
	os.system("curl https://getfedora.org/static/fedora.gpg | gpg --import")
	os.system("gpg --verify-files *-CHECKSUM.txt")
	checksum=requests.get("https://spins.fedoraproject.org/static/checksums/Fedora-Spins-31-1.9-x86_64-CHECKSUM")
	checksum=checksum.text
	f = open('Fedora-Spins-31-1.9-x86_64-CHECKSUM.txt', 'w')
	f.write(checksum)
	f.close()
	print("\n[+]Verifying Checksum...")
	os.system("gpg --verify-files Fedora-Spins-31-1.9-x86_64-CHECKSUM.txt")
	print("\n\n[*]Please match the primary key fingerprint with your version here:- https://spins.fedoraproject.org/en/verify")	



def UEFIverify(loc):
	print("Does your system support UEFI?")
	uefi=input()
	if uefi == 'no' or uefi=='No':
		os.system("sudo umount "+newdevice)
		os.system("sudo dd bs=4M if="+meow+"+ of="+newdevice+" conv=fdatasync  status=progress")
	else:
		print("Warning! We will now format your USB and erase everything present on it...")
		os.system("sudo mkfs.vfat -F32 "+newdevice)
		os.system("sudo mkdir ~/USB")
		os.system("sudo mount "+newdevice+" ~/USB")
		os.system("sudo mkdir ~/ISOmountPoint")
		os.system("sudo mount -o loop "+str(loc)+" ~/ISOmountPoint")
		os.system("sudo umount ~/ISOmountPoint")
		os.system("sudo cp -r ~/ISOmountPoint* ~/USB")
		os.system("sudo umount "+newdevice)



print("\033[93m \n\n***********************************************************")
print("Welcome to Fedora Disk Writer (CLI Beta version) for Linux")
print("***********************************************************\n")
print("Before procedding please backup any important data that you don't want to get deleted from the USB to a safe place...")
print("\nDo you already have a Fedora ISO?")
hehe=input()


if hehe=='yes':
	print("\nEnter the location of the Fedora ISO:")
	loc=input()

	verifyISO(loc)

	print("\nNow, select your USB device (not partition) from the list of devices:\n")

	os.system("lsblk")

	device=input()
	newdevice='/dev/'+device
	UEFIverify(loc)



else:


	print("\nWhich Fedora Spin do you want?")
	print("\n1. KDE Plasma (Regular)")
	print("2. XFCE")
	print("3. LXQT")
	print("4. MATE-COMPIZ")
	print("5. Cinnamon")
	print("6. LXDE")
	print("7. SOAS")
	print("\nPress CTRL+C to quit!")
	selection=int(input())
	print("\nStarting download...")
	if selection == 1:
		url = 'https://download.fedoraproject.org/pub/fedora/linux/releases/31/Spins/x86_64/iso/Fedora-KDE-Live-x86_64-31-1.9.iso'
		meow=dir+'Fedora-KDE-Live-x86_64-31-1.iso'
		wget.download(url, meow)
	if selection == 2:
		url = 'https://download.fedoraproject.org/pub/fedora/linux/releases/31/Spins/x86_64/iso/Fedora-Xfce-Live-x86_64-31-1.9.iso'
		meow=dir+'Fedora-Xfce-Live-x86_64-31-1.9.iso'
		wget.download(url, meow)
	if selection == 3:
		url = 'https://download.fedoraproject.org/pub/fedora/linux/releases/31/Spins/x86_64/iso/Fedora-LXQt-Live-x86_64-31-1.9.iso'
		meow=dir+'Fedora-LXQt-Live-x86_64-31-1.9.iso'
		wget.download(url, meow)
	if selection == 4:
		url = 'https://download.fedoraproject.org/pub/fedora/linux/releases/31/Spins/x86_64/iso/Fedora-MATE_Compiz-Live-x86_64-31-1.9.iso'
		meow=dir+'Fedora-MATE_Compiz-Live-x86_64-31-1.9.iso'
		wget.download(url, meow)
	if selection == 5:
		url = 'https://download.fedoraproject.org/pub/fedora/linux/releases/31/Spins/x86_64/iso/Fedora-Cinnamon-Live-x86_64-31-1.9.iso'
		meow=dir+'Fedora-Cinnamon-Live-x86_64-31-1.9.iso'
		wget.download(url, meow)
	if selection == 6:
		url = 'https://download.fedoraproject.org/pub/fedora/linux/releases/31/Spins/x86_64/iso/Fedora-LXDE-Live-x86_64-31-1.9.iso'
		meow=dir+'Fedora-LXDE-Live-x86_64-31-1.9.iso'
		wget.download(url, meow)
	if selection == 7:
		url = 'https://download.fedoraproject.org/pub/fedora/linux/releases/31/Spins/x86_64/iso/Fedora-SoaS-Live-x86_64-31-1.9.iso'
		meow=dir+'Fedora-SoaS-Live-x86_64-31-1.9.iso'
		wget.download(url, meow)


	print("\nDownload Completed!\n")

	verifyISO(meow)

	print("Now, select your USB device (not partition) from the list of devices:\n")

	os.system("lsblk")

	device=input()
	newdevice='/dev/'+device
	UEFIverify(meow)

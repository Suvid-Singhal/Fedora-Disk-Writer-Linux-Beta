import wget
import os
dir=os.getcwd()

print("Welcome to Fedora Disk Writer (CLI Beta version) for Linux\n")
print("Before procedding please backup any important data that you don't want to get deleted from the USB to a safe place...")
print("\nDo you already have a Fedora ISO?")
hehe=input()
if hehe=='yes':
	print("Enter the location of the Fedora ISO:")
	loc=input()


	print("Now, select your USB device (not partition) from the list of devices:\n")

	os.system("lsblk")

	device=input()
	newdevice='/dev/'+device
	print("Does your system support UEFI?")
	uefi=input()
	if uefi == 'no' or uefi=='No':
		os.system("sudo umount "+newdevice)
		os.system("sudo dd bs=4M if="+loc+"+ of="+newdevice+" conv=fdatasync  status=progress")
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
else:


	print("Which Fedora Spin do you want?")
	print("1. KDE Plasma (Regular)")
	print("2. XFCE")
	print("3. LXQT")
	print("4. MATE-COMPIZ")
	print("5. Cinnamon")
	print("6. LXDE")
	print("7. SOAS")
	print("\nPress CTRL+C to quit!")
	selection=int(input())
	print("Starting download...")
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


	print("Download Completed!\n")

	print("Now, select your USB device (not partition) from the list of devices:\n")

	os.system("lsblk")

	device=input()
	newdevice='/dev/'+device
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

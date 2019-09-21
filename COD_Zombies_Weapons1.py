import os
import time
from enum import Enum

print('Loading .........')

class WeaponDetails:
	number_of_guns = 0
	weapons = []
	weapons_by_class = {}

	def __init__(self, name, weapon_class, damage, distance, fire_rate, accuracy, mags, rounds_in_mags, wall_buy, attachments):
		self.name = name
		self.weapon_class = weapon_class
		self.damage = damage
		self.distance = distance
		self.fire_rate = fire_rate
		self.accuracy = accuracy
		self.mags = mags
		self.rounds_in_mags = rounds_in_mags
		self.total_ammo = mags * rounds_in_mags
		self.wall_buy = wall_buy
		self.attachments = attachments
		WeaponDetails.weapons.append(self)
		WeaponDetails.number_of_guns += 1
	
		wc = WeaponClass(weapon_class)
		if wc in WeaponDetails.weapons_by_class:
			WeaponDetails.weapons_by_class[wc].append(self)
		else:
			WeaponDetails.weapons_by_class[wc] = [self]

	def __repr__(self):
		return "WeaponDetails('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(self.name, self.weapon_class, self.damage, self.distance, self.fire_rate, self.accuracy, self.mags, self.rounds_in_mags, self.wall_buy, self.attachments) + '\n'
	
	def __str__(self):
		return f'Weapon {self.name} of the {self.weapon_class} class '

	def stats(self):
		self.default_stats = "Weapon Name: " + self.name + "\nWeapon Class: " + self.weapon_class + "\nDamage: " + str(self.damage) + " / 20\nDistance: " + str(self.distance) + " / 20\nFire Rate: " + str(self.fire_rate)  + " / 20\nAccuracy: " + str(self.accuracy) + " / 20\nNumber of Magazines: " + str(self.mags) + "\nRounds in Magazines: " + str(self.rounds_in_mags) + "\nTotal Amount of Ammo: " + str(self.total_ammo) + "\nCan Buy Off of The Wall: " + str(self.wall_buy) + "\nCan Have Attachments: " + str(self.attachments)
		return self.default_stats

	@staticmethod
	def get_in_stat(key, wc=None):
		if wc:			
			return max(WeaponDetails.weapons_by_class[wc], key=key)
		else:
			return max(WeaponDetails.weapons, key=key)
	
	@staticmethod
	def adjustable_weapon_stats(self):
		self.weapon_stats = [self.damage, self.distance, self.fire_rate, self.accuracy, self.mags, self.rounds_in_mags]
		return self.weapon_stats

class WeaponClass(Enum):
	AR = "Assault Rifle"
	SMG = "Submachine Gun"
	TR = "Tactical Rifle"
	LMG = "Light Machine Gun"
	SR = "Sniper Rifle"
	SEC = "Secondaries"

class Attachments:
	all_attachments = []
	Attachment_By_Class = {}

	def __init__(self, position, name, damage, distance, fire_rate, accuracy, mags, rounds_in_mags):
		self.position = position
		self.name = name
		self.damage = damage
		self.distance = distance
		self.fire_rate = fire_rate
		self.accuracy = accuracy
		self.mags = mags
		self.rounds_in_mags = rounds_in_mags
		Attachments.all_attachments.append(self)

		ac = AttachmentClass(position)
		if ac in Attachments.Attachment_By_Class:
			Attachments.Attachment_By_Class[ac].append(self)
		else:
			Attachments.Attachment_By_Class[ac] = [self]

	def attachmentstats(self):
		self.attach_stats = "Attachment Name: " + self.name + "\nAttachment Class: " + self.position + "\nDamage Boost: " + str(self.damage) + " / 20\nDistance Boost: " + str(self.distance) + " / 20\nFire Rate Boost: " + str(self.fire_rate)  + " / 20\nAccuracy Boost: " + str(self.accuracy) + " / 20\nNumber of Magazines Boost: " + str(self.mags) + "\nRounds in Magazines Boost: " + str(self.rounds_in_mags)
		return self.attach_stats

	@staticmethod
	def adjustable_attachment_stats(self):
		stat_list = []
		if self.damage > 0:
			adjustable_attachment_stats.stat_list.append(self.damage)
		if self.distance > 0:
			adjustable_attachment_stats.stat_list.append(self.distance)
		if self.fire_rate > 0:
			adjustable_attachment_stats.stat_list.append(self.fire_rate)
		if self.accuracy > 0:
			adjustable_attachment_stats.stat_list.append(self.accuracy)
		if self.mags > 0:
			adjustable_attachment_stats.stat_list.append(self.mags)
		if self.rounds_in_mags > 0:
			adjustable_attachment_stats.stat_list.append(self.rounds_in_mags)
		return stat_list

class AttachmentClass(Enum):
	OPT = "Optics"
	ATT = "Attachments"
	OPMOD = "Operator Mod"

def formated_attachment_list():
	list1 = Attachments.attachmentstats(all_attachments)
	return list1
#Weapons
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
#Assault Rifles
WeaponDetails('ICR 7', 'Assault Rifle', 6, 10, 12, 12, 3, 35, True, True)
WeaponDetails('MADDOX RFB', 'Assault Rifle', 6, 10, 14, 8, 3, 40, True, True)
WeaponDetails('KN-57', 'Assault Rifle', 7, 9, 11, 10, 3, 35, True, True)
WeaponDetails('HITCHCOCK M9', 'Assault Rifle', 11, 10, 14, 8, 10, 30, False, False)
WeaponDetails('RAMPART 17', 'Assault Rifle', 10, 11, 10, 8, 3, 30, False, True)
WeaponDetails('VAPR XKG', 'Assault Rifle', 6, 10, 13, 11, 3, 35, True, True)
WeaponDetails('GRAV', 'Assault Rifle', 8, 9, 11, 10, 3, 35, False, False)
WeaponDetails('SWAT RFT', 'Assault Rifle', 8, 10, 13, 11, 3, 35, False, True)

#Submachine Guns
WeaponDetails('ESCARGOT', 'Submachine Gun', 4, 3, 15, 6, 10, 30, True, False)
WeaponDetails('MX9', 'Submachine Gun', 6, 5, 14, 7, 3, 35, True, True)
WeaponDetails('SPITFIRE', 'Submachine Gun', 7, 2, 17, 5, 4, 34, True, True)
WeaponDetails('SAUG 9MM', 'Submachine Gun', 3, 3, 16, 9, 3, 36, True, True)
WeaponDetails('GKS', 'Submachine Gun', 6, 9, 13, 11, 3, 38, True, True)
WeaponDetails('CORDITE', 'Submachine Gun', 5, 5, 15, 6, 3, 60, False, True)
WeaponDetails('M1927', 'Submachine Gun', 6, 3, 16, 6, 7, 50, False, False)
WeaponDetails('MP-40', 'Submachine Gun', 7, 4, 10, 8, 3, 32, False, False)
WeaponDetails('DAEMON 3XB', 'Submachine Gun', 5, 3, 18, 6, 3, 36, False, True)

#Tactical Rifles
WeaponDetails('SWORDFISH', 'Tactical Rifle', 5, 10, 13, 14, 3, 36, True, True)
WeaponDetails('ESSEX MODEL 07', 'Tactical Rifle', 9, 9, 3, 12, 10, 5, True, False)
WeaponDetails('ABR 223', 'Tactical Rifle', 11, 10, 12, 9, 3, 30, False, True)
WeaponDetails('AUGER DMR', 'Tactical Rifle', 10, 9, 5, 11, 3, 20, True, True)

#Light Machine Gun
WeaponDetails('TITAN', 'Light Machine Gun', 10, 14, 9, 8, 3, 75, True, True)
WeaponDetails('HADES', 'Light Machine Gun', 11, 12, 14, 7, 3, 65, False, True)
WeaponDetails('VKM 750', 'Light Machine Gun', 10, 14, 7, 6, 3, 50, False, True)
WeaponDetails('ZWEIHANDER', 'Light Machine Gun', 10, 9, 5, 11, 3, 20, False, False)

#Sniper Rifles
WeaponDetails('SDM', 'Sniper Rifle', 16, 16, 6, 12, 3, 12, False, True)
WeaponDetails('PALADIN HB50', 'Sniper Rifle', 20, 16, 1, 9, 3, 5, False, True)
WeaponDetails('KOSHKA', 'Sniper Rifle', 19, 16, 2, 11, 3, 6, True, True)
WeaponDetails('OUTLAW', 'Sniper Rifle', 19, 16, 3, 13, 3, 9, False, True)

#Secondaries
WeaponDetails('BOWIE KNIFE', 'Secondaries', 20, 2, 2, 16, 0, 0, True, False)
WeaponDetails('WELLING', 'Secondaries', 3, 8, 8, 11, 50, 8, False, False)
WeaponDetails('MOZU', 'Secondaries', 14, 6, 7, 7, 4, 6, True, True)
WeaponDetails('M1897 TREBUCHET', 'Secondaries', 10, 3, 3, 5, 10, 8, True, False)
WeaponDetails('STRIFE', 'Secondaries', 6, 8, 8, 11, 3, 12, True, True)
WeaponDetails('RK 7 GARRISON', 'Secondaries', 8, 3, 12, 9, 3, 15, True, True)
WeaponDetails('SG12', 'Secondaries', 11, 3, 6, 4, 4, 6, False, True)
WeaponDetails('HELLION SALVO', 'Secondaries', 20, 19, 2, 16, 3, 1, False, True)
WeaponDetails('MOG 12', 'Secondaries', 9, 3, 3, 5, 4, 4, True, True)
WeaponDetails('KAP 45', 'Secondaries', 8, 5, 15, 4, 3, 20, False, True)

#Attachments
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
#Optics
Attachments('Optics', 'Reflex', 0, 0, 0, 1, 0, 0)
Attachments('Optics', 'Recon', 1, 0, 0, 1, 0, 0)
Attachments('Optics', 'Holographic', 0, 0, 0, 1, 0, 0)
Attachments('Optics', 'Dual Zoom', 0, 1, 0, 1, 0, 0)
Attachments('Optics', 'Threat Detector', 0, 0, 0, 2, 0, 0)
Attachments('Optics', 'ELO', 0, 0, 0, 1, 0, 0)
Attachments('Optics', 'Iron Sights', 0, 0, 0, 0, 0, 0)
Attachments('Optics', 'Compact Scope', 0, 1, 0, 1, 0, 0)

#Attachments
Attachments('Attachments', 'Grip', 0, 0, 0, 1, 0, 0)
Attachments('Attachments', 'Grip II', 0, 0, 0, 2, 0, 0)
Attachments('Attachments', 'FMJ', 1, 0, 0, 0, 0, 0)
Attachments('Attachments', 'FMJ II', 1, 0, 0, 0, 0, 0)
Attachments('Attachments', 'Long Barrel', 0, 2, 0, 0, 0, 0)
Attachments('Attachments', 'Long Barrel', 0, 1, 0, 1, 0, 0)
Attachments('Attachments', 'Quickdraw', 0, 0, 0, 1, 0, 0)
Attachments('Attachments', 'Quickdraw II', 0, 0, 0, 2, 0, 0)
Attachments('Attachments', 'Laser Sight', 0, 0, 0, 1, 0, 0)
Attachments('Attachments', 'Laser Sight II', 0, 0, 0, 2, 0, 0)
Attachments('Attachments', 'Fast Mags', 0, 0, 0, 0, 0, 0)
Attachments('Attachments', 'Fast Mags II', 0, 0, 0, 1, 0, 0)
Attachments('Attachments', 'Stock', 0, 0, 0, 1, 0, 0)
Attachments('Attachments', 'Hybrid Mags', 0, 0, 0, 0, 0, 10)
Attachments('Attachments', 'Extended Mags', 0, 0, 0, 0, 0, 20)
Attachments('Attachments', 'Extended Mags II', 0, 0, 0, 0, 0, 75)
Attachments('Attachments', 'Rapid Fire', 0, 0, 1, 0, 0, 0)
Attachments('Attachments', 'Rapid Fire II', 0, 0, 2, 0, 0, 0)
Attachments('Attachments', 'Supressor', 0, -1, 0, 0, 0, 0)
Attachments('Attachments', 'High Caliber', 1, 0, 0, 0, 0, 0)
Attachments('Attachments', 'High Caliber II', 2, 0, 0, 0, 0, 0)
Attachments('Attachments', 'Steady Grip', 0, 0, 0, 2, 0, 0)
Attachments('Attachments', 'Stabilizer', 0, 0, 0, 2, 0, 0)


def Zombies_art():
	print("""_________        .__  .__            _____  ________          __               
\\_   ___ \\_____  |  | |  |     _____/ ____\\ \\______ \\  __ ___/  |_ ___.__. /\\  
/    \\  \\/\\__  \\ |  | |  |    /  _ \\   __\\   |    |  \\|  |  \\   __<   |  | \\/  
\\     \\____/ __ \\|  |_|  |__ (  <_> )  |     |    `   \\  |  /|  |  \\___  | /\\  
 \\______  (____  /____/____/  \\____/|__|    /_______  /____/ |__|  / ____| \\/  
        \\/     \\/                                   \\/             \\/          
__________.__                 __     ________                 .___.___.___.___ 
\\______   \\  | _____    ____ |  | __ \\_____  \\ ______  ______ |   |   |   |   |
 |    |  _/  | \\__  \\ _/ ___\\|  |/ /  /   |   \\____ \\/  ___/  |   |   |   |   |
 |    |   \\  |__/ __ \\  \\___ |    <  /    |    \\ |_> >___  \\  |   |   |   |   |
 |______  /____(____  /\\___ >__|_  \\ \\_______  /   __/____  > |___|___|___|___|
        \\/          \\/     \\/     \\/         \\/|__|       \\/                   
__________________      _____ __________.______________ _________              
\\____    /\\_____  \\    /     \\______   \\   \\_   _____//   _____/              
  /     /  /   |   \\  /  \\ /  \\|    |  _/   ||    __)_ \\_____  \\               
 /     /_ /    |    \\/    Y    \\    |   \\   ||        \\/        \\              
/_______ \\_______  /\\____|__  /______  /___/_______  /_______  /              
        \\/       \\/         \\/       \\/            \\/        \\/               
        """)
def zombies_menu():
	answer = 0
	while answer == 0:
		Zombies_art()
		print('\n\nWhat Would You Like To Do?\n\n')
		print('Option 1: Find Gun Stats')
		print('Option 2: Most Accurate Gun')
		print('Option 3: Highest Damage Gun')
		print('Option 4: Fastest Firing Rate')
		print('Option 5: Furthest Range')
		print('Option 6: Highest Ammo Capacity')
		print('Option 7: Test Gun Stats With Attachments')
		print('Option 8: Exit')
		Selection = input('')
		if Selection == '1':
			os.system('cls')
			menu_items = list(WeaponClass)
			Class_Selected = ShowMenu(menu_items, lambda w: w.value)
			if Class_Selected is not None:
				ListOfWeapons = WeaponDetails.weapons_by_class[Class_Selected]
				Weapon_Selected = ShowMenu(ListOfWeapons, lambda w: w.name)
				if Weapon_Selected is not None:
					print(Weapon_Selected.stats())
				
		elif Selection == '2':
			os.system('cls')
			menu_items = list(WeaponClass)
			Class_Selected = ShowMenu(menu_items, lambda w: w.value, True)
			if Class_Selected is menu_items:
				info = WeaponDetails.get_in_stat(lambda w: w.accuracy)
				print(f'{info}has the best accuracy with {info.accuracy}')
			elif Class_Selected is not None:
				info = WeaponDetails.get_in_stat(lambda w: w.accuracy, Class_Selected)
				print(f'{info}has the best accuracy with {info.accuracy}')

		elif Selection == '3':
			os.system('cls')
			menu_items = list(WeaponClass)
			Class_Selected = ShowMenu(menu_items, lambda w: w.value, True)
			if Class_Selected is menu_items:
				info = WeaponDetails.get_in_stat(lambda w: w.damage)
				print(f'{info}has the highest highest damage with {info.damage}')
			elif Class_Selected is not None:
				info = WeaponDetails.get_in_stat(lambda w: w.damage, Class_Selected)
				print(f'{info}has the highest highest damage with {info.damage}')

		elif Selection == '4':
			os.system('cls')
			menu_items = list(WeaponClass)
			Class_Selected = ShowMenu(menu_items, lambda w: w.value, True)
			if Class_Selected is menu_items:
				info = WeaponDetails.get_in_stat(lambda w: w.fire_rate)
				print(f'{info}has the highest fastest firing rate with {info.fire_rate}')
			elif Class_Selected is not None:
				info = WeaponDetails.get_in_stat(lambda w: w.fire_rate, Class_Selected)
				print(f'{info}has the highest fastest firing rate with {info.fire_rate}')

		elif Selection == '5':
			os.system('cls')
			menu_items = list(WeaponClass)
			Class_Selected = ShowMenu(menu_items, lambda w: w.value, True)
			if Class_Selected is menu_items:
				info = WeaponDetails.get_in_stat(lambda w: w.distance)
				print(f'{info}has the furthest range with {info.distance}')
			elif Class_Selected is not None:
				info = WeaponDetails.get_in_stat(lambda w: w.distance, Class_Selected)
				print(f'{info}has the furthest range with {info.distance}')

		elif Selection == '6':
			os.system('cls')
			menu_items = list(WeaponClass)
			Class_Selected = ShowMenu(menu_items, lambda w: w.value, True)
			if Class_Selected is menu_items:
				info = WeaponDetails.get_in_stat(lambda w: w.total_ammo)
				print(f'{info}has the highest ammo capacity with {info.total_ammo}')
			elif Class_Selected is not None:
				info = WeaponDetails.get_in_stat(lambda w: w.total_ammo, Class_Selected)
				print(f'{info}has the highest ammo capacity with {info.total_ammo}')

		elif Selection == '7':
			os.system('cls')
			WIP()
			menu_items = list(WeaponClass)
			Class_Selected = ShowMenu(menu_items, lambda w: w.value)
			if Class_Selected is not None:
				menu_items = WeaponDetails.weapons_by_class[Class_Selected]
				Weapon_Selected = ShowMenu(menu_items, lambda w: w.name)
				if Weapon_Selected is not None:
					print(f'You selected the {Weapon_Selected.name}.')
					menu_items = list(AttachmentClass)
					Attachment_Class = ShowMenu(menu_items, lambda w: w.value)
					if Attachment_Class is not None:
						menu_items = Attachments.Attachment_By_Class[Attachment_Class]
						Add_attachment = ShowMenu(menu_items, lambda w: w.name)
						#debug lines 285, 291, 293
						if Add_attachment is not None:
							print(f'You selected {Add_attachment.name}')
							print(Weapon_Selected.stats() + '\n\n' + Add_attachment.attachmentstats() + '\n\n\n\n' + '')
							WeaponDetails.adjustable_weapon_stats(Weapon_Selected)
							print(Add_attachment.adjustable_attachment_stats())

		elif Selection == '8':
			answer = 1
			os.system('cls')
			Exit()
		else:
			print("Please only type the selected options, Numbers Only.")

def ShowMenu(menu_items, key, showall=False):
	answer = 0
	while answer == 0:
		for i, x in enumerate(menu_items, 1):
			print('Option {}: {}'.format(i, key(x)))
		if showall:
			print('Option {}: Best in Slot'.format(len(menu_items) + 1))
			print('Option {}: Back'.format(len(menu_items) + 2))
			max_num = len(menu_items) + 2
		elif not showall:
			print('Option {}: Back'.format(len(menu_items) + 1))
		Selection = input('')
		if Selection.isdigit():
			Select_Num = int(Selection)
			if Select_Num <= len(menu_items) and Select_Num >= 1:
				Class_Selected = menu_items[Select_Num - 1]
				os.system('cls')
				return Class_Selected
			elif not showall and Select_Num == len(menu_items) + 1 or showall and Select_Num == max_num:
				os.system('cls')
				return None
			elif showall and len(menu_items) + 1:
				os.system('cls')
				return menu_items
			else:
				os.system('cls')
				print('Stop Headbutting Your Keyboard! Type only numbers within the Menu, Thanks!')
		else:
			os.system('cls')	
			print("Please only type the selected options.")

def WIP():
	os.system('cls')
	print('This is still under Construction! Please Be Fucking Patient!')

def Exit():
	print('Special Thanks to Riffautae, from the Python Discord, for all the help in simplifying the code.\nIf you see him around tell him Thank You if you like this project.')
	time.sleep(10)
os.system('cls')
zombies_menu()
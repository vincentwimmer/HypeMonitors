import re
import json
import requests
import threading
from time import sleep
from datetime import datetime
from datetime import timedelta
import random
from dhooks import Webhook, Embed
import linecache
import sys
import gc

getuserjsonfile = '/Database/vmonitorsShopifyUsers.json'
with open(getuserjsonfile) as useraccountsf:
	useraccounts = json.load(useraccountsf)

def updateAccountJSON():
	global useraccounts
	while True:
		try:
			sleep(30)		
			with open(getuserjsonfile) as useraccountsf:
				useraccounts = json.load(useraccountsf)
		except:
			sleep(1)

def getProxies():
	proxy = []
	proxy_txt = open('/Database/proxies.txt', 'r')
	for proxies in proxy_txt:
		proxies = proxies.strip('\n')
		proxy.append(proxies)
	proxy_txt.close()
	return proxy

def getUserAgents():
	useragent = []
	useragent_txt = open('/Database/useragents.txt', 'r')
	for useragents in useragent_txt:
		useragents = useragents.strip('\n')
		useragent.append(useragents)
	useragent_txt.close()
	return useragent
#

# Gather all Discord distros

# New Unfilitered Channels
def getNewUnf():
	NewUnfdiscords = []
	userlist = useraccounts['users']
	NewUnfdiscords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['Shopify New'] != None and item['Shopify New'] != "":
			NewUnfdiscords.append(item['Shopify New'])
	return NewUnfdiscords

def getPubUnf():
	PubUnfdiscords = []
	userlist = useraccounts['users']
	PubUnfdiscords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['Shopify Published'] != None and item['Shopify Published'] != "":
			PubUnfdiscords.append(item['Shopify Published'])
	return PubUnfdiscords

# Updated Unfilitered Channels
def getUpdUnf():
	UpdUnfdiscords = []
	userlist = useraccounts['users']
	UpdUnfdiscords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['Shopify Unfiltered'] != None and item['Shopify Unfiltered'] != "":
			UpdUnfdiscords.append(item['Shopify Unfiltered'])
	return UpdUnfdiscords

# Jays/Nike Channels
def getJayNi():
	JayNikdiscords = []
	userlist = useraccounts['users']
	JayNikdiscords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['Shopify Jordan/Nike'] != None and item['Shopify Jordan/Nike'] != "":
			JayNikdiscords.append(item['Shopify Jordan/Nike'])
	return JayNikdiscords

# Yzy Channels
def getYzy():
	YZYdiscords = []
	userlist = useraccounts['users']
	YZYdiscords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['Shopify YZY'] != None and item['Shopify YZY'] != "":
			YZYdiscords.append(item['Shopify YZY'])
	return YZYdiscords

# Adidas Channels
def getAdis():
	Adiddiscords = []
	userlist = useraccounts['users']
	Adiddiscords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['Shopify Adidas'] != None and item['Shopify Adidas'] != "":
			Adiddiscords.append(item['Shopify Adidas'])
	return Adiddiscords

# Converse Channels
def getCons():
	Consdiscords = []
	userlist = useraccounts['users']
	Consdiscords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['Shopify Converse'] != None and item['Shopify Converse'] != "":
			Consdiscords.append(item['Shopify Converse'])
	return Consdiscords

def getVans():
	Vansdiscords = []
	userlist = useraccounts['users']
	Vansdiscords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['Shopify Vans'] != None and item['Shopify Vans'] != "":
			Vansdiscords.append(item['Shopify Vans'])
	return Vansdiscords

def getOVO():
	OVOdiscords = []
	userlist = useraccounts['users']
	OVOdiscords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['OVO'] != None and item['OVO'] != "":
			OVOdiscords.append(item['OVO'])
	return OVOdiscords

def getTscott():
	Tscottdiscords = []
	userlist = useraccounts['users']
	Tscottdiscords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['Travis Scott'] != None and item['Travis Scott'] != "":
			Tscottdiscords.append(item['Travis Scott'])
	return Tscottdiscords

def getKITH():
	KITHdiscords = []
	userlist = useraccounts['users']
	KITHdiscords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['KITH'] != None and item['KITH'] != "":
			KITHdiscords.append(item['KITH'])
	return KITHdiscords

def getBodega():
	Bodegadiscords = []
	userlist = useraccounts['users']
	Bodegadiscords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['Bodega'] != None and item['Bodega'] != "":
			Bodegadiscords.append(item['Bodega'])
	return Bodegadiscords

def getDSM():
	DSMdiscords = []
	userlist = useraccounts['users']
	DSMdiscords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['Dover Street'] != None and item['Dover Street'] != "":
			DSMdiscords.append(item['Dover Street'])
	return DSMdiscords

def getCPlant():
	CPlantdiscords = []
	userlist = useraccounts['users']
	CPlantdiscords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['Cactus Plant'] != None and item['Cactus Plant'] != "":
			CPlantdiscords.append(item['Cactus Plant'])
	return CPlantdiscords

def getUndef():
	Undefdiscords = []
	userlist = useraccounts['users']
	Undefdiscords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['Undefeated'] != None and item['Undefeated'] != "":
			Undefdiscords.append(item['Undefeated'])
	return Undefdiscords

def getSk8():
	Sk8discords = []
	userlist = useraccounts['users']
	Sk8discords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['Skate Shops'] != None and item['Skate Shops'] != "":
			Sk8discords.append(item['Skate Shops'])
	return Sk8discords

def getToys():
	Toysdiscords = []
	userlist = useraccounts['users']
	Toysdiscords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['Toy Shops'] != None and item['Toy Shops'] != "":
			Toysdiscords.append(item['Toy Shops'])
	return Toysdiscords

def getTeddyFresh():
	TeddyFreshdiscords = []
	userlist = useraccounts['users']
	TeddyFreshdiscords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['Teddy Fresh'] != None and item['Teddy Fresh'] != "":
			TeddyFreshdiscords.append(item['Teddy Fresh'])
	return TeddyFreshdiscords

def getFMasks():
	FMasksdiscords = []
	userlist = useraccounts['users']
	FMasksdiscords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['Face Masks'] != None and item['Face Masks'] != "":
			FMasksdiscords.append(item['Face Masks'])
	return FMasksdiscords

def getDeals20():
	Deals20discords = []
	userlist = useraccounts['users']
	Deals20discords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['Deals20'] != None and item['Deals20'] != "":
			Deals20discords.append(item['Deals20'])
	return Deals20discords

def getDeals5():
	Deals5discords = []
	userlist = useraccounts['users']
	Deals5discords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['Deals5'] != None and item['Deals5'] != "":
			Deals5discords.append(item['Deals5'])
	return Deals5discords

def getDealsFree():
	DealsFreediscords = []
	userlist = useraccounts['users']
	DealsFreediscords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['DealsFree'] != None and item['DealsFree'] != "":
			DealsFreediscords.append(item['DealsFree'])
	return DealsFreediscords

#-------------------------------------------------------------------------------------

def Main(url):
	try:
		proxies = getProxies()
	except:
		print("no proxy 4 u")
	#print("Proxies loaded.")
	sleep(10)
	useragents = getUserAgents()

	NewUnfCords = getNewUnf()
	PubUnfCords = getPubUnf()
	UpdUnfCords = getUpdUnf()
	JayNiCords = getJayNi()
	YzyCords = getYzy()
	AdisCords = getAdis()
	ConsCords = getCons()
	VansCords = getVans()
	OVOCords = getOVO()
	TScottCords = getTscott()
	KithCords = getKITH()
	BodegaCords = getBodega()
	TFreshCords = getTeddyFresh()
	DSMCords = getDSM()
	CPlantCords = getCPlant()
	UndefCords = getUndef()
	Sk8Cords = getSk8()
	ToysCords = getToys()
	FMasks = getFMasks()
	D20Cords = getDeals20()
	D5Cords = getDeals5()
	DFreeCords = getDealsFree()

	webpage = ""

	products = []

	NowTime = datetime.now().astimezone().replace(microsecond=0)

	while True:
		#Make Garbage Collection Happy
		getMeta = None
		handle = None
		headers = {}
		headhost = None
		hook = None
		image = None
		link = None
		mdata = None
		meta = []
		metadata = None
		name = None
		nameparse = []
		negkeywords = {}
		poskeywords = {}
		price = None
		productCTime = None
		productName = None
		products = []
		productsCreatedTime = None
		productsUpdatedTime = None
		productUTime = None
		proxies = []
		proxy = None
		proxy_dict = {}
		sizes_list = {}
		stockQTY = None
		storename = None
		useragent = None
		variantID = None
		variants = []
		webpage = None
		x = None

		NewUnfCords = getNewUnf()
		PubUnfCords = getPubUnf()
		UpdUnfCords = getUpdUnf()
		JayNiCords = getJayNi()
		YzyCords = getYzy()
		AdisCords = getAdis()
		ConsCords = getCons()
		VansCords = getVans()
		OVOCords = getOVO()
		TScottCords = getTscott()
		KithCords = getKITH()
		BodegaCords = getBodega()
		TFreshCords = getTeddyFresh()
		DSMCords = getDSM()
		CPlantCords = getCPlant()
		UndefCords = getUndef()
		Sk8Cords = getSk8()
		ToysCords = getToys()
		FMasks = getFMasks()
		D20Cords = getDeals20()
		D5Cords = getDeals5()
		DFreeCords = getDealsFree()
		
		try:
			proxies = getProxies()
			x = random.randint(0, (len(proxies) - 1))
			proxy = proxies[x]
			proxy_dict = {'https': ('socks5://{}'.format(proxy))}
		except:
			sleep(20)
			print("no proxies loaded.")
			pass
		
		try:
			x = random.randint(0, (len(useragents) - 1))
			useragent = useragents[x]
		except:
			print('no user agents')
		
		if len(proxies) > 0:
			try:
				products.clear()
				url_1 = (url + '/products.json')
				headhost = re.split('[/]', url_1)
				headers = {
					"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
					"Accept-Encoding": "gzip, deflate, br",
					"Accept-Language": "en-US,en;q=0.5",
					"Connection": "keep-alive",
					"Host" : headhost[2],
					"TE" : "Trailers",
					"Upgrade-Insecure-Requests": "1", 
					"User-Agent": useragent
					}
				webpage = requests.get(url_1, headers=headers, proxies=proxy_dict, timeout=(35))
				products = json.loads((webpage.text))['products']

			except:
				sleep(5)	

			if products != []:				
				try:
					storename = re.split(r'\.', headhost[2])
					for product in products:
						variants = product['variants']
						for x in range(len(variants)):				
							productsCreatedTime = (variants[x]['created_at'])
							productsUpdatedTime = (variants[x]['updated_at'])

							productCTime = datetime.fromisoformat(productsCreatedTime)
							productUTime = datetime.fromisoformat(productsUpdatedTime)

							#Prep Discord variables
							productName = (product['title'])
							handle = (product['handle'])
							variantID = variants[x]['id']
							stockQTY = 0

							# Check for New Items
							if productCTime > NowTime:
								link = (str(url) + '/products/{}'.format(handle))

								try:
									metadata = link + "/meta.json"

									getMeta = requests.get(metadata, headers=headers, proxies=proxy_dict, timeout=(35))
									meta = json.loads((getMeta.text))['product']['variants']

									for mdata in meta:
										if mdata['id'] == variantID:
											stockQTY = (mdata['inventory_quantity'])
								except:
									stockQTY = 0

								#Create discord message
								##############################################################################

								handle = product['handle']
								link = (str(url) + '/products/{}'.format(handle))	
								# Product name
								name = product['title']
								# Grabs product image URL
								image = product['images']
								try:
									image = image[0]['src']
								except:
									image = ('https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/300px-No_image_available.svg.png')

								# Grabs ATC Links
								sizes_list = ('Size {}: '.format(variants[x]['title']) + str(url) + '/cart/{}:1'.format(variants[x]['id']))
								# Grabs product price
								price = variants[x]['price']

								# Payload message sent to discord webhook.					
								embed = Embed(description=name, timestamp='now', color=0x11b668)
								image1 = (image)
								
								embed.set_author(name=storename[1].upper())
								embed.add_field(name='Status', value='NEW')
								embed.add_field(name='Name', value=name)
								embed.add_field(name='Price', value=str(price))
								embed.add_field(name='Product Page', value=link)
								if stockQTY > 0:
									embed.add_field(name='Available QTY:', value=str(stockQTY))
								embed.add_field(name='One-Click Links', value=str(sizes_list))
								embed.set_footer(text='vMonitors Shopify')
								embed.set_thumbnail(image1)
								try:
									
									#--------------------------------------------------------------------------------------------------------------------------------

									# Cut that name up for filtration
									nameparse = re.split(" |-|/", name.lower())

									# Check for Jawns
									poskeywords = {'space hippie', '270', 'off-white', 'max', 'react', 'presto', 'nike', 'overreact', 'jordan', 'force', 'the ten', 'air', 'the 10', 'flyknit', 'dunk'}
									negkeywords = {'deck', 'tights', 'polo', 'snapback', 'backpack', 'pant', 'legging', 'leggings', 'dress', 'legasee', 'shorts', 'windrunner', 'windbreaker', 'jacket', 'vest ', 'asic', 'pants', 'sweater', 'head band', 'poster', 'screenprinted', 'adidas', 'tank', 'sweatpants', 'keychain', 'shirt', 'socks', 'tee', 'yeezy', 'hat', 'headband', 'yoga', 'pullover', 'bra', 'collectable', 'hoodie', 'yzy'}

									if poskeywords & set(nameparse) and stockQTY > 0:
										if negkeywords & set(nameparse):
											pass
										else:
											for jnc in range(len(JayNiCords)):
												try:
													hook = Webhook(JayNiCords[jnc])
													#													hook.send(embed=embed)
												except:
													hook2pre = re.split(r"discordapp.com", JayNiCords[jnc])
													hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
													hook2.send(embed=embed)

									# Check for Yzy
									poskeywords = {'yzy', 'yeezy', 'yeezus', 'yeez'}
									negkeywords = {'deck', 'tights', 'polo', 'snapback', 'backpack', 'pant', 'legging', 'leggings', 'dress', 'legasee', 'shorts', 'windrunner', 'windbreaker', 'jacket', 'vest ', 'keychain', 'nike', 'shirt', 'converse', 'sweatpants', 'bra', 'collectable', 'head band', 'taylor', 'hat', 'yoga', 'screenprinted', 'pants', 'tee', 'headband', 'chuck', 'sweater', 'asic', 'adidas', 'socks', 'tank', 'hoodie', 'pullover', 'poster'}

									if poskeywords & set(nameparse) and stockQTY > 0:
										if negkeywords & set(nameparse):
											pass
										else:
											for yzc in range(len(YzyCords)):
												try:
													hook = Webhook(YzyCords[yzc])
													hook.send(embed=embed)
												except:
													hook2pre = re.split(r"discordapp.com", YzyCords[yzc])
													hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
													hook2.send(embed=embed)

									# Check for Adi
									poskeywords = {'nizza', 'originals', 'nmd', 'adidas', 'r1', 'adilette', 'sobakov', 'ultraboost'}
									negkeywords = {'deck', 'tights', 'polo', 'snapback', 'backpack', 'pant', 'legging', 'leggings', 'dress', 'legasee', 'shorts', 'windrunner', 'windbreaker', 'jacket', 'vest ', 'chuck', 'nike', 'head band', 'sweatpants', 'asic', 'keychain', 'yzy', 'taylor', 'sweater', 'pullover', 'hoodie', 'converse', 'shirt', 'screenprinted', 'poster', 'socks', 'tee', 'collectable', 'yeezy', 'tank', 'pants', 'headband', 'hat', 'yoga', 'bra'}

									if poskeywords & set(nameparse) and stockQTY > 0:
										if negkeywords & set(nameparse):
											pass
										else:
											for adic in range(len(AdisCords)):
												try:
													hook = Webhook(AdisCords[adic])
													hook.send(embed=embed)
												except:
													hook2pre = re.split(r"discordapp.com", AdisCords[adic])
													hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
													hook2.send(embed=embed)

									# Check for Cons
									poskeywords = {'taylor', 'chuck', '70', 'all-star', 'all star', 'converse'}
									negkeywords = {'deck', 'tights', 'polo', 'snapback', 'backpack', 'pant', 'legging', 'leggings', 'dress', 'legasee', 'shorts', 'windrunner', 'windbreaker', 'jacket', 'vest ', 'sweater', 'head band', 'collectable', 'headband', 'keychain', 'pullover', 'asic', 'tank', 'hoodie', 'sweatpants', 'poster', 'yzy', 'yoga', 'tee', 'socks', 'yeezy', 'adidas', 'bra', 'screenprinted', 'hat', 'pants', 'shirt'}

									if poskeywords & set(nameparse) and stockQTY > 0:
										if negkeywords & set(nameparse):
											pass
										else:
											for conc in range(len(ConsCords)):
												try:
													hook = Webhook(ConsCords[conc])
													hook.send(embed=embed)
												except:
													hook2pre = re.split(r"discordapp.com", ConsCords[conc])
													hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
													hook2.send(embed=embed)

									# Check for Vans
									poskeywords = {'vans'}
									negkeywords = {'deck', 'tights', 'polo', 'snapback', 'backpack', 'pant', 'legging', 'leggings', 'dress', 'legasee', 'shorts', 'windrunner', 'windbreaker', 'jacket', 'vest ', 'sweater', 'head band', 'collectable', 'headband', 'keychain', 'pullover', 'asic', 'tank', 'hoodie', 'sweatpants', 'poster', 'yzy', 'yoga', 'tee', 'socks', 'yeezy', 'adidas', 'bra', 'screenprinted', 'hat', 'pants', 'shirt'}

									if poskeywords & set(nameparse) and stockQTY > 0:
										if negkeywords & set(nameparse):
											pass
										else:
											for vanc in range(len(VansCords)):
												try:
													hook = Webhook(VansCords[vanc])
													hook.send(embed=embed)
												except:
													hook2pre = re.split(r"discordapp.com", VansCords[vanc])
													hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
													hook2.send(embed=embed)
									
									# Check for FaceMasks
									poskeywords = {'facemask', 'mask', 'masque'}
									negkeywords = {'deck', 'tights', 'polo', 'snapback', 'backpack', 'pant', 'legging', 'leggings', 'dress', 'legasee', 'shorts', 'windrunner', 'windbreaker', 'jacket', 'vest ', 'sweater', 'head band', 'headband', 'keychain', 'pullover', 'asic', 'tank', 'hoodie', 'sweatpants', 'poster', 'yzy', 'yoga', 'tee', 'socks', 'yeezy', 'adidas', 'bra', 'screenprinted', 'hat', 'pants', 'shirt'}

									if poskeywords & set(nameparse) and stockQTY > 0:
										if negkeywords & set(nameparse):
											pass
										else:
											for fmc in range(len(FMasks)):
												try:
													hook = Webhook(FMasks[fmc])
													hook.send(embed=embed)
												except:
													hook2pre = re.split(r"discordapp.com", FMasks[fmc])
													hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
													hook2.send(embed=embed)
									
									# Check for OVO
									poskeywords = {'octobersveryown'}									
									if poskeywords & set(storename) and stockQTY > 0:
										for ovoc in range(len(OVOCords)):
											try:
												hook = Webhook(OVOCords[ovoc])
												hook.send(embed=embed)
											except:
												hook2pre = re.split(r"discordapp.com", OVOCords[ovoc])
												hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
												hook2.send(embed=embed)
									

									# Check for Travis Scott
									poskeywords = {'travisscott'}
									if poskeywords & set(storename) and stockQTY > 0:
										for tsc in range(len(TScottCords)):
											try:
												hook = Webhook(TScottCords[tsc])
												hook.send(embed=embed)
											except:
												hook2pre = re.split(r"discordapp.com", TScottCords[tsc])
												hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
												hook2.send(embed=embed)
									

									# Check for KITH
									poskeywords = {'kith'}
									if poskeywords & set(storename) and stockQTY > 0:
										for kc in range(len(KithCords)):
											try:
												hook = Webhook(KithCords[kc])
												hook.send(embed=embed)
											except:
												hook2pre = re.split(r"discordapp.com", KithCords[kc])
												hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
												hook2.send(embed=embed)
									

									# Check for Bodega
									poskeywords = {'Bodega','bdga','bdgastore'}
									if poskeywords & set(storename) and stockQTY > 0:
										for pc in range(len(BodegaCords)):
											try:
												hook = Webhook(BodegaCords[pc])
												hook.send(embed=embed)
											except:
												hook2pre = re.split(r"discordapp.com", BodegaCords[pc])
												hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
												hook2.send(embed=embed)
									

									# Check for Dover Street
									poskeywords = {'doverstreetmarket','eflash','eflash-jp','eflash-sg','eflash-us'}
									if poskeywords & set(storename) and stockQTY > 0:
										for dsmc in range(len(DSMCords)):
											try:
												hook = Webhook(DSMCords[dsmc])
												hook.send(embed=embed)
											except:
												hook2pre = re.split(r"discordapp.com", DSMCords[dsmc])
												hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
												hook2.send(embed=embed)
									

									# Check for Cactus Plant
									poskeywords = {'cactusplantfleamarket'}
									if poskeywords & set(storename) and stockQTY > 0:
										for cpfc in range(len(CPlantCords)):
											try:
												hook = Webhook(CPlantCords[cpfc])
												hook.send(embed=embed)
											except:
												hook2pre = re.split(r"discordapp.com", CPlantCords[cpfc])
												hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
												hook2.send(embed=embed)
									

									# Check for Undefeated
									poskeywords = {'undefeated'}
									if poskeywords & set(storename) and stockQTY > 0:
										for undec in range(len(UndefCords)):
											try:
												hook = Webhook(UndefCords[undec])
												hook.send(embed=embed)
											except:
												hook2pre = re.split(r"discordapp.com", UndefCords[undec])
												hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
												hook2.send(embed=embed)
									
									# Check for Teddy Fresh
									poskeywords = {'teddyfresh'}
									if poskeywords & set(storename) and stockQTY > 0:
										for tfc in range(len(TFreshCords)):
											try:
												hook = Webhook(TFreshCords[tfc])
												hook.send(embed=embed)
											except:
												hook2pre = re.split(r"discordapp.com", TFreshCords[tfc])
												hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
												hook2.send(embed=embed)

									# Check for Skate Shops
									poskeywords = {'35thnorth', '5050store', 'amigoskateshop', 'atlasskateboarding', 'blacksheepskateshop', 'boredofsouthsea', 'theberrics', 'empireskateshop', 'fuckingawesomestore', 'galacticg', 'garageskateshop', 'hemleyskateboarding', 'homebase610', 'kineticskateboarding', 'orchardshop', 'Bodegaskateboards', 'plusskateshop', 'slamcity', 'strangeloveskateboards', 'urbanaveboardshop', 'welcomeleeds'}
									if poskeywords & set(storename) and stockQTY > 0:
										for skac in range(len(Sk8Cords)):
											try:
												hook = Webhook(Sk8Cords[skac])
												hook.send(embed=embed)
											except:
												hook2pre = re.split(r"discordapp.com", Sk8Cords[skac])
												hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
												hook2.send(embed=embed)
									

									# Check for Toy Shops
									poskeywords = {'bimtoy', 'bottleneckgallery', 'chronotoys', 'ferraramarketinc', 'figpin', 'fugitivetoys', 'galactictoys', 'kawsone', 'kidrobot', 'toytokyo', 'mondoshop', 'laika', 'thenecastore', 'toydrops'}
									if poskeywords & set(storename) and stockQTY > 0:
										for toyc in range(len(ToysCords)):
											try:
												hook = Webhook(ToysCords[toyc])
												hook.send(embed=embed)
											except:
												hook2pre = re.split(r"discordapp.com", ToysCords[toyc])
												hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
												hook2.send(embed=embed)
									
									#--------------------------------------------------------------------------------------------------------------------------------

									#Send to Deals
									intPrice = round(float(price))

									if intPrice < 21 and intPrice > 5 and stockQTY > 0:
										for d20 in range(len(D20Cords)):
											try:
												hook = Webhook(D20Cords[d20])
												hook.send(embed=embed)
											except:
												hook2pre = re.split(r"discordapp.com", D20Cords[d20])
												hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
												hook2.send(embed=embed)

									if intPrice < 6 and intPrice > 0 and stockQTY > 0:
										for d5 in range(len(D5Cords)):
											try:
												hook = Webhook(D5Cords[d5])
												hook.send(embed=embed)
											except:
												hook2pre = re.split(r"discordapp.com", D5Cords[d5])
												hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
												hook2.send(embed=embed)

									if intPrice < 1 and stockQTY > 0:
										for df0 in range(len(DFreeCords)):
											try:
												hook = Webhook(DFreeCords[df0])
												hook.send(embed=embed)
											except:
												hook2pre = re.split(r"discordapp.com", DFreeCords[df0])
												hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
												hook2.send(embed=embed)

									#--------------------------------------------------------------------------------------------------------------------------------

									for nuc in range(len(NewUnfCords)):
										try:
											hook = Webhook(NewUnfCords[nuc])
											
											hook.send(embed=embed)
										except:
											hook2pre = re.split(r"discordapp.com", NewUnfCords[nuc])
											hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
											
											hook2.send(embed=embed)

								except Exception as e:
									print("Failure at New Send")
									print(e)
									pass

								##############################################################################

							if productUTime > NowTime:
								link = (str(url) + '/products/{}'.format(handle))

								try:
									metadata = link + "/meta.json"

									getMeta = requests.get(metadata, headers=headers, proxies=proxy_dict, timeout=(35))
									meta = json.loads((getMeta.text))['product']['variants']

									for mdata in meta:
										if mdata['id'] == variantID:
											stockQTY = (mdata['inventory_quantity'])
								except:
									stockQTY = 0

								#Create discord message
								##############################################################################

								handle = product['handle']
								link = (str(url) + '/products/{}'.format(handle))	
								# Product name
								name = product['title']
								# Grabs product image URL
								image = product['images']
								try:
									image = image[0]['src']
								except:
									image = ('https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/300px-No_image_available.svg.png')

								# Grabs ATC Links
								sizes_list = ('Size {}: '.format(variants[x]['title']) + str(url) + '/cart/{}:1'.format(variants[x]['id']))
								# Grabs product price
								price = variants[x]['price']

								# Payload message sent to discord webhook.
								embed = Embed(description=name, timestamp='now', color=0x11b668)
								image1 = (image)
								
								embed.set_author(name=storename[1].upper())
								embed.add_field(name='Status', value='UPDATED')
								embed.add_field(name='Name', value=name)
								embed.add_field(name='Price', value=str(price))
								embed.add_field(name='Product Page', value=link)
								if stockQTY > 0:
									embed.add_field(name='Available QTY:', value=str(stockQTY))
								embed.add_field(name='One-Click Links', value=str(sizes_list))
								embed.set_footer(text='vMonitors Shopify')
								embed.set_thumbnail(image1)
								try:
									
									#--------------------------------------------------------------------------------------------------------------------------------

									# Cut that name up for filtration
									nameparse = re.split(" |-|/", name.lower())

									# Check for Jawns
									poskeywords = {'space hippie', '270', 'off-white', 'max', 'react', 'presto', 'nike', 'overreact', 'jordan', 'force', 'the ten', 'air', 'the 10', 'flyknit', 'dunk'}
									negkeywords = {'deck', 'tights', 'polo', 'snapback', 'backpack', 'pant', 'legging', 'leggings', 'dress', 'legasee', 'shorts', 'windrunner', 'windbreaker', 'jacket', 'vest ', 'asic', 'pants', 'sweater', 'head band', 'poster', 'screenprinted', 'adidas', 'tank', 'sweatpants', 'keychain', 'shirt', 'socks', 'tee', 'yeezy', 'hat', 'headband', 'yoga', 'pullover', 'bra', 'collectable', 'hoodie', 'yzy'}

									if poskeywords & set(nameparse) and stockQTY > 0:
										if negkeywords & set(nameparse):
											pass
										else:
											for jnc in range(len(JayNiCords)):
												try:
													hook = Webhook(JayNiCords[jnc])hook.send(embed=embed)
												except:
													hook2pre = re.split(r"discordapp.com", JayNiCords[jnc])
													hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))hook2.send(embed=embed)

									# Check for Yzy
									poskeywords = {'yzy', 'yeezy', 'yeezus', 'yeez'}
									negkeywords = {'deck', 'tights', 'polo', 'snapback', 'backpack', 'pant', 'legging', 'leggings', 'dress', 'legasee', 'shorts', 'windrunner', 'windbreaker', 'jacket', 'vest ', 'keychain', 'nike', 'shirt', 'converse', 'sweatpants', 'bra', 'collectable', 'head band', 'taylor', 'hat', 'yoga', 'screenprinted', 'pants', 'tee', 'headband', 'chuck', 'sweater', 'asic', 'adidas', 'socks', 'tank', 'hoodie', 'pullover', 'poster'}

									if poskeywords & set(nameparse) and stockQTY > 0:
										if negkeywords & set(nameparse):
											pass
										else:
											for yzc in range(len(YzyCords)):
												try:
													hook = Webhook(YzyCords[yzc])
													hook.send(embed=embed)
												except:
													hook2pre = re.split(r"discordapp.com", YzyCords[yzc])
													hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
													hook2.send(embed=embed)

									# Check for Adi
									poskeywords = {'nizza', 'originals', 'nmd', 'adidas', 'r1', 'adilette', 'sobakov', 'ultraboost'}
									negkeywords = {'deck', 'tights', 'polo', 'snapback', 'backpack', 'pant', 'legging', 'leggings', 'dress', 'legasee', 'shorts', 'windrunner', 'windbreaker', 'jacket', 'vest ', 'chuck', 'nike', 'head band', 'sweatpants', 'asic', 'keychain', 'yzy', 'taylor', 'sweater', 'pullover', 'hoodie', 'converse', 'shirt', 'screenprinted', 'poster', 'socks', 'tee', 'collectable', 'yeezy', 'tank', 'pants', 'headband', 'hat', 'yoga', 'bra'}

									if poskeywords & set(nameparse) and stockQTY > 0:
										if negkeywords & set(nameparse):
											pass
										else:
											for adic in range(len(AdisCords)):
												try:
													hook = Webhook(AdisCords[adic])
													hook.send(embed=embed)
												except:
													hook2pre = re.split(r"discordapp.com", AdisCords[adic])
													hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
													hook2.send(embed=embed)

									# Check for Cons
									poskeywords = {'taylor', 'chuck', '70', 'all-star', 'all star', 'converse'}
									negkeywords = {'deck', 'tights', 'polo', 'snapback', 'backpack', 'pant', 'legging', 'leggings', 'dress', 'legasee', 'shorts', 'windrunner', 'windbreaker', 'jacket', 'vest ', 'sweater', 'head band', 'collectable', 'headband', 'keychain', 'pullover', 'asic', 'tank', 'hoodie', 'sweatpants', 'poster', 'yzy', 'yoga', 'tee', 'socks', 'yeezy', 'adidas', 'bra', 'screenprinted', 'hat', 'pants', 'shirt'}

									if poskeywords & set(nameparse) and stockQTY > 0:
										if negkeywords & set(nameparse):
											pass
										else:
											for conc in range(len(ConsCords)):
												try:
													hook = Webhook(ConsCords[conc])
													hook.send(embed=embed)
												except:
													hook2pre = re.split(r"discordapp.com", ConsCords[conc])
													hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
													hook2.send(embed=embed)

									# Check for Vans
									poskeywords = {'vans'}
									negkeywords = {'deck', 'tights', 'polo', 'snapback', 'backpack', 'pant', 'legging', 'leggings', 'dress', 'legasee', 'shorts', 'windrunner', 'windbreaker', 'jacket', 'vest ', 'sweater', 'head band', 'collectable', 'headband', 'keychain', 'pullover', 'asic', 'tank', 'hoodie', 'sweatpants', 'poster', 'yzy', 'yoga', 'tee', 'socks', 'yeezy', 'adidas', 'bra', 'screenprinted', 'hat', 'pants', 'shirt'}

									if poskeywords & set(nameparse) and stockQTY > 0:
										if negkeywords & set(nameparse):
											pass
										else:
											for vanc in range(len(VansCords)):
												try:
													hook = Webhook(VansCords[vanc])
													hook.send(embed=embed)
												except:
													hook2pre = re.split(r"discordapp.com", VansCords[vanc])
													hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
													hook2.send(embed=embed)
									
									# Check for FaceMasks
									poskeywords = {'facemask', 'mask', 'masque'}
									negkeywords = {'deck', 'tights', 'polo', 'snapback', 'backpack', 'pant', 'legging', 'leggings', 'dress', 'legasee', 'shorts', 'windrunner', 'windbreaker', 'jacket', 'vest ', 'sweater', 'head band', 'headband', 'keychain', 'pullover', 'asic', 'tank', 'hoodie', 'sweatpants', 'poster', 'yzy', 'yoga', 'tee', 'socks', 'yeezy', 'adidas', 'bra', 'screenprinted', 'hat', 'pants', 'shirt'}

									if poskeywords & set(nameparse) and stockQTY > 0:
										if negkeywords & set(nameparse):
											pass
										else:
											for fmc in range(len(FMasks)):
												try:
													hook = Webhook(FMasks[fmc])
													hook.send(embed=embed)
												except:
													hook2pre = re.split(r"discordapp.com", FMasks[fmc])
													hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
													hook2.send(embed=embed)
									
									# Check for OVO
									poskeywords = {'octobersveryown'}									
									if poskeywords & set(storename):
										for ovoc in range(len(OVOCords)):
											try:
												hook = Webhook(OVOCords[ovoc])
												hook.send(embed=embed)
											except:
												hook2pre = re.split(r"discordapp.com", OVOCords[ovoc])
												hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
												hook2.send(embed=embed)
									

									# Check for Travis Scott
									poskeywords = {'travisscott'}
									if poskeywords & set(storename):
										for tsc in range(len(TScottCords)):
											try:
												hook = Webhook(TScottCords[tsc])
												hook.send(embed=embed)
											except:
												hook2pre = re.split(r"discordapp.com", TScottCords[tsc])
												hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
												hook2.send(embed=embed)
									

									# Check for KITH
									poskeywords = {'kith'}
									if poskeywords & set(storename):
										for kc in range(len(KithCords)):
											try:
												hook = Webhook(KithCords[kc])
												hook.send(embed=embed)
											except:
												hook2pre = re.split(r"discordapp.com", KithCords[kc])
												hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
												hook2.send(embed=embed)
									

									# Check for Bodega
									poskeywords = {'Bodega','bdga','bdgastore'}
									if poskeywords & set(storename):
										for pc in range(len(BodegaCords)):
											try:
												hook = Webhook(BodegaCords[pc])
												hook.send(embed=embed)
											except:
												hook2pre = re.split(r"discordapp.com", BodegaCords[pc])
												hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
												hook2.send(embed=embed)
									

									# Check for Dover Street
									poskeywords = {'doverstreetmarket','eflash','eflash-jp','eflash-sg','eflash-us'}
									if poskeywords & set(storename):
										for dsmc in range(len(DSMCords)):
											try:
												hook = Webhook(DSMCords[dsmc])
												hook.send(embed=embed)
											except:
												hook2pre = re.split(r"discordapp.com", DSMCords[dsmc])
												hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
												hook2.send(embed=embed)
									

									# Check for Cactus Plant
									poskeywords = {'cactusplantfleamarket'}
									if poskeywords & set(storename):
										for cpfc in range(len(CPlantCords)):
											try:
												hook = Webhook(CPlantCords[cpfc])
												hook.send(embed=embed)
											except:
												hook2pre = re.split(r"discordapp.com", CPlantCords[cpfc])
												hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
												hook2.send(embed=embed)
									

									# Check for Undefeated
									poskeywords = {'undefeated'}
									if poskeywords & set(storename):
										for undec in range(len(UndefCords)):
											try:
												hook = Webhook(UndefCords[undec])
												hook.send(embed=embed)
											except:
												hook2pre = re.split(r"discordapp.com", UndefCords[undec])
												hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
												hook2.send(embed=embed)
									
									# Check for Teddy Fresh
									poskeywords = {'teddyfresh'}
									if poskeywords & set(storename) and stockQTY > 0:
										for tfc in range(len(TFreshCords)):
											try:
												hook = Webhook(TFreshCords[tfc])
												hook.send(embed=embed)
											except:
												hook2pre = re.split(r"discordapp.com", TFreshCords[tfc])
												hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
												hook2.send(embed=embed)

									# Check for Skate Shops
									poskeywords = {'35thnorth', '5050store', 'amigoskateshop', 'atlasskateboarding', 'blacksheepskateshop', 'boredofsouthsea', 'theberrics', 'empireskateshop', 'fuckingawesomestore', 'galacticg', 'garageskateshop', 'hemleyskateboarding', 'homebase610', 'kineticskateboarding', 'orchardshop', 'Bodegaskateboards', 'plusskateshop', 'slamcity', 'strangeloveskateboards', 'urbanaveboardshop', 'welcomeleeds'}
									if poskeywords & set(storename) and stockQTY > 0:
										for skac in range(len(Sk8Cords)):
											try:
												hook = Webhook(Sk8Cords[skac])
												hook.send(embed=embed)
											except:
												hook2pre = re.split(r"discordapp.com", Sk8Cords[skac])
												hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
												hook2.send(embed=embed)
									

									# Check for Toy Shops
									poskeywords = {'bimtoy', 'bottleneckgallery', 'chronotoys', 'ferraramarketinc', 'figpin', 'fugitivetoys', 'galactictoys', 'kawsone', 'kidrobot', 'toytokyo', 'mondoshop', 'laika', 'thenecastore', 'toydrops'}
									if poskeywords & set(storename) and stockQTY > 0:
										for toyc in range(len(ToysCords)):
											try:
												hook = Webhook(ToysCords[toyc])
												hook.send(embed=embed)
											except:
												hook2pre = re.split(r"discordapp.com", ToysCords[toyc])
												hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
												hook2.send(embed=embed)
									

									#--------------------------------------------------------------------------------------------------------------------------------

									#Send to Deals
									intPrice = round(float(price))

									if intPrice < 21 and intPrice > 5 and stockQTY > 0:
										for d20 in range(len(D20Cords)):
											try:
												hook = Webhook(D20Cords[d20])
												hook.send(embed=embed)
											except:
												hook2pre = re.split(r"discordapp.com", D20Cords[d20])
												hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
												hook2.send(embed=embed)

									if intPrice < 6 and intPrice > 0 and stockQTY > 0:
										for d5 in range(len(D5Cords)):
											try:
												hook = Webhook(D5Cords[d5])
												hook.send(embed=embed)
											except:
												hook2pre = re.split(r"discordapp.com", D5Cords[d5])
												hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
												hook2.send(embed=embed)

									if intPrice < 1 and stockQTY > 0:
										for df0 in range(len(DFreeCords)):
											try:
												hook = Webhook(DFreeCords[df0])
												hook.send(embed=embed)
											except:
												hook2pre = re.split(r"discordapp.com", DFreeCords[df0])
												hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
												hook2.send(embed=embed)

									#--------------------------------------------------------------------------------------------------------------------------------

									# Send to Unfiltered
									for uuc in range(len(UpdUnfCords)):
										try:
											hook = Webhook(UpdUnfCords[uuc])
											
											hook.send(embed=embed)
										except:
											hook2pre = re.split(r"discordapp.com", UpdUnfCords[uuc])
											hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
											
											hook2.send(embed=embed)
								except:
									print("Failure at Update Send")
									pass	
								##############################################################################
				except Exception as e:
					print(e)
					pass
				
				# CLEAN UP
				products.clear()
				del AdisCords
				del BodegaCords
				del ConsCords
				del CPlantCords
				del DSMCords
				del FMasks
				del D20Cords
				del D5Cords
				del DFreeCords
				del getMeta
				del handle
				del headers
				del headhost
				del hook
				del image
				del JayNiCords
				del KithCords
				del link
				del meta
				del metadata
				del name
				del nameparse
				del negkeywords
				del NewUnfCords
				del OVOCords
				del poskeywords
				del price
				del productCTime
				del productName
				del products
				del productsCreatedTime
				del productsUpdatedTime
				del productUTime
				del proxies
				del proxy
				del proxy_dict
				del PubUnfCords
				del sizes_list
				del Sk8Cords
				del stockQTY
				del storename
				del ToysCords
				del TScottCords
				del UndefCords
				del UpdUnfCords
				del useragent
				del VansCords
				del variantID
				del variants
				del webpage
				del x
				del YzyCords
				del TFreshCords
				gc.collect()

				NowTime = datetime.now().astimezone().replace(microsecond=0)				
				sleep(random.randint(35,75))

urls = []
shopify_links = open('shops.txt', 'r')
for slinks in shopify_links:
	slinks = slinks.strip('\n')
	urls.append(slinks)

shopify_links.close()

print("Prep Start")

sleep(5)

proxy_threads = threading.Thread(target=getProxies, name='getProxy Thread {}'.format(0))
useragent_threads = threading.Thread(target=getUserAgents, name='getUserAgents Thread {}'.format(0))

print("Firing Cannons")

for x in range(len(urls)):
	main_threads = threading.Thread(target=Main, name='Main Thread {}'.format(x), args= (urls[x],))
	main_threads.start()	
	#print('{} initialized'.format(main_threads.name))

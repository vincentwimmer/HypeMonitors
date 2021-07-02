import re
import json
import time
import random
from datetime import datetime
from datetime import timedelta
import requests
import threading
from dhooks import Webhook, Embed

delay = '90'
dCordLogWebhook = "Webhook URL"

getuserjsonfile = '/Database/vmonitorsSNKRSUsers.json'
with open(getuserjsonfile) as useraccountsf:
	useraccounts = json.load(useraccountsf)

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

def getDsnkrsUS():
	DsnkrsUSCords = []
	userlist = useraccounts['users']
	DsnkrsUSCords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['SNKRS US'] != None:
			DsnkrsUSCords.append(item['SNKRS US'])
	return DsnkrsUSCords

def getDsnkrsCAN():
	DsnkrsCANCords = []
	userlist = useraccounts['users']
	DsnkrsCANCords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['SNKRS CAN'] != None:
			DsnkrsCANCords.append(item['SNKRS CAN'])
	return DsnkrsCANCords

def getDsnkrsUK():
	DsnkrsUKCords = []
	userlist = useraccounts['users']
	DsnkrsUKCords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['SNKRS UK'] != None:
			DsnkrsUKCords.append(item['SNKRS UK'])
	return DsnkrsUKCords

def getDsnkrsGER():
	DsnkrsGERCords = []
	userlist = useraccounts['users']
	DsnkrsGERCords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['SNKRS GER'] != None:
			DsnkrsGERCords.append(item['SNKRS GER'])
	return DsnkrsGERCords

def getDsnkrsFR():
	DsnkrsFRCords = []
	userlist = useraccounts['users']
	DsnkrsFRCords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['SNKRS FR'] != None:
			DsnkrsFRCords.append(item['SNKRS FR'])
	return DsnkrsFRCords

def getDsnkrsRU():
	DsnkrsRUCords = []
	userlist = useraccounts['users']
	DsnkrsRUCords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['SNKRS RU'] != None:
			DsnkrsRUCords.append(item['SNKRS RU'])
	return DsnkrsRUCords

def getDsnkrsUAE():
	DsnkrsUAECords = []
	userlist = useraccounts['users']
	DsnkrsUAECords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['SNKRS UAE'] != None:
			DsnkrsUAECords.append(item['SNKRS UAE'])
	return DsnkrsUAECords

def getDsnkrsJP():
	DsnkrsJPCords = []
	userlist = useraccounts['users']
	DsnkrsJPCords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['SNKRS JP'] != None:
			DsnkrsJPCords.append(item['SNKRS JP'])
	return DsnkrsJPCords

def getDsnkrsCN():
	DsnkrsCNCords = []
	userlist = useraccounts['users']
	DsnkrsCNCords.clear()
	for item in userlist:
		if item['Status'] == "Active" and item['SNKRS CN'] != None:
			DsnkrsCNCords.append(item['SNKRS CN'])
	return DsnkrsCNCords

def post_log(message,Name):  
	embed = Embed(title=Name,url='https://www.nike.com/launch/t/', description='', timestamp='now', color=0x11b668)
	embed.add_field(name='Message', value=message)
	embed.set_author(name='vMonitors SNKRS Monitor')
	embed.set_footer(text='vMonitors')
	try:
		hook1 = Webhook(dCordLogWebhook)
		hook1.send(embed=embed)
	except:
		hook2pre = re.split(r"discordapp.com", dCordLogWebhook)
		hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
		hook2.send(embed=embed)

def post_discord(imageSqUrl,imageLsUrl,title,fullTitle,status,styleColor,publishType,exclusiveAccess,hardLaunch,price,launchDate,availability,genders,method,Name,sizes):

	DsnkrsUSCords = getDsnkrsUS()
	DsnkrsCANCords = getDsnkrsCAN()
	DsnkrsUKCords = getDsnkrsUK()
	DsnkrsGERCords = getDsnkrsGER()
	DsnkrsFRCords = getDsnkrsFR()
	DsnkrsRUCords = getDsnkrsRU()
	DsnkrsUAECords = getDsnkrsUAE()
	DsnkrsJPCords = getDsnkrsJP()
	DsnkrsCNCords = getDsnkrsCN()

	if launchDate != "Null":
		launchDateSplit = re.split('z|Z', launchDate)
		launchDateToEST = datetime.fromisoformat(launchDateSplit[0]).replace(microsecond=0) - timedelta(hours=4)
		launchDateUpdated = (str(launchDateToEST) + " EDT")
	else:
		launchDateUpdated = "Not Listed"

	if sizes != ['Null']:
		sizesA = sizes
		sizesB = sizesA[:len(sizesA)//2]
		sizesC = sizesA[len(sizesA)//2:]

	if genders != ['Null']:
		gendersStack = '\n'.join(genders)
	else:
		gendersStack = ['NA']

	info = (f'Style: {styleColor} | Price: {price} \n Type: {publishType} | Hard Launch: {hardLaunch} \n Sizing: \n +{gendersStack}')

	embed = Embed(title=f'{fullTitle}',url='https://www.nike.com/launch/t/'+str(title).lower(), color=0x11b668, description=f' {Name} \n \n Method: {method} \n Avilable: {str(availability)} \n Exclusive: {exclusiveAccess} \n **Info** \n {info}', timestamp='now')
	
	if imageLsUrl != 'Null':
		embed.set_image(imageLsUrl)

	if sizes != ['Null']:
		embed.add_field(name='Stock', value='\n'.join(sizesB))
		embed.add_field(name='.', value='\n'.join(sizesC))

	if launchDate != "Null":
		embed.add_field(name='Launching', value=launchDateUpdated,inline=False)
	embed.set_author(name=Name)

	if imageSqUrl != "Null":
		embed.set_thumbnail(url=imageSqUrl)
	embed.set_footer(text='vMonitors SNKRS')

	try:
		if Name == str('SNKRS US'):
			for sus in range(len(DsnkrsUSCords)):
				try:
					hook = Webhook(DsnkrsUSCords[sus])
					hook.send(embed=embed)
				except:
					hook2pre = re.split(r"discordapp.com", DsnkrsUSCords[sus])
					hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
					hook2.send(embed=embed)

		if Name == str('SNKRS CAN'):
				for scan in range(len(DsnkrsCANCords)):
					try:
						hook = Webhook(DsnkrsUSCords[scan])
						hook.send(embed=embed)
					except:
						hook2pre = re.split(r"discordapp.com", DsnkrsUSCords[scan])
						hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
						hook2.send(embed=embed)

		if Name == str('SNKRS UK'):
				for suk in range(len(DsnkrsUKCords)):
					try:
						hook = Webhook(DsnkrsUKCords[suk])
						hook.send(embed=embed)
					except:
						hook2pre = re.split(r"discordapp.com", DsnkrsUKCords[suk])
						hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
						hook2.send(embed=embed)

		if Name == str('SNKRS GER'):
				for sger in range(len(DsnkrsGERCords)):
					try:
						hook = Webhook(DsnkrsUSCords[sger])
						hook.send(embed=embed)
					except:
						hook2pre = re.split(r"discordapp.com", DsnkrsUSCords[sger])
						hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
						hook2.send(embed=embed)

		if Name == str('SNKRS FR'):
				print("Trying France Send")
				for sfr in range(len(DsnkrsFRCords)):
					try:
						hook = Webhook(DsnkrsFRCords[sfr])
						hook.send(embed=embed)
						print("France Sent")
					except:
						hook2pre = re.split(r"discordapp.com", DsnkrsFRCords[sfr])
						hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
						hook2.send(embed=embed)
						print("France Sent")

		if Name == str('SNKRS RU'):
				for sru in range(len(DsnkrsRUCords)):
					try:
						hook = Webhook(DsnkrsRUCords[sru])
						hook.send(embed=embed)
					except:
						hook2pre = re.split(r"discordapp.com", DsnkrsRUCords[sru])
						hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
						hook2.send(embed=embed)

		if Name == str('SNKRS UAE'):
				for suae in range(len(DsnkrsUAECords)):
					try:
						hook = Webhook(DsnkrsUAECords[suae])
						hook.send(embed=embed)
					except:
						hook2pre = re.split(r"discordapp.com", DsnkrsUAECords[suae])
						hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
						hook2.send(embed=embed)

		if Name == str('SNKRS JP'):
				for sjp in range(len(DsnkrsJPCords)):
					try:
						hook = Webhook(DsnkrsJPCords[sjp])
						hook.send(embed=embed)
					except:
						hook2pre = re.split(r"discordapp.com", DsnkrsJPCords[sjp])
						hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
						hook2.send(embed=embed)

		if Name == str('SNKRS CN'):
				for scn in range(len(DsnkrsCNCords)):
					try:
						hook = Webhook(DsnkrsCNCords[scn])
						hook.send(embed=embed)
					except:
						hook2pre = re.split(r"discordapp.com", DsnkrsCNCords[scn])
						hook2 = Webhook(str(hook2pre[0]+"discord.com"+hook2pre[1]))
						hook2.send(embed=embed)
	except Exception as e:
		post_log(f'**Failure on postDiscord thread {fullTitle}** \n \n {e} ', fullTitle)

def scrpaeSlugs(url):
	useragents = getUserAgents()

	try:

		try:
			x = random.randint(0, (len(useragents) - 1))
			useragent = useragents[x]
		except:
			print('no user agents')

		headers = {
					"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
					"Accept-Encoding": "gzip, deflate, br",
					"Accept-Language": "en-US,en;q=0.5",
					"Connection": "keep-alive",
					"TE" : "Trailers",
					"Upgrade-Insecure-Requests": "1", 
					"User-Agent": useragent
					}

		proxies = getProxies()
		time.sleep(int(10))
		try:
			x = random.randint(0, (len(proxies) - 1))
			proxy = proxies[x]
			proxy_dict = {'https': ('socks5://{}'.format(proxy))}
		except:        
			pass
		
		apiReq = requests.get(url, headers=headers, proxies=proxy_dict, timeout=(60))
		apiObjects = json.loads(apiReq.text)['objects']

		objectSlugs = []
		for item in apiObjects:
			try:
				objectSlugs.append(item['publishedContent']['properties']['seo']['slug'])
			except:
				pass
		return objectSlugs
	except Exception as e:
		post_log(f'**Failure on scrapeSlugs thread {url}** \n \n {e} ', url)
		
def hitApi(url):
	useragents = getUserAgents()
	try:
		x = random.randint(0, (len(useragents) - 1))
		useragent = useragents[x]
	except:
		print('no user agents')
	headers = {
				"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
				"Accept-Encoding": "gzip, deflate, br",
				"Accept-Language": "en-US,en;q=0.5",
				"Connection": "keep-alive",
				"TE" : "Trailers",
				"Upgrade-Insecure-Requests": "1", 
				"User-Agent": useragent
				}
	proxies = getProxies()
	try:
		x = random.randint(0, (len(proxies) - 1))
		proxy = proxies[x]
		proxy_dict = {'https': ('socks5://{}'.format(proxy))}
	except:
		print('No proxies available. Using localhost...')
	
	try:
		apiReq = requests.get(url,headers=headers,proxies=proxy_dict, timeout=(60))
		apiInfo = json.loads(apiReq.text)
		apiObjects =  apiInfo['objects']
		return apiObjects
	except:
		post_log(str("Can't connect " + str(url)),"Main")
		time.sleep(int(1))


def main(API,Name):
		old_slugs = scrpaeSlugs(API)
		while old_slugs == None:
			old_slugs = scrpaeSlugs(API)
		post_log(f'{Name} Monitor has started.',Name)
		while True:
			try:
				apiObjects = hitApi(API)
				new_slugs = []
				if apiObjects != None:
					try:
						for item in apiObjects:
							try:
								new_slugs.append(item['publishedContent']['properties']['seo']['slug'])
							except:
								pass
						if new_slugs != None:
							differnces = set(new_slugs) - set(old_slugs)
							#Remove comment for next line to test spam the discord.
							#differnces = set(new_slugs)
							if differnces:
								for difference in differnces:
									for item in apiObjects:
										try:
											if item['publishedContent']['properties']['seo']['slug'] == difference:
												try:
													imageSqUrl = item['publishedContent']['properties']['coverCard']['properties']['squarishURL']
												except:
													imageSqUrl = 'Null'

												try:	
													imageLsUrl = item['publishedContent']['properties']['coverCard']['properties']['landscapeURL']
												except:
													imageLsUrl = 'Null'

												try:
													title = item['publishedContent']['properties']['seo']['slug'].upper()
												except:
													title = 'Null'

												try:
													status = item['productInfo'][0]['merchProduct']['status']
												except:
													#print('Error Parsing Status')
													status = 'Null'

												try:
													fullTitle = item['productInfo'][0]['productContent']['fullTitle']
												except:
													try:
														fullTitle = title
													except:
														#print('Error Parsing Full Title')
														fullTitle = 'Null'

												try:
													styleColor = item['productInfo'][0]['merchProduct']['styleColor']
												except:
													#print('Error Parsing Style Color')
													styleColor = 'Null'

												try:
													publishType = item['productInfo'][0]['merchProduct']['publishType']
												except:
													#print('Error Parsing Publish Type')
													publishType = 'Null'

												try:
													exclusiveAccess = item['productInfo'][0]['merchProduct']['exclusiveAccess']
												except:
													#print('Error Parsing Exclusive Access')
													exclusiveAccess = 'Null'

												try:
													hardLaunch = item['productInfo'][0]['merchProduct']['hardLaunch']
												except:
													#print('Error Parsing hard Launching')
													hardLaunch = 'Null'

												try:
													price = str(item['productInfo'][0]['merchPrice']['fullPrice']) +' USD'
												except:
													#print('Error Parsing Price')
													price = 'Null'

												try:
													availability = str(item['productInfo'][0]['availability']['available'])
												except:
													#print('Error Parsing Aviabality')
													availability = 'Null'

												try:
													method = item['productInfo'][0]['launchView']['method']
												except:
													#print('Error Parsing Method')
													method = 'Null'
												try:
													launchDate = item['productInfo'][0]['launchView']['startEntryDate']
												except:
													try:
														launchDate = item['productInfo'][0]['merchProduct']['commerceStartDate']
													except:
														#print('Error Parsing Launch Date')
														launchDate = 'Null'

												sizes = []
												try:
													for size,stock in zip(item['productInfo'][0]['skus'],item['productInfo'][0]['availableSkus']):
														sizes.append(size['countrySpecifications'][0]['localizedSize'] +' - Qty: '+ str(stock['level']))

												except:
													#print('Error Getting Size and Stock')
													sizes = ['Null']

												genders = []
												try:
													for gender in (item['productInfo'][0]['merchProduct']['genders']):
														genders.append(gender)

												except:
													#print('Error Getting Size and Stock')
													genders = ['Null']

												post_discord(imageSqUrl,imageLsUrl,title,fullTitle,status,styleColor,publishType,exclusiveAccess,hardLaunch,price,launchDate,availability,genders,method,Name,sizes)

												old_slugs = new_slugs
										except:
											pass

							else:
								#print(str(datetime.now())+ f' ------------------- Monitoring [ {Name} ]')
								time.sleep(int(delay))
					except Exception as e:
						post_log(f'**Failure on main thread {Name} in apiObjects** \n \n {e} ', Name)
						
					
			except Exception as e:
				post_log(f'**Total failure on main thread {Name}** \n \n {e} ', Name)
				
				time.sleep(int(delay))
			
if __name__ == "__main__":
	APIS = [
		"https://api.nike.com/product_feed/threads/v2?filter=marketplace(US)&filter=language(en)&filter=channelId(008be467-6c78-4079-94f0-70e2d6cc4003)&fields=id&fields=lastFetchTime&fields=productInfo&fields=publishedContent.properties",
		"https://api.nike.com/product_feed/threads/v2?filter=marketplace(CA)&filter=language(en-gb)&filter=channelId(008be467-6c78-4079-94f0-70e2d6cc4003)&fields=id&fields=lastFetchTime&fields=productInfo&fields=publishedContent.properties",
		"https://api.nike.com/product_feed/threads/v2?filter=marketplace(GB)&filter=language(en-gb)&filter=channelId(008be467-6c78-4079-94f0-70e2d6cc4003)&fields=id&fields=lastFetchTime&fields=productInfo&fields=publishedContent.properties",
		"https://api.nike.com/product_feed/threads/v2?filter=marketplace(DE)&filter=language(de)&filter=channelId(008be467-6c78-4079-94f0-70e2d6cc4003)&fields=id&fields=lastFetchTime&fields=productInfo&fields=publishedContent.properties",
		"https://api.nike.com/product_feed/threads/v2?filter=marketplace(FR)&filter=language(fr)&filter=channelId(008be467-6c78-4079-94f0-70e2d6cc4003)&fields=id&fields=lastFetchTime&fields=productInfo&fields=publishedContent.properties",
		"https://api.nike.com/product_feed/threads/v2?filter=marketplace(RU)&filter=language(ru)&filter=channelId(008be467-6c78-4079-94f0-70e2d6cc4003)&fields=id&fields=lastFetchTime&fields=productInfo&fields=publishedContent.properties",
		"https://api.nike.com/product_feed/threads/v2?filter=marketplace(AE)&filter=language(en-gb)&filter=channelId(008be467-6c78-4079-94f0-70e2d6cc4003)&fields=id&fields=lastFetchTime&fields=productInfo&fields=publishedContent.properties",
		"https://api.nike.com/product_feed/threads/v2?filter=marketplace(JP)&filter=language(ja)&filter=channelId(008be467-6c78-4079-94f0-70e2d6cc4003)&fields=id&fields=lastFetchTime&fields=productInfo&fields=publishedContent.properties",
		"https://api.nike.com/product_feed/threads/v2?filter=marketplace(CN)&filter=language(zh-Hans)&filter=channelId(008be467-6c78-4079-94f0-70e2d6cc4003)&fields=id&fields=lastFetchTime&fields=productInfo&fields=publishedContent.properties"
		]
	for API in APIS:
		if 'US' in API:
			apiName = 'SNKRS US'
		elif 'CA' in API:
			apiName = 'SNRKS CAN'		
		elif 'GB' in API:
			apiName = 'SNRKS UK'
		elif 'DE' in API:
			apiName = 'SNRKS GER'
		elif 'FR' in API:
			apiName = 'SNRKS FR'
		elif 'RU' in API:
			apiName = 'SNRKS RU'
		elif 'AE' in API:
			apiName = 'SNRKS UAE'
		elif 'JP' in API:
			apiName = 'SNKRS JP'
		elif 'CN' in API:
			apiName = 'SNKRS CN'

		threading.Thread(target=getProxies, name='getProxy').start()
		threading.Thread(target=main,args=(API,apiName,)).start()

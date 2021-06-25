import whois

# List of TLD's available from whois package
tld_list = [".ac.uk", ".am", ".amsterdam", ".ar", ".at", ".au", ".bank", ".be", ".biz", ".br", ".by", ".ca", ".cc", ".cl", ".club", ".cn", ".co", ".co.il", ".co.jp", ".com", ".com.au", ".com.tr", ".courses", ".cr", ".cz", ".de", ".download", ".edu", ".education", ".eu", ".fi", ".fm", ".fr", ".frl", ".game", ".global", ".hk", ".id", ".ie", ".im", ".in", ".info", ".ink", ".io", ".ir", ".is", ".it", ".jp", ".kr", ".kz", ".link", ".lt", ".lv", ".me", ".ml", ".mobi", ".mu", ".mx", ".name", ".net", ".ninja", ".nl", ".nu", ".nyc", ".nz", ".online", ".org", ".pe", ".pharmacy", ".pl", ".press", ".pt", ".pub", ".pw", ".rest", ".ru", ".ru.rf", ".rw", ".sale", ".se", ".security", ".sh", ".site", ".space", ".store", ".study", ".tech", ".tel", ".theatre", ".tickets", ".trade", ".tv", ".ua", ".uk", ".us", ".uz", ".video", ".website", ".wiki", ".work", ".xyz", ".za"]

def available_tlds():
	'''
		Get List of Available TLD's
	'''
	return tld_list

def getDetails(domain: str):
	'''
		Get Details of Entered Domain Name
	'''
	try:
		data = whois.query(domain)
	except (whois.exceptions.FailedParsingWhoisOutput, whois.exceptions.UnknownTld):
		return None
		
	if data is None:
		return None
	return data.__dict__
import configparser

def get_officescan_client_ptn():
	config=configparser.ConfigParser()
	config.read('C:\\Program Files (x86)\\Trend Micro\\OfficeScan Client\\updinfo.ini')
	return(int(config.get('INI_UPDATE_SECTION','Ptnfile_Version')))
	
if __name__ == '__main__':
	print(get_officescan_client_ptn())
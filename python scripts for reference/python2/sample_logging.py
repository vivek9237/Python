import logging
log_file = "root/script/log/out.log"
log_level = "debug"

def logWriter():
    if log_level == "debug":
        logging.basicConfig(filename=log_file,level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    elif log_level == "info":
        logging.basicConfig(filename=log_file,level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    elif log_level == "warning":
        logging.basicConfig(filename=log_file,level=logging.WARNING,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    else:
        logging.basicConfig(filename=log_file,level=logging.ERROR,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

logWriter()
try:
	logging.debug("sample debug")
	logging.info("sample info")
	logging.error("sample error")
except Exception as e:
	logging.exception(e)
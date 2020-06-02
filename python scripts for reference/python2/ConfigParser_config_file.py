import ConfigParser

config_file = 'config.ini'

def load_config_file(config_file):
    with open(config_file) as f:
        config_temp = f.read()
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.readfp(io.BytesIO(config_temp))
    global input_file_location, output_file_location, log_file, log_level
    input_file_location = config.get('DEFAULT','input_file_location')
    output_file_location = config.get('DEFAULT','output_file_location')
    log_file = config.get('LOG','log_file')
    log_level = config.get('LOG','log_level')
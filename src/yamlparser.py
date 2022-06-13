import yaml
import logging

_LOGGER = logging.getLogger(__name__)

def load_yaml(file):
    try:
        stram = open(file, "r")
        print(stram)
        yaml_data = yaml.safe_load(stram)
        return yaml_data
    except Exception as e:
        raise
        _LOGGER.error("Can't load yaml with sids %r (%r)" % (file, e))

def get_gateway_password(config, ip=""):
	if (config == None):
		raise "Config is null"
	configGateway = config.get("gateway", None)
	if (configGateway == None):
		raise "Config gateway is null"
	password = configGateway.get("password", None)
	if (password == None):
		raise "Config gateway passowrd is null"
	return password
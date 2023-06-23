import pyyeelight
import logging
import math

_LOGGER = logging.getLogger(__name__)

class LightBulbState:
	bright = 0
	color_temperature = 0
	status = "OFF"
	rgb = 0
	model = ""

	ip = ""
	name = ""
	yeelight = None # yeelight object

	def __init__(self, ip, model, yeelightObj):
		self.yeelight = yeelightObj
		self.model = model
		self.name = yeelightObj.__name__
		self.ip = ip

	def update_properties(self, force = False):
		if (force):
			self.yeelight.refresh_property()
		prop = self.yeelight.get_all_properties()
		# print(prop)
		self.bright = prop["bright"]
		self.color_temperature = prop["ct"]
		self.status = prop["power"].upper()
		self.rgb = prop["rgb"]

	def hash(self):
		return str(self.bright) + ":" + str(self.color_temperature) + ":" + str(self.status.upper()) + ":" + str(self.rgb)

	def is_int(self, x):
		try:
			tmp = int(x)
			return True
		except Exception as e:
			return False

	def process_command(self, value):
		_LOGGER.info("Turning on bulb: " + str(value['state']))
		try:
			if "state" in value:
				if (value['state'] == "on" or value['state'] == "ON"):
					_LOGGER.info("Turning on bulb: " + self.name)
					if("brightness" not in value or "brightness" in value and int(value['brightness']) > 0):
						self.yeelight.turn_on()
				if (value['state'] == "off" or value['state']== "OFF"):
					_LOGGER.info("Turning off bulb: " + self.name)
					self.yeelight.turn_off()
			if "brightness" in value:
				brightness = int(math.ceil(int(value['brightness'])/255*100))
				_LOGGER.info("Setting brightness of bulb " + self.name + " to " + str(brightness))
				if(brightness==0):
					self.yeelight.turn_off()
					brightness=1
				else:
					self.yeelight.set_brightness(brightness)
			if "color_temp" in value:
				colorTemp = (4800/100*(100-100/347*(int(value['color_temp'])-153))+1700)
				_LOGGER.info("Setting temperature of bulb " + self.name + " to " + str(colorTemp))
				self.yeelight.set_color_temperature(int(colorTemp))
			if "color" in value:
				Red = value['color']["r"]
				Green = value['color']["g"]
				Blue =  value['color']["b"]
				#intval = int(value)
				#Blue =  intval & 255
				#Green = (intval >> 8) & 255
				#Red =   (intval >> 16) & 255
				_LOGGER.info("Setting rgb of bulb" + self.name +'to ' + str(Red)+" "+str(Green)+" "+str(Blue))

				self.yeelight.set_rgb_color(Red, Green, Blue)
		except Exception as e:
			_LOGGER.error('Error while set value of bulb ' + self.name + ' error:', e)
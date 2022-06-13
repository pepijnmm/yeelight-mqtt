#forked for better home assistant(mqtt) support. it now is:
for example:

#kitchen lamp
  - platform: "mqtt"
    name: "kitchen_lamp"
    state_topic: "yeelight/light/kitchen"
    brightness: true
    color_temp: true
    rgb: true
    schema: "json"
    command_topic: "yeelight/light/kitchen/set"

# Yeelight to MQTT bridge

Works with Yeelight WiFi bulbs (color and monochrome).

bottom part not valid anymore. just go to the yeelight app then lan managment and enable the light you wanna start using
~You need to activate developer mode (http://forum.yeelight.com/t/trying-to-enable-developer-mode-with-yeelight-app-lamp-always-offline/137)~

Bridge accept following MQTT set:
```
"home/light/main-color/status/set" -> on 
```

will turn on light and translate devices state from gateway:
```
"home/light/main-color/status" on
"home/light/main-color/ct" 3500
"home/light/main-color/bright" 3
"home/light/main-color/rgb" 1247743
```

## Config
Edit file config/config-sample.yaml and rename it to config/config.yaml

## Docker-Compose
Sample docker-compose.yaml file for user:
```
yeelight:
  image: "monster1025/yeelight-mqtt"
  container_name: yeelight
  volumes:
    - "./config:/app/config"
  restart: always
```

## Known bugs:
- Lamp's alive status updated only at startup.

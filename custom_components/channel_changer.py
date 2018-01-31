import voluptuous as vol
import homeassistant.helpers.config_validation as cv
import json
import logging
from homeassistant.helpers.event import track_state_change
from homeassistant.const import STATE_ON, STATE_OFF, STATE_HOME, STATE_NOT_HOME, MATCH_ALL

DOMAIN = 'channel_changer'

_LOGGER = logging.getLogger(__name__)
# CONF_PROVIDER = 'Freeview'
# DEPENDENCIES = []

# CONFIG_SCHEMA = vol.Schema({
#     DOMAIN: vol.Schema({
#         vol.Required(CONF_PROVIDER): cv.string
#     })
# }, extra=vol.ALLOW_EXTRA)


def setup(hass, config):
    _LOGGER.debug(hass)
    _LOGGER.debug(config)
    #
    # # comp_conf = config['channel_changer']
    # # provider = comp_conf['provider']
    # _LOGGER.info("The 'battery' component is ready!")
    # # _LOGGER.debug("TV Provider: ", provider)
    #
    # def state_changed(entity_id, old_state, new_state):
    #     _LOGGER.info("Entity_id: ", entity_id)
    #     _LOGGER.info("Old state: ", old_state)
    #     _LOGGER.info("New state: ", new_state)
    #
    #     if entity_id == 'input_select.virgin_media_channels':
    #         cl = ChannelChanger()
    #         cl.change_channel_to(new_state, hass)
    #
    # track_state_change(hass, MATCH_ALL, state_changed)
    #
    return True


class ChannelChanger:

    def __init__(self):
        self.jsonPath = '/home/john/.homeassistant/www/assets/vm_channels.json'
        self.channel_name = ''
        self.channel_number = ''
        self.number_list = []
        self.json_string = ''
        self.all_channels = ''
        self.channel_details = ''

    def get_json(self):
        json_contents = open(self.jsonPath)
        json_str = json_contents.read()
        self.json_string = json.loads(json_str)

    def get_channels(self):
        self.all_channels = self.json_string['channels']

    def get_channel_details(self):
        self.channel_details = self.all_channels[self.channel_name]

    def get_channel_number(self):
        self.channel_number = self.channel_details['channel_number']

    def convert_channel_to_list(self):
        self.number_list = list(self.channel_number)

    def change_channel_to(self, channel_name, hass):
        self.channel_name = channel_name
        self.get_json()
        self.get_channels()
        self.get_channel_details()
        self.get_channel_number()
        self.convert_channel_to_list()

        for button_name in self.number_list:
            remote_button_name = 'remote__virgin_media__' + button_name


            hass.services.call('switch', 'turn_on', {'entity_id': remote_button_name})
            _LOGGER.info("Changed Channel to: ", button_name)



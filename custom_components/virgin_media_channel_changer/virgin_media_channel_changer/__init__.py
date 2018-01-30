import json


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

    def change_channel_to(self, channel_name):
        self.channel_name = channel_name
        self.get_json()
        self.get_channels()
        self.get_channel_details()
        self.get_channel_number()
        self.convert_channel_to_list()

        for button_name in self.number_list:
            remote_button_name = 'remote__virgin_media__' + button_name
            hass.services.async_call('switch', 'turn_on', {'entity_id': remote_button_name})
            print("Number: ", button_name)


name = data.get('name', 'world')
logger.error("Hello {}".format(name))

bbc = ChannelChanger()
bbc.change_channel_to(name)

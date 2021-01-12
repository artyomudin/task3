class TVController:
    CHANNELS = ['Nullchannel', "BBC", "Discovery", "TV1000"]

    def __init__(self, name, num ):
        self.num = num
        self.name = name

    def first_channel():
        return TVController.CHANNELS[1]

    def last_channel():
        return TVController.CHANNELS[-1]

    def turn_channel(n):
        current_chan = n
        if n in range(1,len(TVController.CHANNELS)+1):
            return TVController.CHANNELS[n]
        else:
            return 'the channel does not exist'

    def current_channel(i):
        return TVController.CHANNELS[i]

    def next_channel():
        cur_chan = 1
        if cur_chan in range(1,len(TVController.CHANNELS)+1):
            return TVController.CHANNELS[cur_chan+1]

    def previous_channel():
        cur_chan = 2
        if cur_chan in range(1, len(TVController.CHANNELS) + 1) and cur_chan !=1:
            return TVController.CHANNELS[cur_chan - 1]
        elif cur_chan == 1:
            return TVController.CHANNELS[-1]

    def is_exist(chan = None, number = None):
        if chan in TVController.CHANNELS:
            return'yes'
        else:
            return 'no'





print(TVController.first_channel())
print(TVController.last_channel())
print(TVController.turn_channel(1))
print(TVController.next_channel())
print(TVController.current_channel(1))
print(TVController.previous_channel())
print(TVController.is_exist("TV1000"))





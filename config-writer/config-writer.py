import configparser
config = configparser.ConfigParser()

config['GPU'] = {}
config['GPU']['GPU_FORCE_64BIT_PTR'] = '0'
config['GPU']['GPU_MAX_HEAP_SIZE'] = '100'
config['GPU']['GPU_USE_SYNC_OBJECTS'] = '1'
config['GPU']['GPU_MAX_ALLOC_PERCENT'] = '100'
config['GPU']['GPU_SINGLE_ALLOC_PERCENT'] = '100'

config['Rig'] = {}
config['Rig']['Miner'] = 'z-enemy'
config['Rig']['Wallet'] = 'RSgJXrFK9862goUzj1jBx923RMVXGvJKuw'
config['Rig']['Rigname'] = ''
config['Rig']['Stats'] = ''
config['Rig']['Intensity'] = '20'

config['Pool1'] = {}
config['Pool1']['Address'] = 'pool.dedpool.io'
config['Pool1']['Port'] = '3636'

config['Pool2'] = {}
config['Pool2']['Address'] = 'ravenminer.com'
config['Pool2']['Port'] = '3636'

config['Pool3'] = {}
config['Pool3']['Address'] = 'miningpanda.site'
config['Pool3']['Port'] = '3666'

config['TIMESHARE'] = {}
config['TIMESHARE']['enabled'] = 'False'
config['TIMESHARE']['YourTime'] = '3600'
config['TIMESHARE']['TimeshareTime'] = '300'
config['TIMESHARE']['timesahreaddress'] = 'RT2r9oGxQxbVE1Ji5p5iPgrqpNQLfc8ksH'

with open('config.ini', 'w') as configfile:
    config.write(configfile)
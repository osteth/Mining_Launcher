'''
Ultimate Mining Launcher v0.1 By @SethWahle

'''
import configparser, os, subprocess, time, signal, sys, socket
    
def build_args(Pool, wallet, extra):
    launcher = config['Rig']['Miner'] + ' -a x16r -o ' + 'stratum+tcp://' + Pool + ' -u ' + wallet + ' -p c=RVN' + extra + ' -i '  + config['Rig']['Intensity'] + ' --retries=4 -R 5'
    return(launcher)

def check_pool(address, port): 
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print("socket creation failed with error %s") %(err)
    try:
        host_ip = socket.gethostbyname(address)
    except socket.gaierror:
        return False
        sys.exit()
    s.connect((host_ip,int(port)))
    return True 
    
def pool_status(poolnumber):
    pools = {check_pool(config['Pool1']['Address'], config['Pool1']['Port']), 
           check_pool(config['Pool2']['Address'], config['Pool2']['Port']), 
           check_pool(config['Pool3']['Address'], config['Pool3']['Port'])}
    return(pools[poolnumber])
           
def launch_strings():        
    #Concatinates the extra options into a properly formated string based on if rigname or stats options are set in config. 
    if not config['Rig']['Rigname']:
        extra = config['Rig']['Rigname']
        if not config['Rig']['Stats']:
            extra = extra + config['Rig']['Stats']
    else:
        if not config['Rig']['Stats']:
            extra = config['Rig']['Stats']
    #build launcher strings based on config options.    
    user_arg1 = build_args(config['Pool1']['Address'] + ":" + config['Pool1']['Port'], config['Rig']['Wallet'], extra)
    user_arg2 = build_args(config['Pool2']['Address'] + ":" + config['Pool2']['Port'], config['Rig']['Wallet'], extra)
    user_arg3 = build_args(config['Pool3']['Address'] + ":" + config['Pool3']['Port'], config['Rig']['Wallet'], extra)
    timeshare_arg1 = build_args(config['Pool1']['Address'] + ":" + config['Pool1']['Port'], config['TIMESHARE']['timesahreaddress'], extra)
    timeshare_arg2 = build_args(config['Pool2']['Address'] + ":" + config['Pool2']['Port'], config['TIMESHARE']['timesahreaddress'], extra)
    timeshare_arg3 = build_args(config['Pool3']['Address'] + ":" + config['Pool3']['Port'], config['TIMESHARE']['timesahreaddress'], extra)
    argstrings = [user_arg1, user_arg2, user_arg3, timeshare_arg1, timeshare_arg2, timeshare_arg3]
    return (argstrings)

def mine():
    while 1 == 1:
        if check_pool(config['Pool1']['Address'], config['Pool1']['Port']) and check_pool(config['Pool2']['Address'], config['Pool2']['Port']) and check_pool(config['Pool3']['Address'], config['Pool3']['Port']) == False:
            print('No Pools Available, Check Internet Connection~!')
            print('Will retry in 30 seconds')
            time.sleep(30)
        else:
            if check_pool(config['Pool1']['Address'], config['Pool1']['Port']) == True:
                if config['TIMESHARE']['enabled'] == 'True':
                    print('Mining on Pool#1 with timeshare enabled')
                    handle = subprocess.Popen(launch_strings[3], shell=True)
                    time.sleep(int(config['TIMESHARE']['TimeshareTime']))
                    handle.kill()
                    handle = subprocess.Popen(launch_strings[0], shell=True)
                    time.sleep(int(config['TIMESHARE']['YourTime']))
                    handle.kill()
                else: 
                    print('Mining on Pool#1 with Timeshare Dissabled')
                    handle = subprocess.Popen(launch_strings[0], shell=True)
                    time.sleep(int(config['TIMESHARE']['YourTime']))
                    handle.kill()
                    
            elif check_pool(config['Pool2']['Address'], config['Pool2']['Port']) == True:
                if config['TIMESHARE']['enabled'] == 'True':
                    print('Mining on pool#2 with timeshare dissabled')
                    handle = subprocess.Popen(launch_strings[4], shell=True)
                    time.sleep(int(config['TIMESHARE']['TimeshareTime']))
                    handle.kill()
                    handle = subprocess.Popen(launch_strings[1], shell=True)
                    time.sleep(int(config['TIMESHARE']['YourTime']))
                    handle.kill()
                else: 
                    print('Mining on pool#2 with timeshare dissabled')
                    handle = subprocess.Popen(launch_strings[1], shell=True)
                    time.sleep(int(config['TIMESHARE']['YourTime']))
                    handle.kill()
                    
            elif check_pool(config['Pool3']['Address'], config['Pool3']['Port']) == True:
                if config['TIMESHARE']['enabled'] == 'True':
                    print('Mining on pool #3 with timeshare Enabled')
                    handle = subprocess.Popen(launch_strings[5], shell=True)
                    time.sleep(int(config['TIMESHARE']['TimeshareTime']))
                    handle.kill()
                    handle = subprocess.Popen(launch_strings[2], shell=True)
                    time.sleep(int(config['TIMESHARE']['YourTime']))
                    handle.kill()
                else: 
                    print('Mining on pool#3 with timeshare dissabled')
                    handle = subprocess.Popen(launch_strings[2], shell=True)
                    time.sleep(int(config['TIMESHARE']['YourTime']))
                    handle.kill()
                
# ---------------------------------------------------------------------------------------|
# || Read Configuration file 
config = configparser.ConfigParser()   
config.read('config.ini')

# ---------------------------------------------------------------------------------------|
# || Setup GPU Environment Options!
os.environ["GPU_FORCE_64BIT_PTR"] = config["GPU"]["GPU_FORCE_64BIT_PTR"]
os.environ["GPU_MAX_HEAP_SIZE"] = config["GPU"]["GPU_MAX_HEAP_SIZE"]
os.environ["GPU_USE_SYNC_OBJECTS"] = config["GPU"]["GPU_USE_SYNC_OBJECTS"]
os.environ["GPU_MAX_ALLOC_PERCENT"] = config["GPU"]["GPU_MAX_ALLOC_PERCENT"]
os.environ["GPU_SINGLE_ALLOC_PERCENT"] = config["GPU"]["GPU_SINGLE_ALLOC_PERCENT"]
print('GPU_FORCE_64BIT_PTR =',config["GPU"]["GPU_FORCE_64BIT_PTR"])
print('GPU_MAX_HEAP_SIZE =', config["GPU"]["GPU_MAX_HEAP_SIZE"])
print('GPU_USE_SYNC_OBJECTS =', config["GPU"]["GPU_USE_SYNC_OBJECTS"])
print('GPU_MAX_ALLOC_PERCENT =', config["GPU"]["GPU_MAX_ALLOC_PERCENT"])
print('GPU_SINGLE_ALLOC_PERCENT =',config["GPU"]["GPU_SINGLE_ALLOC_PERCENT"])


launch_strings = launch_strings()
mine()       
            

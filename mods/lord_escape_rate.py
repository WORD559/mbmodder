import os, shutil, re

from modframework import Mod

def lord_escape_rate(rate_in_percent,module,warband_dir):
    """Sets probability of a lord escaping after being defeated in battle by the player."""
    try:
        x = int(rate_in_percent)
        if x < 0:
            raise ValueError
        if x > 100:
            raise ValueError
    except:
        print "Invalid rate -- exiting"
        return

    # Check module exists
    module_path = "{base}/game/Modules/{module}".format(base=warband_dir,module=module)
    if not os.path.isdir(module_path):
        print "Module does not exist -- exiting"
        return
    
    # Back up the module's scripts file
    scripts_file = module_path+"/scripts.txt"
    shutil.copy(scripts_file,scripts_file+".bak")

    # Open it and read it
    with open(scripts_file,"r") as to_read:
        scripts_data = to_read.read().split(" ")
    if os.name == "posix": # convert line endings if need be
        scripts_data = [i.strip("\r") for i in scripts_data]
    
    # Find and replace the correct value
    header_index = scripts_data.index("\ncf_check_hero_can_escape_from_player")
    chance_index = header_index+76
    print "Current value is {chance}%".format(chance=scripts_data[chance_index])
    print "Changing to {new}%".format(new=rate_in_percent)
    scripts_data[chance_index] = str(rate_in_percent)

    # Reconstruct config file
    scripts_data = " ".join(scripts_data)

    # Write to file 1kiB at a time
    with open(module_path+"/scripts.txt","w") as to_write:
        while len(scripts_data) > 0:
            to_write.write(scripts_data[:1024])
            scripts_data = scripts_data[1024:]

    print "Replaced!"

# Create the mod with the function
mod = Mod(lord_escape_rate)

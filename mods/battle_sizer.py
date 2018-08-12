# Battle sizer mod

import os, shutil, re

def battle_size(units,config_dir):
    """Sets numbers of units allowed in a battle at once."""
    # num_units = 30 + 120*battle_size
    battle_size = round((int(units)-30)/120.,4)
    print "Setting battle_size to '{num:1.4f}'...".format(num=battle_size)

    # Back up the config file
    config_file = config_dir+"/rgl_config.txt"
    shutil.copy(config_file,config_file+".bak")

    # Open it and read it
    with open(config_dir+"/rgl_config.txt","r") as config_file:
        config_data = config_file.read().split("\n")
    if os.name == "posix": # convert line endings if need be
        config_data = [i.strip("\r") for i in config_data]
    
    # Find and replace the correct line
    found = False
    regex = re.compile("^battle_size = .*$")
    for line in range(len(config_data)):
        if regex.match(config_data[line]):
            print "Found line, replacing..."
            new_line = "battle_size = {num:1.4f}".format(num=battle_size)
            config_data[line] = new_line
            found = True
            break
    if not found:
        print "Unable to find correct line. Has config been manually edited before?"
        return

    # Reconstruct config file
    config_data = "\n".join(config_data)

    # Write to file
    with open(config_dir+"/rgl_config.txt","w") as config_file:
        config_file.write(config_data)

    print "Replaced!"

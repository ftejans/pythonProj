#dict to hold settings:
# ch1_settings = ['channel': '5A', 'enable': True, 'wave': 'square', 'freq_hz': 5e5, 'volts': 3.5]
ch1_settings = {
    "channel": "5A", 
    "volts":"3.5"
    }

#Retrieving items from dictionary
print(ch1_settings["channel"])

#Adding items to dictionary
ch1_settings["Wave"]="square"
print(ch1_settings)

#Create an empty dictionary
empty_settings = {}

# #Wipe an existing dictionary
# ch1_settings ={}
# print(ch1_settings)

# #Edit an item in a dictionary
# ch1_settings["channel"] = "5B"
# print (ch1_settings)

# #Loop through a dictionary - long way
# for setting in ch1_settings:
#     if setting == "channel":
#         print(f"Channel set is: {ch1_settings["channel"]}")
#     elif setting == "volts":
#         print(f"voltage set is: {ch1_settings["volts"]}")
#     elif setting == "Wave":
#         print(f"Wave set is: {ch1_settings["Wave"]}")
#     else:
#         print("nothing") 

#Loop through a dictionary- short way
for key in ch1_settings:
    print(f"{key}:", ch1_settings[key])
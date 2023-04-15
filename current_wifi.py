import subprocess 
wifi_list_rssi = {} #Get the rssi signal strange data of the current wifi 
try:
   output = subprocess.check_output("iwgetid",shell=True) 
   name_current_wifi = output.decode().split("\n")[0].split("   ")[1].split(" ")[1].split(":")[1]
   print(name_current_wifi) 
   # input the current wifi name to find the current rssi signal strange 
   wifi_strange = subprocess.check_output("iwlist scanning",shell=True)
   get_rssi = wifi_strange.decode()
   print(get_rssi.split("\n")[3].split("    ")[5]) 
   print(get_rssi.split("\n")[4].split("    ")[5])
   print(get_rssi.split("\n")[6].split("    ")[5]) 
   wifi_list_rssi[name_current_wifi] = {'wifi_freq':get_rssi.split("\n")[3].split("    ")[5],'rssi_signal':get_rssi.split("\n")[4].split("    ")[5]}
   print(wifi_list_rssi) 
   
except:
   print("Current wifi not found you are not connected")
   

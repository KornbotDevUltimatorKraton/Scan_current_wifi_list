import math 
import requests 
import subprocess 
import time
from itertools import count 

wifi_list_rssi = {} #Get the rssi signal strange data of the current wifi 

# Get the wifi localization from rssi from the local robot indoor environment 
def distance_RSSI(Pt,Pl,rssi): 
      A = Pt-Pl 
      c_dat = (A-rssi)*0.014336239
      d = math.pow(10,c_dat) 
      return d

for i in count(0): # running loop in count  
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
       data_local = get_rssi.split("\n")[4].split("    ")[5].split(" ")
       print(data_local)
       A_diff = data_local[0].split("=")[1].split("/")
       rssi_value = data_local[3].split("=")[1]
       distance_data =   distance_RSSI(int(A_diff[1]),int(A_diff[0]),float(rssi_value))
       wifi_list_rssi[name_current_wifi] = {'wifi_freq':get_rssi.split("\n")[3].split("    ")[5].split(":")[1],'rssi_signal':data_local[3].split("=")[1],"A":int(A_diff[1]) - int(A_diff[0]),'distance':distance_data}
       print(wifi_list_rssi)
       payload_data = {"kornbot380@hotmail.com":wifi_list_rssi}
       rssi_post_robot = requests.post("https://roboreactor.com/rssi_robot_client",json=payload_data)
       print(rssi_post_robot.json())
       time.sleep(0.5)
  except:
       print("Current wifi not found you are not connected")
   

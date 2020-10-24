import time
  
# Timer starts 
Start=time.time() 
Last=Start 
Lap_No=1
  
print("Count Laps: Press ENTER")
print("Stop: Press CTRL+C")
  
try: 
     while True: 
              
          input() #If user presses enter

          # The current lap-time 
          Lap_Time=round((time.time() - Last), 2) 
  
          # Total time elapsed from start of timer
          Total_Time=round((time.time() - Start), 2) 
  
          print("Lap No. "+str(Lap_No))  
          print("Total Time Elapsed: "+str(Total_Time)) 
          print("Lap Time: "+str(Lap_Time)) 
            
          print("*"*20) 
  
          # Updating the previous total time 
          # and lap number 
          Last=time.time() 
          Lap_No+=1
  
except KeyboardInterrupt: 
     print("Stopping Counting Laps")
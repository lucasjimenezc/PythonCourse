#Day 9 Blind auction
import os
print('''                                                                                                                            ░░░░░░  
                                                                                                                        ░░░░░░░░░░░░░░▒▒▒▒
                                                                                                                ░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒
                                                                                                        ░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░▒▒▒▒▒▒▒▒
            ░░░░░░░░░░                                                                            ░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░
      ░░░░░░░░░░░░░░░░░░░░                                                                  ░░░░░░░░░░    ░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░  
    ░░░░░░░░░░░░░░░░░░░░░░░░                                                        ░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▓▓░░      
  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░                                              ░░░░    ░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒░░            
  ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░                                      ░░░░  ░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██▓▓░░                    
  ▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░                        ░░░░    ░░░░░░░░░░  ░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒░░░░                          
  ▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░              ░░░░░░░░░░  ░░░░  ░░░░░░▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒░░░░                                  
  ░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░          ░░░░░░░░░░  ░░░░░░░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒░░                                          
  ░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░    ░░░░░░░░░░░░░░░░▒▒░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒░░░░                                              
    ▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░                                                      
    ▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░                                                            
    ░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░                                                                  
    ░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒░░░░                                                                      
      ▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░                                                                          
      ▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░                                                                                  
      ░░▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░                                                                                        
        ▒▒▒▒▒▒▒▒▒▒░░░░░░░░  ░░░░░░░░░░░░░░░░░░░░                                                                                          
        ░░▒▒▒▒▒▒▒▒░░░░░░░░  ░░░░░░░░░░░░░░░░░░▒▒                                                                                          
        ░░░░▒▒▒▒▒▒▒▒░░░░░░░░  ░░░░░░░░░░░░░░░░▒▒                                                                                          
          ░░▒▒▒▒▒▒▒▒▒▒░░░░░░      ░░▒▒▒▒▓▓▓▓▓▓▓▓░░                                                                                        
            ░░▒▒▒▒▒▒▒▒▒▒░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                                                                        
            ░░░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒                                                                                        
              ░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒                                                                                        
                ░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░                                                                                        
                ░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░                                                                                        
                  ░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░                                                                                        
                    ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░                                                                                          
                      ▒▒▓▓▓▓▓▓▓▓▓▓████▓▓▒▒░░░░                                                                                            
                      ░░▒▒▓▓▓▓▓▓▒▒▒▒▒▒░░░░      '''                                                                                       
)
bids = {}
print("\nWelcome to the blind auction program")
seguir = "yes"
mayor = 0
winner = ""
while(seguir=="yes"):
    name = input("Insert your name:\n")
    bid = int(input("Insert your bid (only numbers)\n$ "))
    bids[name] = bid
    seguir = input("Any more bids?('yes' to continue)\n")
    os.system ("clear") 
print(bids)
for key in bids:
    if bids[key] > mayor : 
        mayor = bids[key]
        winner = key

print(f"The winner is {winner} with a bid of {mayor}$")




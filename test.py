real_id = "dym"
real_mdp = "test"

while True:
    input_id = input("Entrez l'id: ")
    input_mpd = input("Entrez le mdp: ")
    if input_id != real_id and input_mpd != real_mdp:
        print("Login ou mdp incorrect")
        continue
    else:
        break
    
print ("Bienvenu ", real_id)


places_list=[]
for i in range(1,6):
    places = input(f"Enter the name of place {i} :")
    places_list.append(places)
print(f"\n places stored in list : {places_list}")
str_places=", ".join(places_list)
print(f"\n All places seperated by comma and space {str_places.upper()}")
    
    
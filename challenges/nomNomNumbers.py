#function that "eats" a number to its right in a list if the number is larger 
#when it eats, it becomes the sum of both numbers
#process repeats from left to right until no more eating can happen

#note that this version will skip a number and move on to the next one in order to evaluate the entire list

def nom_noms(nom_nom_list):
    final_nom_nom_list = []
    def small_nom_noms(nom_nom_list):
        for index, x in enumerate(nom_nom_list):
            if len(nom_nom_list) > 1 and x > nom_nom_list[index + 1]:               #
                nommed = x + nom_nom_list[index + 1]
                del nom_nom_list[index: index + 2]
                nom_nom_list.insert(0, nommed)
                small_nom_noms(nom_nom_list)
            elif len(nom_nom_list) > 1 and x <= nom_nom_list[index + 1]:
                final_nom_nom_list.append(nom_nom_list[index])
                del nom_nom_list[index]
                small_nom_noms(nom_nom_list)
            else:
                final_nom_nom_list.append(nom_nom_list[index])
                print(final_nom_nom_list)
            break
    small_nom_noms(nom_nom_list)


nom_noms([5,4,5,6,7,8,9,10,11,100])
nom_noms([1,5,4,5,6,7,8,9,10,11,100])
nom_noms([5,3,7])
nom_noms([5,3,9])
nom_noms([1,2,3])
nom_noms([2,1,3])
nom_noms([8,5,9])
nom_noms([6,5,6,100])

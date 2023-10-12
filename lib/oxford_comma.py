def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return items[0] + " and " + items[1]
    elif len(items) >= 3:
        last_item = items[-1]
        #print(last_item)
    
        i = 0
        remaining_items = list()
        while i < len(items) - 1:
            remaining_items.append(items[i])
            i += 1
        #print(remaining_items)
        new_string = ", ".join(remaining_items)
        #print(new_string)
        final_string = new_string + ', and ' + last_item
        return final_string
        











    #removed_elements = list()
    #last_element = items[-1]

    #for element in range(len(items) - 1):
        #removed_elements.append(element)


    #def join_all_elements(string1,string2):
        #first_string = ",".join(string1)
        #final_string = first_string + 'and' + string2
        #return final_string
    #join_all_elements(removed_elements, last_element)

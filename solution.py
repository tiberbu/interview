



 def get_mask_user_details():
        first_name = "Fredrick"
        last_name = "Maina"
        date_of_birth = "1996-06-26"
        email = "fredmainahk@gmail.com"

        # create a python dictionary that takes in the data,
        # masks all other characters if dic item starts with a char
        # else mask first 2 details for year, one for month and day


        personal_details = {
            "first_name" : "Fredrick",
             "last_name" : "Maina",
              "date_of_birth" : "1996-06-26",
               "email" : "fredmainahk@gmail.com",
        }

        for detail in personal_details:
            unmasked_detail = str(personal_details)
            masked_detail = len(unmasked_detail[:-2])*"#"+unmasked_detail[-2:]   

            new_list = []
            new_list.update(masked_detail)
        return jsonify(new_list)




get_mask_user_details()

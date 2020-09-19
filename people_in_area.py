def people_in_rec_area(length_1, length_2, social_d):
    area = length_1*length_2
    max_people_in_rec = int(area/(social_d**2))
    return (max_people_in_rec)

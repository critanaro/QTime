def people_in_rec_area(length_1, length_2, social_d):
    """This function's job is to tell us how many people can fit in a rectangular area. We model people as equally sized circles, with the distance between the center of two circles being the "social distance" between them. Our function takes the lengths of the rectangle and the distance between the center of two adjacent circles as inputs.
    The circles are laid out in a rectangular grid within the rectangular area. This way, the lengths of the sides of the rectange can be given by L1=n*2r and L2 = m*2r where n and m are the number of circles and r is the radius of each circle. We also let social_d = 2r, the distane between the center of two circles."""
    if length_1 <= 0 or length_2 <= 0 or social_d <= 0:
        raise Exception("Lengths of rectangle and the social distance should be positve numbers.")
    else:
        area = length_1*length_2 #We model our waiting area as a rectangle whose area we define as the product of its length and width.
        max_people_in_rec = int(area/(social_d**2)) #We take A = n*m*social_d^2, where n*m yields the max number of people that can fit in the area. We get: n*m = number of people = area/social_d^2
        return (max_people_in_rec) #returns the maximum number of people in the rectangular area

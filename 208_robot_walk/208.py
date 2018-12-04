
import sympy






def populate_direction(start_dir):

    if start_dir not in known_dirs:
        known_dirs.update([start_dir])
        # print known_dirs

        right_dir = start_dir - 2 * sympy.pi / 5
        left_dir = start_dir + 2 * sympy.pi / 5


        populate_direction(right_dir)
        populate_direction(left_dir)

    # if ()

def walk(start_dir, start_point, choice_dir, start_center, center_relative_pos):
    if not choice_dir:
        end_dir = start_dir + 2 * sympy.pi / 5
    else:
        end_dir = start_dir - 2 * sympy.pi / 5

    (x0, y0) = start_point
    (cx0, cy0) = start_center

    if center_relative_pos == choice_dir:
        end_relative_pos = choice_dir
        end_center = start_center

    else:
        end_center = ((2*x0 - cx0)/2, (2*y0 - cy0)/2)
        end_relative_pos = not choice_dir

    #return end_center, end_dir

    return (end_center, end_dir, end_relative_pos)


left = False
right = True

#choice dir, true -> right, false -> left
#relative position: true -> center is the right of direction, false -> center is on the left of direction

if __name__ == "__main__":
    start_dir = sympy.pi / 2
    start_point = (1, 0)
    start_center = (0,0)
    start_relative_pos = left

    for i in range(5):
        (start_center, start_dir, start_relative_pos) = walk(start_dir=start_dir, start_point=(1, 0), choice_dir=right,
                                                   start_center=start_center, center_relative_pos=start_relative_pos)
        print (start_point, start_dir, start_relative_pos)

        # (x,y) = start_point
        # print x + sympy.cos(start_dir)
        # print y + sympy.sin(start_dir)
        #

        if start_point == (1,0):
            print "home!"



    # print known_dirs

    # existing_tuple  = { (start_dir)}
    #
    # while True:


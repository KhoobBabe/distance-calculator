def points_distance(main_list):
    tot_dis = 0
    #two consecutive tuples taken  
    for i in range(len(main_list)-1):
        for j in range(i+1, len(main_list)):

            #initial distance is zero
            

            #distance taken between two consecutive points
            x = (float(main_list[i+1][0]) - float(main_list[i][0]))**2
            y = (float(main_list[i+1][1]) - float(main_list[i][1]))**2
            dis = ((x + y)**0.5)
        #adding the distance between all the points
        tot_dis += dis

    print("The distance between points is: ", "%.3f" % tot_dis)


#code starts from here
#input taken for how many points are needed
poin_num = int(input("How many points do you want to enter: "))

#initial main list is empty like the brain
main_list = []

#inputs taken for the number of points as requested by the client
for i in range(poin_num):
    tup = eval(input("enter the point: "))
    #tuples added in the main list
    main_list.append(tup)

points_distance(main_list)


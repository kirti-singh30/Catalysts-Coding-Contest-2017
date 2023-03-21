
import math
import sys

def travelDistance( a, b):
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 =b[1]
    d = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
    return d

def  travelTime( distance,  speed) :
    return distance / speed

def  journeyTime( journey,  hyper) :
    tA = travelDistance(journey[0], hyper[0])
    tB = travelDistance(journey[0], hyper[1])
    t = 200.0
    if (tA < tB) :
        t += travelTime(tA, 15.0)
        t += travelTime(travelDistance(hyper[1], journey[1]), 15.0)
    else :
        t += travelTime(tB, 15.0)
        t += travelTime(travelDistance(hyper[0], journey[1]), 15.0)
    t += travelTime(travelDistance(hyper[0], hyper[1]), 250.0)
    return t

def hyperlooptime(start,des):
    travel_time = travelDistance(start,des)/250.0 + 200.0
    return round(travel_time)

def drivetime(loc1,loc2):
    return travelDistance(loc1,loc2)/15.0

def closestLocation( startLoc,  locations) :
    distances =  dict()
    for key,value in locations.items() :
        distances[key] = travelDistance(startLoc, value)
    
    #del distances[startLoc]
    #print(distances)
    max_idx = min(distances, key = distances.get) 
    #print(f"closest location is {max_idx}")
    return locations[max_idx]

def sortest_drive_time(hyperloop_locations,location_dict,loc):

    hyperloop_loc_dict = {}
    hyperloop_loc_dict[hyperloop_locations[0]] =  location_dict[hyperloop_locations[0]]
    hyperloop_loc_dict[hyperloop_locations[1]] =  location_dict[hyperloop_locations[1]]

    close_location = closestLocation(location_dict[loc],hyperloop_loc_dict)

    if loc in hyperloop_locations:
        drive_time = -1
    else:
        drive_time = drivetime(location_dict[loc],close_location)
    return drive_time

def total_drive_time(hyperloop_locations,location_dict,start,des):

    start_drive_time = sortest_drive_time(hyperloop_locations,location_dict,start)
    des_drive_time = sortest_drive_time(hyperloop_locations,location_dict,des)
    hyper_time = hyperlooptime(location_dict[hyperloop_locations[0]],location_dict[hyperloop_locations[1]])
    total_time = round(start_drive_time + hyper_time + des_drive_time)

    return total_time

def faster_journey(hyperloop_locations,location_dict,journey_dict):
    i = 0
    for _,value in journey_dict.items():
        start = value["loc1"]
        des = value["loc2"]
        current_time = value["time"]
        drive_time = total_drive_time(hyperloop_locations,location_dict,start,des)
        if drive_time < current_time:
            i+=1
            print(f"Faster journey between {start}, {des} with {drive_time}")
    return i


if __name__ == "__main__":

    args = sys.argv

    # read the input and output files
    with open(sys.argv[1], 'r') as f:
        input_data = f.read()
    input_data = input_data.rstrip()
    input_data_list = input_data.split('\n')
    # now extract the locations and coordinates
    hyperloop_locations = input_data_list[-1].split(" ")
    number_locs = int(input_data_list[0])
    #start,destination = input_data_list[-2].split(" ")[0],input_data_list[-2].split(" ")[1]
    # get the number of journey
    num_journey = input_data_list[number_locs+1]
    journey_list = input_data_list[number_locs+2:-1]

    location_dict = {}
    for locations in input_data_list[1:number_locs+1]:
        location_details = locations.split(" ")
        location_dict[location_details[0]] =[int(location_details[1]),int(location_details[2])] 
    #print(location_dict)
    journey_dict = {}
    i = 0
    for j in journey_list:
        journey_dict[i]={}
        journey_dict[i]["loc1"] = j.split(" ")[0]
        journey_dict[i]["loc2"] = j.split(" ")[1]
        journey_dict[i]["time"] = int(j.split(" ")[2])
        i+=1

    print(f"number of Locations is {number_locs}")
    print(f"number of journey is {num_journey}")
    # print(f"journey list {journey_list}")
    # print(f"Location dict  {location_dict}")
    # print(f"journey dict  {journey_dict}")
    # print(f"Start {start} and destination is {destination}")
    print(f"Hyperloop Locations is {hyperloop_locations}")

    num_faster_j = faster_journey(hyperloop_locations,location_dict,journey_dict)
    print(f"Number of fastewr journey {num_faster_j}")
    
    # print(f"start Time is {start_drive_time}")
    # print(f"hyper Time is {hyper_time}")
    # print(f"des Time is {des_drive_time}")
    # print(f"Travel Time is {total_time}")
    # write results
    #output_file.write("{}".format(hyper_time))


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
    print(f"closest location is {max_idx}")
    return locations[max_idx]

if __name__ == "__main__":

    args = sys.argv

    # read the input and output files
    input_file = open(args[1], 'r')
    #output_file = open(args[2], 'w')
    with open(sys.argv[1], 'r') as f:
        input_data = f.read()
    input_data = input_data.rstrip()
    input_data_list = input_data.split('\n')
    # now extract the locations and coordinates
    hyperloop_locations = input_data_list[-1].split(" ")
    hyperloop_loc_dict = {}
    
    start,destination = input_data_list[-2].split(" ")[0],input_data_list[-2].split(" ")[1]
    location_dict = {}
    for locations in input_data_list[1:-2]:
        location_details = locations.split(" ")
        location_dict[location_details[0]] =[int(location_details[1]),int(location_details[2])] 
    #print(location_dict)
    x = int(input_data_list[0])
    print(f"number of Locations is {x}")
    print(f"Start {start} and destination is {destination}")
    print(f"Hyperloop Locations is {hyperloop_locations}")


    hyperloop_loc_dict[hyperloop_locations[0]] =  location_dict[hyperloop_locations[0]]
    hyperloop_loc_dict[hyperloop_locations[1]] =  location_dict[hyperloop_locations[1]]

    close_start_location = closestLocation(location_dict[start],hyperloop_loc_dict)
    close_end_location = closestLocation(location_dict[destination],hyperloop_loc_dict)

    if start in hyperloop_locations:
        start_drive_time = -1
    else:
        start_drive_time = drivetime(location_dict[start],close_start_location)
    
    if destination in hyperloop_locations:
        des_drive_time = -1
    else:
        des_drive_time = drivetime(location_dict[destination],close_end_location)

    hyper_time = hyperlooptime(location_dict[hyperloop_locations[0]],location_dict[hyperloop_locations[1]])

    total_time = round(start_drive_time + hyper_time + des_drive_time)
    
    print(f"start Time is {start_drive_time}")
    print(f"hyper Time is {hyper_time}")
    print(f"des Time is {des_drive_time}")
    print(f"Travel Time is {total_time}")
    # write results
    #output_file.write("{}".format(hyper_time))

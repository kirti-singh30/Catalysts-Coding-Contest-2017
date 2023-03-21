
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
    return locations[max_idx],max_idx

def sortest_drive_time(hyperloop_locations,location_dict,loc):

    hyperloop_loc_dict = {}
    hyperloop_loc_dict[hyperloop_locations[0]] =  location_dict[hyperloop_locations[0]]
    hyperloop_loc_dict[hyperloop_locations[1]] =  location_dict[hyperloop_locations[1]]

    close_location,max_idx = closestLocation(location_dict[loc],hyperloop_loc_dict)
    print(close_location)

    if loc in hyperloop_locations:
        drive_time = -1
    else:
        drive_time = drivetime(location_dict[loc],close_location)
    return drive_time,max_idx


def total_drive_time(hyperloop_locations,location_dict,start,des):

    start_drive_time,start_close = sortest_drive_time(hyperloop_locations,location_dict,start)
    des_drive_time,des_close = sortest_drive_time(hyperloop_locations,location_dict,des)
    if len(hyperloop_locations)>2:
        index_1 = [i for i, val in enumerate(hyperloop_locations) if val == 'start_close']
        index_2 = [i for i, val in enumerate(hyperloop_locations) if val == 'des_close']
        if index_1<index_2:
            def_locs = hyperloop_locations[index_2:index_1+1]
            for idx,locs in enumerate(def_locs):

                hyper_time +=  hyperlooptime(location_dict[locs],location_dict[hyperloop_locations[idx+1])
    else:
        hyper_time = hyperlooptime(location_dict[start_close],location_dict[des_close])
    total_time = round(start_drive_time + hyper_time + des_drive_time)

    print(f"start Time is {start_drive_time}")
    print(f"hyper Time is {hyper_time}")
    print(f"des Time is {des_drive_time}")
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

def  benefincal(location_dict,journey_dict, hyper) :
    counter = 0
    for _,value in journey_dict.items() :
        start = value["loc1"]
        des = value["loc2"]
        tH = total_drive_time(hyper,location_dict,start,des )
        if (tH < value["time"]) :
            counter += 1
    return counter

def find_hyperloop_sts(location_dict, journey_dict,  target) :
    for stop1,value in location_dict.items() :
        for stop2,value in location_dict.items() :
            if (stop1==stop2) :
                continue
            else :
                hyper = [stop1, stop2]
                if (benefincal(location_dict,journey_dict, hyper) >= target) :
                    return hyper[0] + " " + hyper[1]

if __name__ == "__main__":

    args = sys.argv

    # read the input and output files
    with open(sys.argv[1], 'r') as f:
        input_data = f.read()
    input_data = input_data.rstrip()
    input_data_list = input_data.split('\n')
    # now extract the locations and coordinates
    no_hloops = input_data_list[-1].split(" ")[0]
    hloops_stops = input_data_list[-1].split(" ")[1:]
    number_locs = int(input_data_list[0])
    start,des = input_data_list[-2].split(" ")[0],input_data_list[-2].split(" ")[1]
    print(f"Hyperloop Locations are {hloops_stops}")
    print(f"Start and des is {start}, {des}")
    location_dict = {}
    for locations in input_data_list[1:number_locs+1]:
        location_details = locations.split(" ")
        location_dict[location_details[0]] =[int(location_details[1]),int(location_details[2])] 
    
    j_time = total_drive_time(hloops_stops,location_dict,start,des)
    print(j_time)

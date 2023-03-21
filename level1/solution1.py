
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
    location_dict = {}
    for locations in input_data_list[1:-1]:
        location_details = locations.split(" ")
        location_dict[location_details[0]] =[int(location_details[1]),int(location_details[2])] 
    #print(location_dict)
    x = int(input_data_list[0])
    print(f"number of Locations is {x}")
    print(f"Hyperloop Locations is {hyperloop_locations}")

    hyper_time = hyperlooptime(location_dict[hyperloop_locations[0]],location_dict[hyperloop_locations[1]])
    
    print(f"Travel Time is {hyper_time}")
    # write results
    #output_file.write("{}".format(hyper_time))

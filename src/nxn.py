import numpy


def nxn(image):
    """
    takes in a labeled image in an array and returns an array of nxn 
    """
    minX = [999999] * 21
    minY = [999999] * 21
    maxX = [-1] * 21
    maxY = [-1] * 21


    for x in range(0,len(image)):
        for y in range(0,len(image[0])):
            value = int(image[x][y])
            if(value):
                if(minX[value] > x):
                    minX[value] = x
                if(minY[value] > y):
                    minY[value] = y
                if(maxX[value] < x):
                    maxX[value] = x
                if(maxY[value] < y):
                    maxY[value] = y
    for z in range(0,21):
        if(minX[z] != 999999):
            delX = maxX[z] - minX[z]
            delY = maxY[z] - minY[z]

            if(delX < delY):
                while(delY != delX):
                    if(minX[z] != 0):
                        minX[z]-=1
                        delX+=1
                    if(maxX[z] < len(image) && delY != delX):
                        maxX[z]+=1 
                        delX+=1
            elif(delY > delX):
                while(delX != delY):
                    if(minX[z] != 0):
                        minX[z]-=1
                        delX+=1
                    if(maxX[z] < len(image) && delY != delX):
                        maxX[z]+=1 
                        delX+=1
    return 




if(__name__ == "__main__"):
    import csv
    reader = csv.reader(open("foo.csv", "rb"), delimiter=",")
    x = list(reader)
    result = numpy.array(x).astype("float")
    nxn(result)

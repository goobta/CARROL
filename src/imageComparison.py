import cv2



def similiarityConfidence(original,new,disp):
   
    """
    Algorithm modified from: https://pysource.com/2018/07/20/find-similarities-between-two-images-with-opencv-and-python/
    work in progress    

    """
    sift = cv2.xfeatures.SIFT_create()
    
    kp_o,desc_o = sift.detectAndComput(original,None)
    kp_n,desc_n = sift.detectAndComput(new,None)

    index_params = dict(algorithm=0, trees=5)
    search_params = dict()
    flann = cv2.FlannBasedMatcher(index_params,search_params)

    matches = flann.knnMatch(desc_1, desc_2, k=2)


    if(disp):
        good_points = []
        ratio = 0.6
        for m, n in matches:
            if m.distance < ratio*n.distance:
                good_points.append(m)
        print(len(good_points))
     
        result = cv2.drawMatches(original, kp_1, image_to_compare, kp_2, good_points, None)
        cv2.imshow("result", result)
        cv2.imshow("Original", original)
        cv2.imshow("Duplicate", image_to_compare)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    count = 0
    total = 0
    for m,n in matches:
        if(m.distance < ratio*n.distance):
            count+=1
        total+=1
    print(str(total) +"," + str(count))
    return total,count


if __name__ == "__main__":
    
    #similiarityConfidence("../datasets/cow/cow00001.png","../datasets/cow/cow00002.png",1)
    

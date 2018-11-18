#ffmpeg -ss 0:00 -i greypass003.mp4 greypass%05d.png

from subprocess import call


def mp4ToDataset(mp4path, dataSetDir,name):
    """
    Creates images named name0.png to nameN.png, where N is the number of frames in mp4Path. 
    Puts the images in dataSetDir

    Example call:
    mp4ToDataset("greypass003.mp4","temp", "gp")
    """
    call(["ffmpeg","-ss","0:00","-i",mp4path,dataSetDir + "/" +name + "%05d.png"])




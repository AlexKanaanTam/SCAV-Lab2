import os
import subprocess


def ex3():

    # Ex 3 lab 2
    resX = input("ResX: ")
    resY = input("ResY: ")
    scale = ('scale='+str(resX)+':'+str(resY))

    subprocess.call(['ffmpeg', '-i', 'bbb_cut.mp4', '-vf',
                    scale, ' newvideo.mp4', ])


if __name__ == "__main__":

    ex3()

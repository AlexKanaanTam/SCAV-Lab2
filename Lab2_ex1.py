import os


def ex1():

    # Ex 1 lab 2
    os.system("ffprobe -v error -select_streams v:0 -show_entries \
            stream=width,height -of csv=s=x:p=0 bbb_cut.mp4")
    os.system("ffprobe -v error -select_streams v:0 -show_entries \
            stream=codec_name -of default=noprint_wrappers=1:nokey=1 \
            bbb_cut.mp4")
    os.system("ffprobe -v error -select_streams v:0 -show_entries \
            stream=nb_frames -of default=noprint_wrappers=1:nokey=1 \
            bbb_cut.mp4")


if __name__ == "__main__":

    ex1()

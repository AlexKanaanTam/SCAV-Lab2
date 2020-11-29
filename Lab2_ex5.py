import numpy as np
import matplotlib.pyplot as plt
import os


# def menu()


menu = True

while menu:
    opt = input('Puede escoger del 1 al 4 para indicar el ejercicio \
         o el 5 para salir. Introduzca un valor: ')
    # Ejercicio 1
    if(opt == 1):
        os.system("ffprobe -v error -select_streams v:0 -show_entries \
            stream= width, height -of csv=s=x:p=0 bbb_cut.mp4")

        os.system("ffprobe -v error -select_streams v:0 -show_entries \
            stream=codec_name -of default_wrappers=1:nokey=1 bbb_cut.mp4")

        os.system("ffprobe -v error -select_streams v:0 -show_entries \
            stream=nb_frames -of default_wrappers=1:nokey=1 bbb_cut.mp4")

    # Ejercicio 2
    if(opt == 2):
        os.rename("bbb_cut.mp4", "720p_res")
        os.rename("bbb_cut.mp4", "480_res")
        os.rename("bbb_cut.mp4", "360x240_res")
        os.rename("bbb_cut.mp4", "160x120_res")

    # Ejercicio 3
        if(opt == 3):
            x_res = input("X resolution: ")
            y_res = input("Y resolution: ")

            scale = ('New scale is =' + str(x_res) + ':'+str(y_res))

            subprocess.call(['ffmpeg', '-i', 'bbb_cut.mp4', scale,
                            'new_video.mp4'])

    # Ejercicio 4
        if(opt == 4):
            os.system("ffmpeg -i bbb_cut.mp4 transcoded_bbb.mov")

    # EXIT
        if(opt == 5):
            menu = False
            break


if __name__ == "__main__":

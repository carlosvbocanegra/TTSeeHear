#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from SeeHearMusic import SeeHearMusic
import SeeHearP3

parser = argparse.ArgumentParser(
    description='Generates a melodic representation of an image based on features and emotional content')
parser.add_argument('-i', '--image', help='name of the image file',
    required=True, type=str)
parser.add_argument('-e', '--emotion', help='result from the preprocessing of the neural network',
    required=True, type=str)
parser.add_argument('-o', '--instrumentopt', help='0=all instruments, 1=no chords, 2=just piano',
    required=True, type=int)

def getMode(emotion):
    if emotion == 'Admiracion':
        mode = 4
    if emotion == 'Extasis':
        mode = 0
    if emotion == 'Melancolia':
        mode = 5
    if emotion == 'Enfado':
        mode = 6
    if emotion == 'Aprobacion':
        mode = 0
    if emotion == 'Tedio':
        mode = 6
    # if emotion == 'Asombro':
    #     mode =
    if emotion == 'Terror':
        mode = 2
    if emotion == 'Alegría':
        mode = 3
    if emotion == 'Optimismo':
        mode = 0
    if emotion == 'Anticipacion':
        mode = 1
    if emotion == 'Aversion':
        mode = 6
    if emotion == 'Serenidad':
        mode = 0
    if emotion == 'Vigilancia':
        mode = 1
    # if emotion == 'Sorpresa':
    #     mode =
    if emotion == 'Interes':
        mode = 1
    if emotion == 'Confianza':
        mode = 4
    if emotion == 'Sumision':
        mode = 5
    if emotion == 'Amor':
        mode = 0
    return mode

if __name__ == '__main__':
    args = parser.parse_args()
    imageFileName = args.image
    emotion = args.emotion
    instropt = args.instrumentopt

    print imageFileName
    print emotion
    print instropt

    im = SeeHearP3.getImageData(imageFileName)
    name = imageFileName[0:-4]
    mode = getMode(emotion)
    shmusic = SeeHearMusic(im, mode, name, instropt)
    shmusic.createMusic()
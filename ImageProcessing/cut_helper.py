import csv
import cv2

def cut_image(csvfilename,imagefilename):
    mImg = None
    lImg = None
    mImgScore = 0
    with open(csvfilename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[-1] != "dog":continue
            score = float(row[-2])
            if score < mImgScore: continue
            mImgScore = score
            imagename=row[0]
            xmin=int(row[4])
            xmax=int(row[5])
            ymin=int(row[6])
            ymax=int(row[7])
            #print row
            img = cv2.imread(imagefilename)
            lImg = img
            roi = img[ymin:ymax,xmin:xmax]
            mImg = roi
    return mImg
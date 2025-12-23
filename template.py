import cv2
import numpy as np

temp = cv2.imread(r"C:\Users\soban\Downloads\new.jpg")
org = cv2.imread(r"C:\Users\soban\Downloads\IMG-20240626-WA0186.jpg")

gry = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
gry1 = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)

w, h = gry.shape[::-1]
res = cv2.matchTemplate(gry1, gry, cv2.TM_CCORR_NORMED)

thr = 0.99

l = np.where(res >= thr)

for i in zip(*l[::-1]):
    cv2.rectangle(org, i, (i[0]+w, i[1]+h), (0, 255, 0), 0)

org = cv2.resize(org, (600, 500))
cv2.imshow('image', org)
temp = cv2.resize(temp, (200, 200))
cv2.imshow('to be found', temp)
cv2.waitKey(0)
cv2.destroyAllWindows()

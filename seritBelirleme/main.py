import cv2
import numpy as np

img = cv2.imread("h_line.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 75, 150) # kenarları saptıyoruz. 75 ve 150 değiştirilebilir.

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=200) #burda da kenarları saptıyoruz fakar bu çok önemli bir
# algoritmadır. şeritlerde ki bulunan boşlkları dolduruyor.
# ilk değer canny den gelen resmi alır, 1 yaz, np.pi/180 yaz, thresh değeridir eğer bazı kenarları almazsa değerini değiştir.
#son parametre ise boşlukları dolduran kısımdır. ilk 50 değerini verdik lineler kısa geldi ondan 200 değeri verdik daha da verebilriz.

# line 4 değer döndürür. x1,y1,x2,y2 değerleri, çizgilerin başlangıç ve bitiş koordinatlarıdır.

for line in lines:
    x1, y1, x2, y2 = line[0] # her line'nin başlangıç ve bitiş koordinatlarını alıyoruz
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2) # ve çizgi çekiyoruz.

cv2.imshow("gray", gray)
cv2.imshow("hough", edges)
cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
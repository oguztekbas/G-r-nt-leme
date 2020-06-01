import cv2
import numpy as np
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)


servoIleriGeri = GPIO.PWM(12,50)
servoAsagiYukari = GPIO.PWM(13,50)
servoKiskac = GPIO.PWM(16,50)
servoGovde = GPIO.PWM(11,50)

def asagiYukari(aci):
  
    servoAsagiYukari.ChangeDutyCycle(8.5-aci/180.0*5) 
   
def ileriGeri(aci):

    servoIleriGeri.ChangeDutyCycle(5.5+aci/180.0*5)
    
    
def kiskac(aci):

    servoKiskac.ChangeDutyCycle(5.4+aci/180.0*5)
    
def govde(aci):

    servoGovde.ChangeDutyCycle(6.5+aci/180.0*5)



kamera = cv2.VideoCapture(0)



dusuk_sari = np.array([22,50,100])  
yuksek_sari = np.array([32,255,255]) 

dusuk_yesil = np.array([42,100,100])  
yuksek_yesil = np.array([70,255,255])

dusuk_mavi = np.array([85,100,100])
yuksek_mavi = np.array([125,255,255])






sari = False
yesil = False
mavi = False

i = 0

while i < 1 :
    
    
    
    ret,goruntu = kamera.read()
    goruntu = goruntu[100:440,80:300]
    hsv = cv2.cvtColor(goruntu,cv2.COLOR_BGR2HSV)
    
    
    
    mask = cv2.inRange(hsv,dusuk_mavi,yuksek_mavi)
    
    
    for x in range(0,mask.shape[0]):
        for y in range(0,mask.shape[1]):
            if mask[x,y] == 255:
                mavi = True
                break
               
    
    mask1 = cv2.inRange(hsv,dusuk_sari,yuksek_sari)        
    
    for x in range(0,mask1.shape[0]):
        for y in range(0,mask1.shape[1]):
            if mask1[x,y] == 255:
               sari = True
               break
    
    mask2 = cv2.inRange(hsv,dusuk_yesil,yuksek_yesil)        
    
    for x in range(0,mask2.shape[0]):
        for y in range(0,mask2.shape[1]):
            if mask2[x,y] == 255:
               yesil = True
               break
            
    
           
            
    if sari == True:
        print("SARI")
        
        servoKiskac.start(5.4)
        time.sleep(0.5)
        servoIleriGeri.start(5.5)
        time.sleep(0.5)
        servoAsagiYukari.start(8.5)
        time.sleep(0.5)
        servoGovde.start(6.5)
        time.sleep(0.5)
        
        for i in range(80):
            kiskac(i)
            time.sleep(0.01)      # KISKAC AÇILDI.
    
    
        time.sleep(0.5)
        
        for i in range(90):
            ileriGeri(i)            #İleri gitti.
            time.sleep(0.01)
    
        time.sleep(0.5)        
    
        for i in range(75):
            asagiYukari(i)       #Asagi indi.
            time.sleep(0.01)
    
        time.sleep(0.5)
    
        for i in range(80):         #kiskaci kapatti.
            kiskac(80-i)
            time.sleep(0.01)
        
        time.sleep(0.5)

        for i in range(90):
            ileriGeri(90-i)            #GERİi gitti.
            time.sleep(0.01)
    
        time.sleep(0.5)        
        
        for i in range(75):
            asagiYukari(75-i)       #Yukarı Çıktı
            time.sleep(0.01)
    
        time.sleep(0.5)
    
        for i in range(80):         #govde dondu.
            govde(i)
            time.sleep(0.01)
        
        time.sleep(0.5)

        for i in range(80):
            kiskac(i)
            time.sleep(0.01)      # KISKAC AÇILDI.
    
        time.sleep(0.5)

        for i in range(80):         #kiskaci kapatti.
            kiskac(80-i)
            time.sleep(0.01)
        
        time.sleep(0.5)

        for i in range(80):         #govde geri dondu.
            govde(80-i)
            time.sleep(0.01)
        
   
        servoKiskac.stop()
   
    
        servoIleriGeri.stop()
   
   
        servoAsagiYukari.stop()

    
        servoGovde.stop()
        
    if mavi == True:
        print("MAVİ")
        
        servoKiskac.start(5.4)
        time.sleep(0.5)
        servoIleriGeri.start(5.5)
        time.sleep(0.5)
        servoAsagiYukari.start(8.5)
        time.sleep(0.5)
        servoGovde.start(6.5)
        time.sleep(0.5)
        
        for i in range(80):
            kiskac(i)
            time.sleep(0.01)      # KISKAC AÇILDI.
    
    
        time.sleep(0.5)
        
        for i in range(90):
            ileriGeri(i)            #İleri gitti.
            time.sleep(0.01)
    
        time.sleep(0.5)        
    
        for i in range(75):
            asagiYukari(i)       #Asagi indi.
            time.sleep(0.01)
    
        time.sleep(0.5)
    
        for i in range(80):         #kiskaci kapatti.
            kiskac(80-i)
            time.sleep(0.01)
        
        time.sleep(0.5)

        for i in range(90):
            ileriGeri(90-i)            #GERİi gitti.
            time.sleep(0.01)
    
        time.sleep(0.5)        
        
        for i in range(75):
            asagiYukari(75-i)       #Yukarı Çıktı
            time.sleep(0.01)
    
        time.sleep(0.5)
    
        for i in range(115):         #govde dondu.
            govde(i)
            time.sleep(0.01)
        
        time.sleep(0.5)

        for i in range(80):
            kiskac(i)
            time.sleep(0.01)      # KISKAC AÇILDI.
    
        time.sleep(0.5)

        for i in range(80):         #kiskaci kapatti.
            kiskac(80-i)
            time.sleep(0.01)
        
        time.sleep(0.5)

        for i in range(115):         #govde geri dondu.
            govde(115-i)
            time.sleep(0.01)
        
   
        servoKiskac.stop()
   
    
        servoIleriGeri.stop()
   
   
        servoAsagiYukari.stop()

    
        servoGovde.stop()
        
   
    if yesil == True:
        print("YEŞİL")
        
        servoKiskac.start(5.4)
        time.sleep(0.5)
        servoIleriGeri.start(5.5)
        time.sleep(0.5)
        servoAsagiYukari.start(8.5)
        time.sleep(0.5)
        servoGovde.start(6.5)
        time.sleep(0.5)
        
        for i in range(80):
            kiskac(i)
            time.sleep(0.01)      # KISKAC AÇILDI.
    
    
        time.sleep(0.5)
        
        for i in range(90):
            ileriGeri(i)            #İleri gitti.
            time.sleep(0.01)
    
        time.sleep(0.5)        
    
        for i in range(75):
            asagiYukari(i)       #Asagi indi.
            time.sleep(0.01)
    
        time.sleep(0.5)
    
        for i in range(80):         #kiskaci kapatti.
            kiskac(80-i)
            time.sleep(0.01)
        
        time.sleep(0.5)

        for i in range(90):
            ileriGeri(90-i)            #GERİi gitti.
            time.sleep(0.01)
    
        time.sleep(0.5)        
        
        for i in range(75):
            asagiYukari(75-i)       #Yukarı Çıktı
            time.sleep(0.01)
    
        time.sleep(0.5)
    
        for i in range(150):         #govde dondu.
            govde(i)
            time.sleep(0.01)
        
        time.sleep(0.5)

        for i in range(80):
            kiskac(i)
            time.sleep(0.01)      # KISKAC AÇILDI.
    
        time.sleep(0.5)

        for i in range(80):         #kiskaci kapatti.
            kiskac(80-i)
            time.sleep(0.01)
        
        time.sleep(0.5)

        for i in range(150):         #govde geri dondu.
            govde(150-i)
            time.sleep(0.01)
        
   
        servoKiskac.stop()
   
    
        servoIleriGeri.stop()
   
   
        servoAsagiYukari.stop()

    
        servoGovde.stop()
        
   
        
               
    cv2.imshow("Orjinal Foto",goruntu)
    cv2.imshow("Mavi",mask)
    cv2.imshow("Sarı",mask1)
    cv2.imshow("Yesil",mask2)
    
    
    if cv2.waitKey(1500) & 0xFF == ord('q'):
        break
    
    i = i + 1
    
    
kamera.release()





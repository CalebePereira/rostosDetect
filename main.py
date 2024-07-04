import cv2 #controlar a webcam (opencv) (trabalhar com imgs)
import mediapipe as mp #biblioteca do google que implementa o reconhecimento de img

index = 0
arr = []
i = 10
while i > 0: #verificar a disponibilidade de webcam
    cap = cv2.VideoCapture(index) #o indice representa a webcam
    if cap.read()[0]:
        arr.append(index)
        cap.release()
    index += 1
    i -= 1
print("Dispositivos de captura disponíveis: ", arr) #mostrar todos indices disponiveis

#conectar na webcam
webcam = cv2.VideoCapture(0)
if not webcam.isOpened(): #verificar se conseguiu abrir a webcam
    print("Erro ao abrir a webcam")
    exit()


#reconhecimento de rosto
solucao_reconhecimento = mp.solutions.face_detection
reconhecimento = solucao_reconhecimento.FaceDetection()
desenho = mp.solutions.drawing_utils

#video: conjunto de frames(fotos)
#andar nos frames
while True:
  #ler informacoes da webcam
  verificador, frame  = webcam.read() #2 retornos (se conseguir ler, a img)

  if not verificador: #se n conseguiu ler a img
    break
  #reconhecer os rostos dentro do frame
  lista_rostos = reconhecimento.process(frame) #processa a img para verificar se dentro do frame tem algum rosto

  if lista_rostos.detections: #verifica os rostos
    for rosto in lista_rostos.detections:
      #para cada rosto desenhar as linhas
      desenho.draw_detection(frame, rosto) #dentro da propria img desenhar o rosto

  cv2.imshow("Rostos", frame) #exibir a janela da webcam
  #parar o loop quando apertar ESC
  if cv2.waitKey(5) == 27: #aguardar 5 miliseg na execucao e se apertar a tecla de codigo 27 (ESC), ele vai parar ou usar funcao ord('a') (passando a tecla na func)
    break

webcam.release() #desligar a webcam
cv2.destroyAllWindows()


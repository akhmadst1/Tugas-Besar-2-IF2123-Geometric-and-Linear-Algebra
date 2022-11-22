import cv2
capture = cv2.VideoCapture(0)
ret, frame = capture.read()
cv2.imwrite(r"..\Algeo02-21115\test\dataset_test\test.jpg", frame)
capture.release()
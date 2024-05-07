# week9
  
1. **摄像头视频帧读取**：使用OpenCV库中的`VideoCapture`类从摄像头读取实时视频帧。
```cap = cv2.VideoCapture(0) # 0表示默认摄像头，如果有多个摄像头，可以尝试不同索引值 while True: ret, frame = cap.read() # 读取视频帧 if not ret: break # 如果无法读取帧，退出循环 cv2.imshow('Video Frame', frame) # 显示视频帧 if cv2.waitKey(1) & 0xFF == ord('q'): break # 按下'q'键退出循环 cap.release() # 释放摄像头 cv2.destroyAllWindows() # 关闭所有窗口```

  


2. **图像预处理**：对每一帧进行预处理，包括去噪、图像增强和边缘检测。 
 ```while True: ret, frame = cap.read() # 读取视频帧 if not ret: break # 预处理步骤 # 1. 去噪处理 frame = cv2.GaussianBlur(frame, (5, 5), 0) # 使用高斯模糊去除噪声 # 2. 图像增强 frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 转换为灰度图像 # 3. 边缘检测 edges = cv2.Canny(frame, 100, 200) # 使用Canny边缘检测算法 # 显示处理后的图像 cv2.imshow('Processed Frame', edges)```
3.  **查找四边形轮廓**：在处理后的图像中查找四边形轮廓，并标记四个角点和中心点。
```# 寻找轮廓 contours, _ = cv2.findContours(processed_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # 遍历找到的轮廓 for contour in contours: # 近似轮廓为四边形 epsilon = 0.04 * cv2.arcLength(contour, True) approx = cv2.approxPolyDP(contour, epsilon, True) if len(approx) == 4: # 绘制四边形轮廓 cv2.drawContours(processed_frame, [approx], 0, (255, 255, 255), 2) # 标记四个角点和中心点 for point in approx: x, y = point.ravel() cv2.circle(processed_frame, (x, y), 5, (0, 0, 255), -1)```
 4. **检测红色和绿色区域**：识别图像中的红色和绿色区域，标记红色点和绿色点的位置。 
 ```# 读取图像 image = cv2.imread('image.jpg') hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # 转换为HSV颜色空间 # 定义红色和绿色的HSV范围 lower_red = np.array([0, 100, 100]) upper_red = np.array([10, 255, 255]) lower_green = np.array([40, 40, 40]) upper_green = np.array([80, 255, 255]) # 根据颜色范围创建掩模 mask_red = cv2.inRange(hsv_image, lower_red, upper_red) mask_green = cv2.inRange(hsv_image, lower_green, upper_green) # 寻找红色和绿色区域的轮廓 contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) contours_green, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # 标记红色点和绿色点的位置 for contour in contours_red: M = cv2.moments(contour) if M["m00"] != 0: cx = int(M["m10"] / M["m00"]) cy = int(M["m01"] / M["m00"]) cv2.circle(image, (cx, cy), 5, (0, 0, 255), -1) # 标记红色点 for contour in contours_green: M = cv2.moments(contour) if M["m00"] != 0: cx = int(M["m10"] / M["m00"]) cy = int(M["m01"] / M["m00"]) cv2.circle(image, (cx, cy), 5, (0, 255, 0), -1) # 标记绿色点```


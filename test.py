import cv2
import numpy as np

def preprocess_image(image):
    # 消噪
    denoised_image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
    
    # 图像增强和对比度增强
    alpha = 1.0  # 对比度增强参数
    beta = 15  # 亮度增强参数
    enhanced_image = cv2.convertScaleAbs(denoised_image, alpha=alpha, beta=beta)

    # 边缘检测
    edges = cv2.Canny(enhanced_image, 50, 150)

    return edges

def find_center_of_quadrilateral(quadrilaterals):
    for quad in quadrilaterals:
        # 计算中心点坐标
        M = cv2.moments(quad)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        
        # 绘制中心点
        cv2.circle(frame, (cx, cy), 5, (255, 255, 255), -1)
        cv2.putText(frame, f"({cx}, {cy})", (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

def find_quadrilaterals(processed_image):
    # 查找轮廓
    contours, _ = cv2.findContours(processed_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    quadrilaterals = []
    for contour in contours:
        # 计算轮廓的面积
        area = cv2.contourArea(contour)

        # 排除面积较小的轮廓
        if area > 2000:
            # 计算轮廓的周长
            perimeter = cv2.arcLength(contour, True)

            # 对轮廓进行多边形逼近
            approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

            # 如果逼近的轮廓是四边形，将其添加到列表中
            if len(approx) == 4:
                quadrilaterals.append(approx)

                # 绘制四个角点
                for point in approx:
                    x, y = point[0]
                    cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)
                    cv2.putText(frame, f"({x}, {y})", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

                # 绘制边界框
                x, y, w, h = cv2.boundingRect(approx)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return quadrilaterals

def lights_detect(image):
    # 将图像转换为HSV颜色空间
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 定义红色和绿色的HSV范围
    lower_red = np.array([165, 100, 100])
    upper_red = np.array([179, 255, 255])
    lower_green = np.array([36, 100, 100])
    upper_green = np.array([86, 255, 255])

    # 根据颜色范围创建掩模
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # 寻找红色点的轮廓
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # 寻找绿色点的轮廓
    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 遍历红色点的轮廓
    for contour in contours_red:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(image, f'Red: ({x + w // 2}, {y + h // 2})', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # 遍历绿色点的轮廓
    for contour in contours_green:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(image, f'Green: ({x + w // 2}, {y + h // 2})', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    return image

# 打开摄像头
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()  # 读取视频帧
    if not ret:
        break

    processed_frame = preprocess_image(frame)  # 预处理视频帧
    quadrilaterals = find_quadrilaterals(processed_frame)  # 查找四边形
    find_center_of_quadrilateral(quadrilaterals)  # 查找四边形中心点
    frame = lights_detect(frame)  # 检测红色和绿色区域

    cv2.imshow('Processed Frame', frame)  # 显示处理后的视频帧

    if cv2.waitKey(1) & 0xFF == ord('q'):  # 按 'q' 键退出
        break

cap.release()
cv2.destroyAllWindows()
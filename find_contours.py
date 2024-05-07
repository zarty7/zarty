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

    return quadrilaterals

# 待处理的图像
image_paths = ["image1.png", "image2.png", "image1.jpeg", "image2.jpeg", "image3.jpeg"]

# 处理多张图像
for image_path in image_paths:
    image = cv2.imread(image_path)
    processed_image = preprocess_image(image)
    quadrilaterals = find_quadrilaterals(processed_image)
    
    print(f"图像: {image_path}")
    for quad in quadrilaterals:
        print("方框的四个坐标:")
        for point in quad:
            x, y = point[0]
            print(f"({x}, {y})")
    print()
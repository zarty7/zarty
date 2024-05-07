import cv2
import numpy as np

def lights_detect(image_path):
    # 读取图像
    image = cv2.imread(image_path)

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
        print("红色点坐标:", x + w // 2, y + h // 2)

    # 遍历绿色点的轮廓
    for contour in contours_green:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(image, f'Green: ({x + w // 2}, {y + h // 2})', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        print("绿色点坐标:", x + w // 2, y + h // 2)

    # 返回图像
    return image

if __name__ == "__main__":
    image_paths = ["image1.png", "image2.png", "image1.jpeg", "image2.jpeg", "image3.jpeg"]
    
    for image_path in image_paths:
        combined_image = lights_detect(image_path)
        
        # 显示带有红色点和绿色点的图像
        cv2.namedWindow('color', cv2.WINDOW_NORMAL)
        cv2.imshow('color', combined_image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
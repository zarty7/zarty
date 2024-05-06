## 图像读取和显示：
- cv2.imread()：读取图像文件。
- cv2.imshow()：显示图像窗口。
- cv2.imwrite()：保存图像到文件。

## 图像处理：
- cv2.cvtColor()：图像颜色空间转换。
- cv2.resize()：调整图像大小。
- cv2.flip()：翻转图像。
- cv2.threshold()：图像阈值处理。
- cv2.blur()：图像模糊处理。

## 轮廓检测和形状分析：
- cv2.findContours()：检测图像中的轮廓。
- cv2.drawContours()：绘制图像中的轮廓。

## 特征检测和描述：
- cv2.Canny()：边缘检测。
- cv2.goodFeaturesToTrack()：检测图像中的角点。
- cv2.HoughLines()：检测直线。
- cv2.HoughCircles()：检测圆。

## 对象跟踪：
- cv2.VideoCapture()：打开视频文件或摄像头。
- cv2.Tracker_create()：创建对象跟踪器。

## 人脸识别和检测：
- cv2.CascadeClassifier()：创建级联分类器进行人脸检测。
- cv2.face.createLBPHFaceRecognizer()：创建LBPH人脸识别器。

## 图像转换和变换：
- cv2.warpAffine()：图像仿射变换。
- cv2.warpPerspective()：图像透视变换。

## 图像特效和增强：
- cv2.filter2D()：图像卷积滤波。
- cv2.equalizeHist()：直方图均衡化。
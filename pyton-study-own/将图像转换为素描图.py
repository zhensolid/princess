
# 和之前的图片格式转换有点类似，就是对图像进行处理。

# 以前大家可能会使用到美图秀秀，现在可能就是抖音的滤镜了。

# 其实使用Python的OpenCV，就能够快速实现很多你想要的效果。

# 图像转换
import cv2

# 读取图片
img = cv2.imread("img.jpg")
# 灰度
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey)
# 高斯滤波
blur_img = cv2.GaussianBlur(invert, (7, 7), 0)
inverse_blur = cv2.bitwise_not(blur_img)
sketch_img = cv2.divide(grey, inverse_blur, scale=256.0)
# 保存
cv2.imwrite('sketch.jpg', sketch_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# USAGE
# python compare.py

# import the necessary packages
from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

def compare_images(imageA, imageB, title):
	# compute the mean squared error and structural similarity
	# index for the images
	m = mse(imageA, imageB)
	s = ssim(imageA, imageB)

	# setup the figure
	fig = plt.figure(title)
	plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))

	# show first image
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off")

	# show the second image
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")

	# show the images
	plt.show()

# load the images -- the original, the original + contrast,
# and the original + photoshop
img1 = cv2.imread("1.jpg")
img2 = cv2.imread("2.jpg")
"""
img3 = cv2.imread("images/day/3.png")
img4 = cv2.imread("images/day/4.png")
img5 = cv2.imread("images/day/5.png")
img6 = cv2.imread("images/day/6.png")
img7 = cv2.imread("images/day/7.png")
img8 = cv2.imread("images/day/8.png")
img9 = cv2.imread("images/day/9.png")
img10 = cv2.imread("images/day/10.png")
img11 = cv2.imread("images/day/11.png")
img12 = cv2.imread("images/day/12.png")
img13 = cv2.imread("images/day/13.png")
img14 = cv2.imread("images/day/14.png")
img15 = cv2.imread("images/day/15.png")
"""
# shopped = cv2.imread("images/jp_gates_photoshopped.png")

# convert the images to grayscale
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
"""
img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)
img5 = cv2.cvtColor(img5, cv2.COLOR_BGR2GRAY)
img6 = cv2.cvtColor(img6, cv2.COLOR_BGR2GRAY)
img7 = cv2.cvtColor(img7, cv2.COLOR_BGR2GRAY)
img8 = cv2.cvtColor(img8, cv2.COLOR_BGR2GRAY)
img9 = cv2.cvtColor(img9, cv2.COLOR_BGR2GRAY)
img10 = cv2.cvtColor(img10, cv2.COLOR_BGR2GRAY)
img11 = cv2.cvtColor(img11, cv2.COLOR_BGR2GRAY)
img12 = cv2.cvtColor(img12, cv2.COLOR_BGR2GRAY)
img13 = cv2.cvtColor(img13, cv2.COLOR_BGR2GRAY)
img14 = cv2.cvtColor(img14, cv2.COLOR_BGR2GRAY)
img15 = cv2.cvtColor(img15, cv2.COLOR_BGR2GRAY)
"""

# shopped = cv2.cvtColor(shopped, cv2.COLOR_BGR2GRAY)

# initialize the figure
fig = plt.figure("Images")
images = ("img1", img1), ("img2", img2) #, ("img3", img3), ("img4", img4) , ("img5", img5), ("img6", img6) , ("img7", img7), ("img8", img8) , ("img9", img9), ("img10", img10) , ("img11", img11), ("img12", img12) , ("img13", img13), ("img14", img14) , ("img15", img15)

# loop over the images
for (i, (name, image)) in enumerate(images):
	# show the image
	ax = fig.add_subplot(1, 3, i + 1)
	ax.set_title(name)
	plt.imshow(image, cmap = plt.cm.gray)
	plt.axis("off")

# show the figure
plt.show()

# compare the images
compare_images(img1, img1, "img1 vs img1")
compare_images(img1, img2, "img1 vs img2")
"""
compare_images(img2, img3, "img2 vs img3")
compare_images(img3, img4, "img3 vs img4")
compare_images(img4, img5, "img4 vs img5")
compare_images(img5, img6, "img5 vs img6")
compare_images(img6, img7, "img6 vs img7")
compare_images(img7, img8, "img7 vs img8")
compare_images(img8, img9, "img8 vs img9")
compare_images(img9, img10, "img9 vs img10")
compare_images(img10, img11, "img10 vs img11")
compare_images(img11, img12, "img11 vs img12")
compare_images(img12, img13, "img12 vs img13")
compare_images(img13, img14, "img13 vs img14")
compare_images(img14, img15, "img14 vs img15")
"""
# compare_images(original, shopped, "Original vs. Photoshopped")

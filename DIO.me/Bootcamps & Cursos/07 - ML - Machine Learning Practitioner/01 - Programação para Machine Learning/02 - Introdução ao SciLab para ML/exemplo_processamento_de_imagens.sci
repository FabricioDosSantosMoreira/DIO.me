scicv_Init();

img = imread(getSampleImage("lena.jpg"));
matplot(img);

img_gray = imread(getSampleImage("lena.jpg"), CV_LOAD_IMAGE_GRAYSCALE);
matplot(img_gray);

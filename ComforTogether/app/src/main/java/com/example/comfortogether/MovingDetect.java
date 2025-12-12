package com.example.comfortogether;

import android.graphics.Bitmap;

import androidx.annotation.NonNull;

import org.opencv.android.Utils;
import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.core.Size;
import org.opencv.imgproc.Imgproc;

public class MovingDetect {
    private double threshold;
    private int    difference = 40;
    private Bitmap oldImg1 = null;
    private Bitmap oldImg2 = null;

    public MovingDetect(double threshold) {
        this.threshold = threshold;
    }

    public double getThreshold() {
        return threshold;
    }

    public void setThreshold(double threshold) {
        this.threshold = threshold;
    }

    public int getDifference() {
        return difference;
    }

    public void setDifference(int difference) {
        this.difference = difference;
    }

    /**
     * Function for detecting moving of frame
     * @param image Bitmap image
     * @return is Frame moving
     */
    public boolean MovingOfFrame(@NonNull Bitmap image) {
        Mat oldFrame1 = new Mat();
        Mat oldFrame2 = new Mat();
        Mat nowFrame  = new Mat();
        Utils.bitmapToMat(image, nowFrame);

        // 비교를 위해 최소 3장 이상의 프레임이 필요하기 때문에,
        // 3장이 쌓일 때 까지 저장만 진행
        if (this.oldImg1 == null) {
            this.oldImg1 = image;
            return false;
        } else if (this.oldImg2 == null) {
            this.oldImg2 = image;
            return false;
        }

        Utils.bitmapToMat(this.oldImg1, oldFrame1);
        Utils.bitmapToMat(this.oldImg2, oldFrame2);

        // 현재 이미지 컬러 컨버팅
        Imgproc.cvtColor(oldFrame1, oldFrame1, Imgproc.COLOR_BGR2GRAY);
        Imgproc.cvtColor(oldFrame2, oldFrame2, Imgproc.COLOR_BGR2GRAY);
        Imgproc.cvtColor(nowFrame, nowFrame, Imgproc.COLOR_BGR2GRAY);

        Mat diff_12 = new Mat();
        Mat diff_23 = new Mat();
        Mat diff    = new Mat();
        Mat kernel  = new Mat();

        // 각 프레임 별 차이값 구함
        Core.absdiff(oldFrame1, oldFrame2, diff_12);
        Core.absdiff(oldFrame2, nowFrame,  diff_23);

        Imgproc.threshold(diff_12, diff_12, this.threshold, 255, Imgproc.THRESH_BINARY);
        Imgproc.threshold(diff_23, diff_23, this.threshold, 255, Imgproc.THRESH_BINARY);

        Core.bitwise_and(diff_12, diff_23, diff);

        Imgproc.getStructuringElement(Imgproc.MORPH_CROSS, new Size(3, 3));
        Imgproc.morphologyEx(diff, diff, Imgproc.MORPH_OPEN, kernel);

        int     diff_cnt    = Core.countNonZero(diff);
        boolean isDetecting = diff_cnt > this.difference;

        this.oldImg1 = this.oldImg2;
        this.oldImg2 = image;

        return isDetecting;
    }
}

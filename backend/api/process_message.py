import cv2

def encodeEmotionsInBytes(recv_emotions):
    """Convertes Emotion data in bytes"""
    if len(recv_emotions)==0:
        return ""
    seprator="&"
    response_data=recv_emotions[0].convertInResponse()
    for j in range(1,len(recv_emotions)):
        response_data+=seprator+recv_emotions[j].convertInResponse()
    return response_data
    
def convertInImage(data,height,width):
    """COnvert data to image"""
    imgH=int(height.decode("utf-8"),16)
    imgW=int(width.decode("utf-8"),16)
    #int(img_height.decode("utf-8"),16)
    print(len(data)," ",imgH,"  ",imgW)
    img1 = cv2.imread("a.jpg")
    return img1

"""
const shift = (0xFF << 24);
Future<Image> convertYUV420toImageColor(CameraImage image) async {
      try {
        final int width = image.width;
        final int height = image.height;
        final int uvRowStride = image.planes[1].bytesPerRow;
        final int uvPixelStride = image.planes[1].bytesPerPixel;

        print("uvRowStride: " + uvRowStride.toString());
        print("uvPixelStride: " + uvPixelStride.toString());

        // imgLib -> Image package from https://pub.dartlang.org/packages/image
        var img = imglib.Image(width, height); // Create Image buffer

        // Fill image buffer with plane[0] from YUV420_888
        for(int x=0; x < width; x++) {
          for(int y=0; y < height; y++) {
            final int uvIndex = uvPixelStride * (x/2).floor() + uvRowStride*(y/2).floor();
            final int index = y * width + x;

            final yp = image.planes[0].bytes[index];
            final up = image.planes[1].bytes[uvIndex];
            final vp = image.planes[2].bytes[uvIndex];
            // Calculate pixel color
            int r = (yp + vp * 1436 / 1024 - 179).round().clamp(0, 255);
            int g = (yp - up * 46549 / 131072 + 44 -vp * 93604 / 131072 + 91).round().clamp(0, 255);
            int b = (yp + up * 1814 / 1024 - 227).round().clamp(0, 255);     
            // color: 0x FF  FF  FF  FF 
            //           A   B   G   R
            img.data[index] = shift | (b << 16) | (g << 8) | r;
          }
        }

        imglib.PngEncoder pngEncoder = new imglib.PngEncoder(level: 0, filter: 0);
        List<int> png = pngEncoder.encodeImage(img);
        muteYUVProcessing = false;
        return Image.memory(png);  
      } catch (e) {
        print(">>>>>>>>>>>> ERROR:" + e.toString());
      }
      return null;
  }

"""
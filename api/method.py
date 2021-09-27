import urllib

def GenerateQRCode(url,port,wantToView=True):    
    """ Generates QRCode.

        if wantToView==True:     it only show QR code on display.

        else        return image format of QRcode. 
    """
    import qrcode
    qr = qrcode.QRCode( version=1,  box_size=10,border=5)
    qr.add_data(url+"&&%d"%port)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='pink')
    import matplotlib.pyplot as plt
    if wantToView:  
         plt.imshow(img)
         plt.show()
    else:
        return img


def GetIp():
    """ Return IP of your machine.

        Return (Local_ip ,External_ip)
    """
    import urllib.request
    import socket
    external_ip=urllib.request.urlopen("https://ident.me").read().decode('utf8')
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    local_ip=s.getsockname()[0]
    s.close()
    return (local_ip,external_ip)


if __name__=='__main__':
    ip=GetIp()
    GenerateQRCode(ip[0],5500)
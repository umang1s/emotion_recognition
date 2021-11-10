
def GenerateQRCode(url,port):    
    """ Generates QRCode.

        if wantToView==True:     it only show QR code on display.

        else        return image format of QRcode. 
    """
    import qrcode
    import json
    data={"IP":url,"PORT":port}
    with open("qr_code.json","w") as f:
        json.dump(data,f)
    qr = qrcode.QRCode( version=1,  box_size=10,border=5)
    qr.add_data(url+"&&%d"%port)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='pink')
    img.save("qr_code.png")


def GetIp():
    """ Return IP of your machine.

        Return (Local_ip ,External_ip)
    """
    import socket
    #import urllib.request
    #external_ip=urllib.request.urlopen("https://ident.me").read().decode('utf8')
    external_ip="abc"
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    local_ip=s.getsockname()[0]
    s.close()
    return (local_ip,external_ip)


def on_button_pressed_b():
    global a, b, c, d, ssid, pw
    serial.redirect_to_usb()
    serial.write_line("click b")
    serial.redirect(SerialPin.P0, SerialPin.P1, BaudRate.BAUD_RATE115200)
    serial.write_string("AT" + "\r\n")
    basic.pause(500)
    a = serial.read_until(serial.delimiters(Delimiters.CARRIAGE_RETURN))
    b = serial.read_until(serial.delimiters(Delimiters.CARRIAGE_RETURN))
    c = serial.read_until(serial.delimiters(Delimiters.CARRIAGE_RETURN))
    d = serial.read_until(serial.delimiters(Delimiters.CARRIAGE_RETURN))
    serial.redirect_to_usb()
    serial.write_line(a)
    serial.write_line(b)
    serial.write_line(c)
    serial.write_line(d)
    serial.redirect(SerialPin.P0, SerialPin.P1, BaudRate.BAUD_RATE115200)
    serial.write_string("AT+CWMODE=1" + "\r\n")
    basic.pause(500)
    a = serial.read_until(serial.delimiters(Delimiters.CARRIAGE_RETURN))
    b = serial.read_until(serial.delimiters(Delimiters.CARRIAGE_RETURN))
    c = serial.read_until(serial.delimiters(Delimiters.CARRIAGE_RETURN))
    d = serial.read_until(serial.delimiters(Delimiters.CARRIAGE_RETURN))
    serial.redirect_to_usb()
    serial.write_line(a)
    serial.write_line(b)
    serial.write_line(c)
    serial.write_line(d)
    serial.redirect(SerialPin.P0, SerialPin.P1, BaudRate.BAUD_RATE115200)
    serial.write_string("AT+RST" + "\r\n")
    basic.pause(5000)
    a = serial.read_until(serial.delimiters(Delimiters.CARRIAGE_RETURN))
    b = serial.read_until(serial.delimiters(Delimiters.CARRIAGE_RETURN))
    c = serial.read_until(serial.delimiters(Delimiters.CARRIAGE_RETURN))
    d = serial.read_until(serial.delimiters(Delimiters.CARRIAGE_RETURN))
    serial.redirect_to_usb()
    serial.write_line(a)
    serial.write_line(b)
    serial.write_line(c)
    serial.write_line(d)
    ssid = "WAS"
    pw = "51132079"
    serial.redirect(SerialPin.P0, SerialPin.P1, BaudRate.BAUD_RATE115200)
    serial.write_string("AT+CWJAP=\"WAS\",\"51132079\"" + "\r\n")
    basic.pause(500)
    a = serial.read_until(serial.delimiters(Delimiters.CARRIAGE_RETURN))
    b = serial.read_until(serial.delimiters(Delimiters.CARRIAGE_RETURN))
    serial.redirect_to_usb()
    serial.write_line(a)
    serial.write_line(b)
    serial.redirect(SerialPin.P0, SerialPin.P1, BaudRate.BAUD_RATE115200)
    serial.write_string("AT+CIPSTART=\"TCP\",\"52.204.34.129\",80" + "\r\n")
    basic.pause(3000)
    a = serial.read_until(serial.delimiters(Delimiters.CARRIAGE_RETURN))
    b = serial.read_until(serial.delimiters(Delimiters.CARRIAGE_RETURN))
    serial.redirect_to_usb()
    serial.write_line(a)
    serial.write_line(b)

    serial.redirect(SerialPin.P0, SerialPin.P1, BaudRate.BAUD_RATE115200)
    
    
    
    chiamata = "GET /update?api_key=" + "ZMQITLYZ39QKVOM1" + "&field1=22" 
    serial.write_string("AT+CIPSEND=" + ( len(chiamata) + 2) + "\r\n")

    serial.write_string("AT+CIPSTART=\"TCP\",\"52.204.34.129\",80" + "\r\n")
    basic.pause(3000)
    a = serial.read_until(serial.delimiters(Delimiters.CARRIAGE_RETURN))
    b = serial.read_until(serial.delimiters(Delimiters.CARRIAGE_RETURN))
    serial.redirect_to_usb()
    serial.write_line(a)
    serial.write_line(b)
    serial.write_line("fine")
input.on_button_pressed(Button.B, on_button_pressed_b)

pw = ""
ssid = ""
d = ""
c = ""
b = ""
a = ""
serial.write_line("init")
basic.show_icon(IconNames.SQUARE)
serial.write_line("provo ad inizializzare ")


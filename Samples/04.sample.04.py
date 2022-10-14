import qrcode

with open("site_list.txt", "rt", encoding="UTF8") as f:
    read_lines = f.readlines()
    
    for line in read_lines:
        line = line.strip()
        print(line)
        
        qr_data = line
        qr_image = qrcode.make(qr_data)

        qr_image.save(qr_data + ".png")
    
print(read_lines)
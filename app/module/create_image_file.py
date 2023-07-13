def writeBinaryFile(file_name, binary_data):
    with open(file_name, "wb") as file:
        file.write(binary_data)


def createImages(path, info_dict, img_dict):
    for phone, code_dict in info_dict.items():
        copy_number = 0
        for code, quantity in code_dict.items():
            img_bdata = img_dict.get(code)

            if img_bdata == None:
                print(phone)
                print(code_dict)
                continue

            for i in range(int(quantity)):
                if copy_number == 0:
                    file_name = path + "\\" + phone + ".png"
                    writeBinaryFile(file_name, img_bdata)
                    copy_number += 1
                else:
                    file_name = path + "\\" + phone + f" ({copy_number}).png"
                    writeBinaryFile(file_name, img_bdata)
                    copy_number += 1

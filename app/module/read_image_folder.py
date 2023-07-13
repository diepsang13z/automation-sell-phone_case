import os


def getImageDict(image_folder):
    """Returns a dictionary with structure {file_name : image_data}"""
    img_dict = {}

    for image_file in os.listdir(image_folder):
        if (
            image_file.endswith(".png")
            or image_file.endswith(".jpg")
            or image_file.endswith(".jpeg")
        ):
            file_name = image_file.split(".")[0]
            image_path = os.path.join(image_folder, image_file)

            with open(image_path, "rb") as image_file:
                image_data = image_file.read()
                img_dict[file_name] = image_data

    return img_dict

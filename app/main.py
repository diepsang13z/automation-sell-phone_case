from module.read_excel_file import getProductColumn, getProductDict
from module.read_image_folder import getImageDict
from module.create_image_file import createImages

excel_file = "D:\\PythonProject\\phone_case_automation_sale\\data\\b3.xlsx"
image_folder = "D:\\PythonProject\\phone_case_automation_sale\\data\\A"
output_folder = "D:\\PythonProject\\phone_case_automation_sale\\out\\testV1"


if __name__ == "__main__":
    product_column = getProductColumn(excel_file)
    product_dict = getProductDict(product_column)
    image_dict = getImageDict(image_folder)
    createImages(output_folder, product_dict, image_dict)
    # print(product_dict)
    # print(len(image_dict.values()))

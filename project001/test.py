import os
import random
import sqlite3

#Connect to the database
conn = sqlite3.connect("image_data")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM image_exchange_picture")
total_images = cursor.fetchone()[0]

random_index = random.randint(1, total_images)
cursor.execute("SELECT * FROM image_exchange_picture WHERE id=?", (random_index,))
random_image = cursor.fetchone()

conn.close()
print(random_image)
print("Random Image:")
print("ID:", random_image[0])
print("Name:", random_image[1])
print("URL:", random_image[2])
print("Tag:", random_image[3])

# # 获取图片文件夹中的所有图片路径
# images_folder = '/Users/pi/Documents/pic/test_images/'
# images = []
# for root, dirs, files in os.walk(images_folder):
#     for ff in files:
#         images.append(os.path.join(root, ff))
#
# # 批量插入图片信息到数据库中
# for image in images:
#     name = os.path.basename(image)
#     image_path = 'photos/' + name
#
#     print(image_path)
#     print(name)
#     cursor.execute("INSERT INTO image_exchange_picture (user, photo) VALUES (?, ?)", (name, image_path))

# 提交并关闭数据库连接
# conn.commit()
# conn.close()
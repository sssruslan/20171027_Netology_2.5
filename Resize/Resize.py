#Есть программа (Image Magick для Windows), которая сжимает фотографии, и есть папка «Source» 
#с самими фотографиями. Каждую фотографию мы хотим уменьшить до 200px в ширину 
#(высота меняется пропорционально). Нужно для каждой фотографии запустить программу и результат 
#работы положить в папку «Result».

#Пример (ImageMagic): convert input.jpg -resize 200 output.jpg

#Задача №3. Дополнительная (не обязательная)
#Реализовать 4 параллельных процесса и разделить фотографии между ними.

import os
import subprocess

def all_list(): # полный список файлов
    source_dir = 'Source'    
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), source_dir))
    files_list = os.listdir(path=".")
    return files_list

def ensure_dir(file_path): # проверяем есть ли уже каталог с именем Result, если нет, то создаем
    if not os.path.exists(file_path):
        os.makedirs(file_path)

def main(files_list): 
    print('Идет обработка...')
    source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Source')
    result_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Result')
    ensure_dir(result_dir)
    for i in files_list:
        input_path = os.path.join(source_dir, i)
        output_path = os.path.join(result_dir, i)
        command = 'convert ' + input_path + ' -resize 200 ' + output_path
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        subprocess.run(command) #subprocess.Popen('имя') - асинхронный запуск
    print('Готово')

main(all_list())
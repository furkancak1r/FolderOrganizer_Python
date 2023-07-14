import os
import shutil
import imghdr
import mimetypes
import errno
import stat

def handle_remove_readonly(func, path, exc):
    excvalue = exc[1]
    if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
        os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 0777
        func(path)
    else:
        raise

def organize_files():
    current_directory = os.getcwd()  # Mevcut çalışma dizinini alır
    image_folder = os.path.join(current_directory, "Resimler")  # Resimleri taşıyacak klasörün yolu
    video_folder = os.path.join(current_directory, "Videolar")  # Videoları taşıyacak klasörün yolu
    other_folder = os.path.join(current_directory, "DigerDosyalar")  # Diğer dosyaları taşıyacak klasörün yolu

    # Klasörlerin oluşturulması
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)
    if not os.path.exists(video_folder):
        os.makedirs(video_folder)
    if not os.path.exists(other_folder):
        os.makedirs(other_folder)

    # Tüm dosya ve klasörlerin taraması
    for root, dirs, files in os.walk(current_directory):
        for filename in files:
            if filename == "a.py":
                continue  # a.py dosyasını taşıma, diğer dosyalara devam et
            file_path = os.path.join(root, filename)
            if os.path.exists(file_path):  # Dosyanın varlığını kontrol et
                file_type, _ = mimetypes.guess_type(file_path)
                if file_type is not None:
                    file_type = file_type.split('/')[0]  # Dosya türünün ilk bölümünü alır (örneğin, 'image' veya 'video')
                    if file_type == 'image':
                        shutil.move(file_path, os.path.join(image_folder, filename))  # Resim dosyalarını taşır
                    elif file_type == 'video':
                        shutil.move(file_path, os.path.join(video_folder, filename))  # Video dosyalarını taşır
                    else:
                        destination_path = os.path.join(other_folder, filename)
                        if file_path != destination_path:  # Aynı dosyanın kendisini taşımamak için kontrol et
                            shutil.copy2(file_path, destination_path)  # Diğer dosyaları kopyalar
                            os.remove(file_path)  # Orijinal dosyayı siler
                else:
                    file_type = imghdr.what(file_path)
                    if file_type is not None:
                        shutil.move(file_path, os.path.join(image_folder, filename))  # Resim dosyalarını taşır
                    else:
                        destination_path = os.path.join(other_folder, filename)
                        if file_path != destination_path:  # Aynı dosyanın kendisini taşımamak için kontrol et
                            shutil.copy2(file_path, destination_path)  # Diğer dosyaları kopyalar
                            os.remove(file_path)  # Orijinal dosyayı siler

    # Boş klasörleri silme
    for root, dirs, files in os.walk(current_directory, topdown=False):
        for dir_name in dirs:
            folder_path = os.path.join(root, dir_name)
            if not os.listdir(folder_path):
                shutil.rmtree(folder_path, onerror=handle_remove_readonly)  # Klasörü ve içeriğini siler

    # İç içe geçmiş boş klasörleri silme
    for root, dirs, files in os.walk(current_directory, topdown=True):
        for dir_name in dirs:
            folder_path = os.path.join(root, dir_name)
            if not os.listdir(folder_path):
                try:
                    os.rmdir(folder_path)  # Klasörü siler
                except OSError as e:
                    handle_remove_readonly(os.rmdir,folder_path,(None,e))

    print("Dosyalar başarıyla taşındı ve boş klasörler silindi!")

organize_files()

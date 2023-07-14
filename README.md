# File Organizer

This Python script organizes files in the current working directory into separate folders based on their file type. It creates three folders: "Resimler" for image files, "Videolar" for video files, and "DigerDosyalar" for all other files. The script moves image and video files into their respective folders and copies all other files into the "DigerDosyalar" folder. After organizing the files, the script deletes any empty directories.

## Usage

To use this script, save it to the directory that you want to organize and run it using Python 3. For example, if you saved the script as `FolderOrganizer_Python`, you can run it from the command line with the following command:`FolderOrganizer_Python`

Make sure that you have the necessary permissions to move and delete files and directories in the current working directory. If you encounter a `PermissionError`, you can try running the script as an administrator or manually changing the permissions of the affected directories.

## Dependencies

This script requires Python 3 and uses the following built-in modules:
- `os`: Provides functions for interacting with the operating system.
- `shutil`: Provides functions for high-level file operations.
- `imghdr`: Determines the type of image contained in a file.
- `mimetypes`: Maps filename extensions to MIME types.

## License

This project is licensed under the the MIT License.


# Dosya Düzenleyici

Bu Python betiği, mevcut çalışma dizinindeki dosyaları dosya türlerine göre ayrı klasörlere düzenler. Üç klasör oluşturur: Resim dosyaları için "Resimler", video dosyaları için "Videolar" ve diğer tüm dosyalar için "DigerDosyalar". Betik, resim ve video dosyalarını ilgili klasörlere taşır ve diğer tüm dosyaları "DigerDosyalar" klasörüne kopyalar. Dosyaları düzenledikten sonra, betik boş dizinleri siler.

## Kullanım

Bu betiği kullanmak için, düzenlemek istediğiniz dizine kaydedin ve Python 3 ile çalıştırın. Örneğin, betiği `FolderOrganizer_Python` olarak kaydettiyseniz, komut satırından aşağıdaki komutla çalıştırabilirsiniz:`FolderOrganizer_Python`


Mevcut çalışma dizinindeki dosya ve dizinleri taşıma ve silme izinlerine sahip olduğunuzdan emin olun. `PermissionError` ile karşılaşırsanız, betiği yönetici olarak çalıştırmayı veya etkilenen dizinlerin izinlerini manuel olarak değiştirmeyi deneyebilirsiniz.

## Bağımlılıklar

Bu betik Python 3 gerektirir ve aşağıdaki yerleşik modülleri kullanır:
- `os`: İşletim sistemi ile etkileşim kurmak için fonksiyonlar sağlar.
- `shutil`: Yüksek seviyeli dosya işlemleri için fonksiyonlar sağlar.
- `imghdr`: Bir dosyada bulunan resmin türünü belirler.
- `mimetypes`: Dosya adı uzantılarını MIME türlerine eşler.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır.

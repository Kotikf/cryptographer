import pyAesCrypt
import os


class Decryption():
    def decryption(self, file, password):
        self.buffer_size = 512 * 1024

        pyAesCrypt.decryptFile(
            str(file),
            str(os.path.splitext(file)[0]), 
            password,
            self.buffer_size
        )

        print("[Файл" + str(os.path.splitext(file)[0]) + " расшифрован]")

        os.remove(file)


    def walking_by_dirs(self, dir, password):
        for name in os.listdir(dir):
            path = os.path.join(dir, name)

            if os.path.isfile(path):
                try:
                    self.decryption(path, password)
                except Exception as ex:
                    print(ex)
            else:
                self.walking_by_dirs(path, password)

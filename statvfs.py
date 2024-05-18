import os

path = "/home/cryptolis"

statvfs_result = os.statvfs(path)

print("Размер блока: ",statvfs_result.f_bsize)
print("Количество свободных блоков: ", statvfs_result.f_bfree)
print("Количесество свободных файловых узлов: ", statvfs_result.f_ffree)

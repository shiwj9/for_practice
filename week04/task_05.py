import hashlib

md5_code = hashlib.md5()
sha256_code = hashlib.sha256()
md5_code.update("Hello".encode('utf8'))
sha256_code.update("Python".encode('utf8'))
print(f'md5:{md5_code.hexdigest()}')
print(f'sha256:{sha256_code.hexdigest()}')

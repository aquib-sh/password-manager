from hashlib import md5, sha256, sha512
from typing import Union

class HashOperator:
    def __init__(self):
        pass

    def __compute(self, data: str, algorithm: Union[md5, sha256, sha512]) -> str:
        encoded_data = data.encode()
        return algorithm(encoded_data).hexdigest()

    def compute_md5(self, data: str) -> str:
        return self.__compute(data, md5) 

    def compute_sha256(self, data: str) -> str:
        return self.__compute(data, sha256) 

    def compute_sha512(self, data: str) -> str:
        return self.__compute(data, sha512) 
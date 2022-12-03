import os
import re
from datetime import datetime

class FileUtil:
    def __init__ (self,filename=None):
        self.filename=filename
    
    @staticmethod
    def parse(item: str) -> str:
        return item.split(',')

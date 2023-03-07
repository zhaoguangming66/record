# 1 execjs 执行js时 报以下错误时
Traceback (most recent call last):
  File "C:\Python37\lib\threading.py", line 917, in _bootstrap_inner
    self.run()
  File "C:\Python37\lib\threading.py", line 865, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Python37\lib\subprocess.py", line 1238, in _readerthread
    buffer.append(fh.read())
UnicodeDecodeError: 'gbk' codec can't decode byte 0xaa in position 1122: illegal multibyte sequence

加上 
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
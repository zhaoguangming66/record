# 1 execjs 执行js时 报以下错误时
```
Traceback (most recent call last):
  File "C:\Python37\lib\threading.py", line 917, in _bootstrap_inner
    self.run()
  File "C:\Python37\lib\threading.py", line 865, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Python37\lib\subprocess.py", line 1238, in _readerthread
    buffer.append(fh.read())
UnicodeDecodeError: 'gbk' codec can't decode byte 0xaa in position 1122: illegal multibyte sequence
```

加上 文件前头加上
```python
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import execjs
```

# 2 webpack导出模块
```javascript
function o(t) {
        if (n[t])
            return n[t].exports;
        var i = n[t] = {
            i: t,
            l: !1,
            exports: {}
        };
        chas=  t.toString()  + ":" + (e[t].toString()) + ","
        zhaolog+=chas
         console.log("'" + t.toString() + "'" + ":" + (e[t] + "") + ",")
        return e[t].call(i.exports, i, i.exports, o),
        i.l = !0,
        i.exports
    }
```

t 是传进来的参数 `e[t].toString()` e 是下面call 或者 apply的东西
```javascript
console.log("'" + t.toString() + "'" + ":" + (e[t] + "") + ",")
```

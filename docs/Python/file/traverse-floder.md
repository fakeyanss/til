# 遍历文件夹

```python
import os

for dirpath, dirnames, filenames in os.walk(r'path'):
    print(f'open {dirpath}')
    if dirnames:
        print(dirnames)
    if filenames:
        print(filenames)
    print('-' * 10)
```
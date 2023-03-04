
<h1 align="left">Things I Learn</h1>
<p align="center">
  <img alt="TILs Count" src="https://img.shields.io/badge/dynamic/json.svg?color=black&label=TILs&query=count&url=https%3A%2F%2Fraw.githubusercontent.com%2Ffakeyanss%2Ftil%2Fmaster%2Fcount.json">
  <img alt="last commit" src="https://img.shields.io/github/last-commit/fakeyanss/til?color=purple">
  <a href="https://github.com/fakeYanss/til/blob/master/LICENSE">
    <img alt="License: MIT" src="https://img.shields.io/github/license/fakeyanss/til" target="_blank" />
  </a>
  <a href="https://foreti.me/til/">
    <img alt="Website" src="https://img.shields.io/website?url=https://foreti.me/til/">
  </a>
  <a href="https://twitter.com/fakeYanss">
    <img alt="Twitter: fakeYanss" src="https://img.shields.io/twitter/follow/fakeYanss.svg?style=social" target="_blank" />
  </a>
</p>

> Personal Wiki of Interesting things I learn every day at the intersection of software development, computer science & stuff.




## Categories
* [Java](#java) [**`3`**]
* [Makefile](#makefile) [**`1`**]
* [Miscellaneous](#miscellaneous) [**`1`**]
* [Python](#python) [**`6`**]

---




### Java

<ul>
<li><a target="_blank" href="https://github.com/fakeyanss/til/blob/master/docs/Java/IO/BIO-NIO-AIO.md">Java 中 BIO、NIO 与 AIO</a>
<li><a target="_blank" href="https://github.com/fakeyanss/til/blob/master/docs/Java/Basic/java-basic.md">Java 基础</a>
<li><a target="_blank" href="https://github.com/fakeyanss/til/blob/master/docs/Java/Spring/loading-order-of-Spring-Beans.md">Spring Beans 类加载顺序</a>
</ul>




### Makefile

<ul>
<li><a target="_blank" href="https://github.com/fakeyanss/til/blob/master/docs/Makefile/use-shell-variable.md">使用 Shell 变量</a>
</ul>




### Miscellaneous

<ul>
<li><a target="_blank" href="https://github.com/fakeyanss/til/blob/master/docs/Miscellaneous/docsify-build.md">构建 docsify 文档项目</a>
</ul>




### Python

<ul>
<li><a target="_blank" href="https://github.com/fakeyanss/til/blob/master/docs/Python/check-indentation-error.md">Check indentation errors in python</a>
<li><a target="_blank" href="https://github.com/fakeyanss/til/blob/master/docs/Python/file/is-file.md">判断目标路径是否是文件</a>
<li><a target="_blank" href="https://github.com/fakeyanss/til/blob/master/docs/Python/file/simple-file-server.md">文件上传下载服务器</a>
<li><a target="_blank" href="https://github.com/fakeyanss/til/blob/master/docs/Python/file/get-base-filename.md">获取路径中的文件名</a>
<li><a target="_blank" href="https://github.com/fakeyanss/til/blob/master/docs/Python/file/traverse-floder.md">遍历文件夹</a>
<li><a target="_blank" href="https://github.com/fakeyanss/til/blob/master/docs/Python/file/rename-file.md">重命名文件</a>
</ul>

## Usage

1. install docsify
```
npm i docsify-cli -g
```

2. create git repo, and init docsify
```
docsify init docs
```

3. customize index.html, just like my [index.html](docs/index.html)

4. preview your writing
```
docsify serve docs
```

5. install docsify-tools, for auto generate sidebar
```
npm i docsify-tools -g
```

generate sidebar
```
docsify-auto-sidebar -d docs
```

you can craete a git hook pre-commit, docsify-auto-sidebar will generate _narbar into sidebar, which is not expected, we can remove it manually
```
docsify-auto-sidebar -d docs

sed -i "" "/_navbar/d" docs/_sidebar.md # mac
sed -i "/_navbar/d" docs/_sidebar.md # linux

python build.py

git add .
```

## Author 

👤 **[FakeYanss](https://fakeyanss.github.io)** 

## About

TIL is inspired by [Bhupesh-V/til](https://github.com/Bhupesh-V/til).

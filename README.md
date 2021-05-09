# Things I Learn

Personal Wiki of Interesting things I learn every day at the intersection of software development, computer science & stuff (My Second Brain 🧠️)

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

git add .
```

## About

TIL is inspired by [Bhupesh-V/til](https://github.com/Bhupesh-V/til)。
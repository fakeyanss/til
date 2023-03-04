# 使用 Shell 变量

在 Makefile 使用 Shell 变量有一点绕，需要加上特殊的符号，并且注意变量只在同一行内共享，除非用 `\` 连接多行。

比如下面这个例子，用于统计项目中go源码的行数。

如果我想在 `echo` 时使用前面计算的行数变量，必须用 `\` 连接这两行，这一点对于初学者非常容易踩坑。

```makefile
# 统计代码行数
statline:
    @total=`find . | grep "\.go$$" | xargs -I f cat f | wc -l`; \
    echo "TOTAL_CODE_LINE: $$total"
```

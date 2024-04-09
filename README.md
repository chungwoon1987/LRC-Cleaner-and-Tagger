这个脚本首先定义了两个函数：
`remove_zwnbsp` 用于删除ZWNBSP字符，
`insert_ti_ar` 用于插入`[ti]`和`[ar]`标签。
然后，它会遍历指定文件夹中的所有`.lrc`文件，
先调用 `remove_zwnbsp` 函数删除ZWNBSP字符，
再调用 `insert_ti_ar` 函数检查并插入标签。

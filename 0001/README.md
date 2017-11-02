## 心得

使用uuid模块生成随机数。随机uuid的重复几率极小，可忽略，适合作为激活码。这里使用uuid4()。
详见[维基百科](https://zh.wikipedia.org/wiki/通用唯一识别码)
以下为uuid模块说明（help(uuid)）

> This module provides immutable UUID objects (class UUID) and the functions
> uuid1(), uuid3(), uuid4(), uuid5() for generating version 1, 3, 4, and 5
> UUIDs as specified in RFC 4122.
> 
> If all you want is a unique ID, you should probably call uuid1() or uuid4().
> Note that uuid1() may compromise privacy since it creates a UUID containing
> the computer's network address.  uuid4() creates a random UUID.

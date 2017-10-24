import logging; logging.basicConfig(level=logging.DEBUG)
import time, uuid ,asyncio
import orm
from orm import Model, StringField, BooleanField, FloatField, TextField

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)

class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)


if __name__== '__main__':

    async def test():
        await orm.create_pool(loop,user='www-data', password='www-data', db='awesome')
        u = User(name='Test', email='test@example.com', passwd='123456780', image='about:blank')
        await u.save()
        a = await u.findall() #这个要打印才显示出来
        print(a)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())
    orm.__pool.close()  #在关闭event loop之前，首先需要关闭连接池。
    loop.run_until_complete(orm.__pool.wait_closed())#在关闭event loop之前，首先需要关闭连接池。
    loop.close()
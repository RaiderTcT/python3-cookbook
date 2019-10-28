# @作者     ： Ulysses
# @功能描述 ： 在子类中扩展属性
# @修改记录 ： 2019/2/21 11:45 创建
class Person:
    def __init__(self, name):
        self.name = name  # 实质上会调用setter方法，跳过name而去访问_name

    @property  # getter函数 将name定义为property属性
    def name(self):
        print('使用getter方法')
        return self._name

    @name.setter  # 可选
    def name(self, value):
        print('使用setter方法')
        if not isinstance(value, str):
            raise  TypeError('字符串类型')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError('无法删除')

p = Person('Rose')
print(p.name)
print(Person.name)  # <property object at 0x000000000054ACC8>


class SubPerson_0(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson_0, SubPerson_0).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson_0, SubPerson_0).name.__delete__(self)

s = SubPerson_0('sub name 0')
print(s.name)

# 只对其中一个方法做扩展
class SubPerson(Person):
    @Person.name.getter
    def name(self):
        print('Getting name')
        return super().name

s = SubPerson('Unr')
print(s.name)

class SubPerson_1(Person):
    @Person.name.setter
    def name(self, value):
        print('Setting name to ', value)
        # name是self描述符， self是用来访问属性的实例（SubPerson_1的实例s1)
        # 使用类名调用描述器，返回描述器本身
        # 使用实例名调用描述器，返回自定义的值
        super(SubPerson_1, SubPerson_1).name.__set__(self, value)
        # object.__set__(self, instance, value)
        # 调用此方法以设置instance指定的所有者类的实例的属性为新值value。
        # 使用super(SubPerson_1, SubPerson_1)，把控制流传递到之前定义的name属性
        # 取SubPerson_1的MRO， class为SubPerson_1之后的类

s1 = SubPerson_1('Roma')
print(s1.name)
print(SubPerson_1.__mro__)


# A descriptor
class String:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        instance.__dict__[self.name] = value


# A class with a descriptor
class Person1:
    name = String('name')

    def __init__(self, name):
        self.name = name


# Extending a descriptor with a property
class SubPerson1(Person1):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson1, SubPerson1).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson1, SubPerson1).name.__delete__(self)

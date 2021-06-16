# Паттерн Декоратор

Паттерн декоратор относится к классу структурных паттернов проектирования. Его основная задача -- динамическое подключение дополнительной функциональности к объекту. При этом для подключения дополнительной функциональности используется не сложная иерархия подклассов, что является классическим решением данной задачи, а отдельная иерархия декораторов.

Каждый из видов дополнительной функциональности, которая может быть добавлена к объекту, помещается в отдельный класс. Эти классы сами по себе небольшие, поэтому в них легко разобраться.

В паттерн "Декоратор" входят оборачиваемый объект и сама иерархия декораторов. Каждый из декораторов реализует какое-то одно функциональное свойство. Это позволяет соблюдать один из SOLID принципов -- принцип единственной ответственности. Так мы можем подключить к классу только ту функциональность, которая необходима ему в данный момент. Для подключения нескольких
функциональных свойств можно последовательно использовать несколько декораторов.


# Структура декораторов

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Decorator_UML_class_diagram.svg/960px-Decorator_UML_class_diagram.svg.png">

Для создания паттерна "Декоратор" необходимы следующие классы:

* Абстрактный объект (Component)
* Оборачиваемый объект (на UML-диаграмме ConcreteComponent)
* Абстрактный декоратор (Decorator)
* Конкретный декоратор (ConcreteDecorator)

Как видно из диаграммы, все декораторы по сути являются объектами, подобными самому компоненту. Из этого следует, что они реализуют одинаковый интерфейс. Согласно принципу подстановки Барбары Лисков у пользователя должна быть возможность корректного использования объекта-декоратора (то есть объекта, обернутого в декоратор), не зная об этом.

Тут находится одно из слабых мест паттерна. Интерфейс объекта и интерфейс модифицированного объекта одинаковы. Это не всегда удобно, иногда для модифицированного объекта требуется отдельный интерфейс.

# Другие похожие паттерны:

### Стратегия

Также позволяет динамически добавлять поведение объекту. Так же, как и в декораторе, стратегии реализуются в отдельных классах Однако, в отличие от декоратора, декорируемый класс не оборачивается в стратегию, а стратегия, как компонент, встраивается в основной класс.

### Цепочка обязанностей

Цепочка обязанностей так же в чем-то близкий к декоратору класс. Она так же задает множество обработчиков некоторого события. Отличие от декоратора заключается в том, что в цепочке обязанностей событие обрабатывает только один из классов, тогда как в декораторе все классы-декораторы обрабатывают событие.

# Использование паттерна Декоратор

При использовании паттерна декорируемый объект оборачивается в декоратор. Таким образом получается вложенная структура из декораторов. Отменить действие декоратора можно, если достать базовый объект из декоратора. Это можно сделать, обратившись к decorated_object.base. Аналогичным образом можно отменить эффект декоратора из середины иерархии. Для этого изменим базовый объект у внешнего декоратора на базовый объект декоратора, который необходимо удалить. Принцип похож на удаление элемента из середины односвязного списка.

# Пример использования Декоратора


```python
from abc import ABC, abstractmethod

class Creature(ABC):
    @abstractmethod
    def feed(self):
        pass
    
    @abstractmethod
    def move(self):
        pass
    
    @abstractmethod
    def make_noise(self):
        pass
    
class Animal(Creature):
    def feed(self):
        print("I eat grass")
        
    def move(self):
        print("I walk forward")
    
    def make_noise(self):
        print("WOOO!")
        
class AbstractDecorator(Creature):
    def __init__(self, obj):
        self.obj = obj
        
    def feed(self):
        self.obj.feed()
    
    def move(self):
        self.obj.move()
    
    def make_noise(self):
        self.obj.make_noise()
        
class Swimming(AbstractDecorator):
    def move(self):
        print("I swim")
    
    def make_noise(self):
        print("...")
        
class Flying(AbstractDecorator):
    def move(self):
        print("I fly")
    
    def make_noise(self):
        print("QUAAA!")
        
class Predator(AbstractDecorator):
    def feed(self):
        print("I eat other animals")
        
class Fast(AbstractDecorator):
    def move(self):
        self.obj.move()
        print("Fast!")
```


```python
animal = Animal()
animal.feed()
animal.move()
animal.make_noise()
print()

animal = Swimming(animal)
animal.feed()
animal.move()
animal.make_noise()
print()

animal = Predator(animal)
animal.feed()
animal.move()
animal.make_noise()
print()

animal = Fast(animal)
animal.feed()
animal.move()
animal.make_noise()
print()


animal = Fast(animal)
animal.feed()
animal.move()
animal.make_noise()
print()

animal.obj.obj = animal.obj.obj.obj
animal.feed()
animal.move()
animal.make_noise()
print()

```

    I eat grass
    I walk forward
    WOOO!
    
    I eat grass
    I swim
    ...
    
    I eat other animals
    I swim
    ...
    
    I eat other animals
    I swim
    Fast!
    ...
    
    I eat other animals
    I swim
    Fast!
    Fast!
    ...
    
    I eat grass
    I swim
    Fast!
    Fast!
    ...
    



```python

```

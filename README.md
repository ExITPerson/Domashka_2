![b3a5a00f-6e6b-488f-9ac1-5623c31cb0d1.jpg](design_tools%2Fb3a5a00f-6e6b-488f-9ac1-5623c31cb0d1.jpg)

# <p align="center"> Домашка 2 </p>


## <p align="center">Описание</p>

**<p align="center">Домашка 2 - это проект, который маленькими шагами заложит основу для интернет-магазина.</p>**

---

## <p align="center">Функции программы</p>


- **Формировать базу из категорий и видов товаров для последующего использования**
- **Создание ордеров на заказ товара**
- **Получение кол-во продуктов на складе**


----

## <p align="center">Установка</p>

1. **Клонируйте репозиторий:**
````
git clone https://github.com/ExITPerson/Domashka_2.git
````

2. **Установите зависимости:**
````
pip install -r requirements.txt
````
---

## <p align="center">Информация о тестировании проекта</p>

- **Запустите тестирование**
````
pytest --cov src --cov-report term-missing
````

- **Увидите информацию о тестах папки scr в терминале**

````
==================== test session starts =====================
platform win32 -- Python 3.12.6, pytest-8.3.3, pluggy-1.5.0
configfile: pytest.ini
plugins: cov-6.0.0
collected 25 items                                           

tests\test_category.py ............                    [ 48%]
tests\test_lawn_grass.py ..                            [ 56%]
tests\test_print_mixin.py .                            [ 60%]
tests\test_products.py .......                         [ 88%]
tests\test_smartphone_products.py ..                   [ 96%] 
tests\test_utils.py .                                  [100%]

---------- coverage: platform win32, python 3.12.6-final-0 -----------
Name                         Stmts   Miss  Cover   Missing    
----------------------------------------------------------    
src\__init__.py                  0      0   100%
src\base_products.py             7      1    86%   10
src\category.py                 76      5    93%   14, 23-25, 35
src\lawn_grass_products.py      12      1    92%   25
src\print_mixin.py               9      0   100%
src\product_iterator.py         25      7    72%   28-41      
src\products.py                 49      1    98%   30
src\smartphone_products.py      13      0   100%
src\utils.py                    19      8    58%   17-25      
src\zero_quantity.py             3      0   100%
----------------------------------------------------------    
TOTAL                          213     23    89%


==================== 25 passed in 0.29s ===================== 
````
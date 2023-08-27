# project-Python_IGRA_Backend
## Игра "Скачки". Идея взята из интернета, мною эта идея усложнена и сделана в виде полной игры. 


     Боб хочет собрать всех своих друзей-предпринимателей вместе.
    Но для того, чтобы заставить занятых друзей прийти к нему,
    следует сделать что-то необычное. У Боба есть ферма, на которой
    живут 10 лошадей. Он хочет провести скачки со ставками.
    Лошади пронумерованы от 1 до 10. На одну и ту же лошадь нельзя
    сделать ставку дважды. Также нельзя делать нулевую ставку.

- **Author** (Автор): [Игорь Щеглов](https://t.me/HelloWonderWorld)

    Игра:

        Это групповая игра, 10 игроков. Каждый игрок ставит на лошадь, нельзя дважды ставить на одну 
-     лошадь, делает ставку. Можно поставить на одну из 10 лошадей. Игрок делает ставку на
-     выбранную лошадь. Введение данных регистрируется, должно быть корректным (лошадь - целые числа 
-     от 1 до 10, сумма ставки - целые числа больше 0). При не правильном вводе (строка, дробные 
-     числа, отрицательные значения), выводится предупреждение и предлагается ввести числа от 1 
-     до 10 на выбор лошади и число больше 0 при выбранной ставке. Когда все ставки сделаны
-     начинается игра. Индикация начала скачек строка, в которой добавляются элементы с интервалом
-     в 2 секунды. Далее выдается информация: игра с датой, лошадь которая пришла первой, и сумма,
-     которую получает победитель с оформлением. Сумма выиграша - это сумма всех ставок без вычетов.
-     Результат выдается методом случайного выбота с помощью модуля random. По окончании игры все 
-     результаты записываются в файл json в виде словаря. По окончании новой игры этот файл 
-     обновляется. Делайте ставки, господа!


## Проект состоит из 3 файлов:

- main- запуск программы

- bet_data.json - запись словаря с информацией по игре

- README - информация по проекту


## Запуск

Для запуска программы в директории необходимо запустить файл main.py


## License

**Free Software**
# Лабораторная работа № 1. Система контроля версий. Работа с ней

**ФИО:** Лукичев Артём Дмитриевич
**Группа:** 221141
**Вариант:** 8

## Индивидуальные задания (вариант 8)

| Задание | Номер | Статус |
| --- | --- | --- |
| Средней сложности 1 | 5 — создать ветку `feature`, добавить новый файл | ✅ |
| Средней сложности 2 | 8 — создать репозиторий на GitHub и связать его с локальным | ✅ |
| Средней сложности 3 | 10 — склонировать чужой репозиторий и изучить историю | ✅ |
| Повышенной сложности 1 | 4 — настроить Git hook для проверки кода flake8 | ✅ |
| Повышенной сложности 2 | 6 — настроить GitHub Actions для проверки Python-кода | ✅ |

## Выполнение

### 1. Создание ветки `feature` (средняя № 5)
Создана ветка `feature/report`, в неё добавлен файл `report.py`,
затем ветка слита с `main` через `git merge --no-ff`.
Граф коммитов (видно слияние):

```
*   f0cdd2b merge: слияние feature/report в main
|\
| * 2ccf690 feat: добавить report.py в ветке feature/report
|/
* bc99b96 refactor: использовать sum_even из utils в main.py
* e135ea4 chore: добавить .gitignore для Python
* 5c88c3c feat: добавить utils.py с суммой чётных чисел
* 218dd16 feat: добавить main.py с функцией приветствия
```

### 2. Репозиторий на GitHub (средняя № 8)
Локальный репозиторий связан с GitHub:
```bash
git remote add origin git@github.com:airman66/lab1-git-version-control.git
git push -u origin main
```

### 3. Клонирование чужого репозитория (средняя № 10)
Склонирован репозиторий `pallets/click`, история изучена
командами `git log --oneline`, `git shortlog -sn`, `git log --stat`.
Результат сохранён в [docs/cloned_repo_history.txt](docs/cloned_repo_history.txt).

### 4. Git hook для flake8 (повышенная № 4)
Настроен хук `pre-commit` в `.git/hooks/pre-commit`:
перед каждым коммитом запускается `python3 -m flake8 --max-line-length=100 .`,
при ошибках стиля коммит отменяется (код выхода 1).

### 5. GitHub Actions (повышенная № 6)
В [`.github/workflows/ci.yml`](.github/workflows/ci.yml) настроен CI:
проверка стиля flake8, компиляция модулей, запуск `main.py`
на каждый push и pull request в ветку `main`.

## Структура проекта

```
lab1-git-version-control/
├── main.py            # точка входа
├── utils.py           # вспомогательные функции
├── report.py          # добавлен через ветку feature/report
├── .gitignore         # __pycache__/, *.pyc, .venv/, .env
├── requirements-dev.txt
├── docs/
│   └── cloned_repo_history.txt   # история клонированного репозитория
└── .github/workflows/
    └── ci.yml          # CI-проверки Python-кода
```

## Запуск

```bash
python3 main.py
```

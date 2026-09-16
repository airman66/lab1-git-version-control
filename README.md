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
| Повышенной сложности 1 | 1 — разрешить конфликт при слиянии веток | ✅ |
| Повышенной сложности 2 | 8 — использовать git submodules | ✅ |

Дополнительно (вне зачёта варианта): настроены git hook с flake8
(`hooks/pre-commit`, `core.hooksPath=hooks`) и GitHub Actions CI.

## Выполнение

### Средняя № 5 — ветка `feature`, новый файл
Создана ветка `feature/report`, в неё добавлен файл `report.py`,
затем ветка слита с `main` через `git merge --no-ff`.

### Средняя № 8 — репозиторий на GitHub
Локальный репозиторий связан с GitHub и запушен:
```bash
git remote add origin git@github.com:airman66/lab1-git-version-control.git
git push -u origin main
```

### Средняя № 10 — клонирование чужого репозитория
Склонирован `pallets/click`, история изучена командами
`git log --oneline`, `git shortlog -sn`, `git log --stat`;
добавлены краткие выводы. Полный отчёт:
[docs/cloned_repo_history.txt](docs/cloned_repo_history.txt).

### Повышенная № 1 — разрешение конфликта при слиянии
1. В ветке `feature/greeting` изменена строка в `main.py`:
   `return f"Hello, {name}! Welcome!"`.
2. В `main` изменена та же строка: `return f"Hello, {name}! Glad to see you."`.
3. `git merge feature/greeting` → конфликт:
   ```
   Auto-merging main.py
   CONFLICT (content): Merge conflict in main.py
   Automatic merge failed; fix conflicts and then commit the result.
   ```
4. Файл получил маркеры `<<<<<<< HEAD / ======= / >>>>>>> feature/greeting`.
5. Конфликт разрешён вручную — оба варианта объединены:
   `return f"Hello, {name}! Glad to see you. Welcome!"`,
   затем `git add main.py` и `git commit` (merge-коммит `dd84b38`).
   После слияния `python3 main.py` выводит: `Hello, Git! Glad to see you. Welcome!`

### Повышенная № 8 — git submodules
```bash
git submodule add https://github.com/pallets/click vendor/click
```
Закоммичены `.gitmodules` и gitlink `vendor/click` (режим 160000,
см. коммит `ce020bc`). Клонирование вместе с сабмодулем:
`git clone --recurse-submodules git@github.com:airman66/lab1-git-version-control.git`.

### Дополнительно: git hook с flake8
Хук лежит в отслеживаемом каталоге `hooks/pre-commit` и подключён через
`git config core.hooksPath hooks`. Перед каждым коммитом запускается
`python3 -m flake8 --max-line-length=100 --exclude=vendor .`, при ошибках
стиля коммит отменяется (проверено на практике).

### Дополнительно: GitHub Actions
В [`.github/workflows/ci.yml`](.github/workflows/ci.yml) на push и PR в `main`:
проверка flake8 (с исключением `vendor/`), компиляция модулей, запуск `main.py`.

## Граф коммитов (актуальный)

```
* fbbd066 ci: исключить vendor/ из проверки flake8
* ce020bc feat: добавить vendor/click как git submodule (повыш. №8)
*   dd84b38 merge: разрешить конфликт в main.py (объединены оба приветствия)
|\
| * a8c1f78 feat: добавить Welcome к приветствию в feature/greeting
* | 1431415 feat: добавить Glad to see you к приветствию в main
|/
* b908ab3 chore: убрать .DS_Store из репозитория
* 52c06ba docs: добавить README с отчётом и настроить CI flake8
*   3acee3f merge: слияние feature/report в main
|\
| * 620ffa6 feat: добавить report.py в ветке feature/report
|/
* 6d71a23 refactor: использовать sum_even из utils в main.py
* d2448b8 chore: добавить .gitignore для Python
* 7203377 feat: добавить utils.py с суммой чётных чисел
* d8745df feat: добавить main.py с функцией приветствия
```
(граф актуален на момент сдачи; свежий вид — `git log --oneline --graph`.)

## Структура проекта

```
lab1-git-version-control/
├── main.py            # точка входа
├── utils.py           # вспомогательные функции
├── report.py          # добавлен через ветку feature/report
├── .gitignore         # __pycache__/, *.pyc, .venv/, .env, .DS_Store
├── .gitmodules        # сабмодуль vendor/click
├── requirements-dev.txt
├── hooks/
│   └── pre-commit     # проверка flake8 перед коммитом (core.hooksPath)
├── docs/
│   └── cloned_repo_history.txt   # история клонированного репозитория
├── vendor/
│   └── click          # git submodule (pallets/click)
└── .github/workflows/
    └── ci.yml          # CI-проверки Python-кода
```

## Запуск

```bash
python3 main.py
# Hello, Git! Glad to see you. Welcome!
# 6
```

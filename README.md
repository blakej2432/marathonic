
```
marathonic
├─ .python-version
├─ config
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ crawl
│  ├─ city.csv
│  ├─ crawl copy.ipynb
│  ├─ crawl.ipynb
│  ├─ crawl.py
│  ├─ crawls.py
│  ├─ race_export.csv
│  └─ race_list_2025.csv
├─ manage.py
├─ poetry.lock
├─ pyproject.toml
├─ react_app
│  ├─ README.md
│  ├─ eslint.config.js
│  ├─ index.html
│  ├─ package-lock.json
│  ├─ package.json
│  ├─ public
│  │  └─ vite.svg
│  ├─ src
│  │  ├─ App.css
│  │  ├─ App.tsx
│  │  ├─ assets
│  │  │  └─ react.svg
│  │  ├─ components
│  │  ├─ entries
│  │  │  ├─ login.tsx
│  │  │  └─ race.tsx
│  │  ├─ index.css
│  │  ├─ main.tsx
│  │  └─ vite-env.d.ts
│  ├─ tsconfig.app.json
│  ├─ tsconfig.json
│  ├─ tsconfig.node.json
│  └─ vite.config.ts
├─ repo
│  ├─ __init__.py
│  ├─ profiles
│  │  ├─ __init__.py
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ manager.py
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  ├─ 0002_alter_customuser_options_alter_customuser_table.py
│  │  │  ├─ 0003_customuser_race.py
│  │  │  ├─ 0004_alter_customuser_email.py
│  │  │  ├─ 0005_alter_customuser_managers.py
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ static
│  │  │  └─ profiles
│  │  │     ├─ css
│  │  │     │  └─ login.css
│  │  │     ├─ images
│  │  │     │  ├─ google.svg
│  │  │     │  ├─ kakao.svg
│  │  │     │  └─ naverlogin.svg
│  │  │     └─ js
│  │  ├─ templates
│  │  │  └─ profiles
│  │  │     ├─ index.html
│  │  │     └─ login.html
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  └─ views.py
│  ├─ race
│  │  ├─ __init__.py
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ filters.py
│  │  ├─ management
│  │  │  └─ commands
│  │  │     ├─ data_to_csv.py
│  │  │     └─ seed_race_list.py
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  ├─ 0002_alter_coursetype_code.py
│  │  │  ├─ 0003_race_city.py
│  │  │  ├─ 0004_alter_race_city.py
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ serializers.py
│  │  ├─ services.py
│  │  ├─ static
│  │  │  └─ race
│  │  │     ├─ css
│  │  │     │  ├─ modal.css
│  │  │     │  └─ race.css
│  │  │     ├─ images
│  │  │     │  ├─ banner-sample.jpg
│  │  │     │  ├─ banner-sample2.jpg
│  │  │     │  ├─ banner-sample3.jpg
│  │  │     │  ├─ main_logo.png
│  │  │     │  ├─ race-sample.jpg
│  │  │     │  └─ search_icon.png
│  │  │     └─ js
│  │  │        ├─ banner.js
│  │  │        └─ modal.js
│  │  ├─ templates
│  │  │  └─ race
│  │  │     ├─ _race_filter.html
│  │  │     ├─ _race_list.html
│  │  │     ├─ _race_modal.html
│  │  │     ├─ index.html
│  │  │     ├─ my_race.html
│  │  │     └─ race.html
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  └─ views
│  │     ├─ myrace_views.py
│  │     └─ race_views.py
│  └─ shoes
│     ├─ __init__.py
│     ├─ admin.py
│     ├─ apps.py
│     ├─ migrations
│     │  └─ __init__.py
│     ├─ models.py
│     ├─ static
│     │  └─ shoes
│     │     ├─ css
│     │     ├─ images
│     │     └─ js
│     ├─ templates
│     │  └─ shoes
│     ├─ tests.py
│     └─ views.py
├─ static
│  ├─ css
│  │  ├─ common.css
│  │  ├─ home.css
│  │  ├─ pretendard.css
│  │  ├─ woff
│  │  │  ├─ Pretendard-Black.woff
│  │  │  ├─ Pretendard-Bold.woff
│  │  │  ├─ Pretendard-ExtraBold.woff
│  │  │  ├─ Pretendard-ExtraLight.woff
│  │  │  ├─ Pretendard-Light.woff
│  │  │  ├─ Pretendard-Medium.woff
│  │  │  ├─ Pretendard-Regular.woff
│  │  │  ├─ Pretendard-SemiBold.woff
│  │  │  └─ Pretendard-Thin.woff
│  │  └─ woff2
│  │     ├─ Pretendard-Black.woff2
│  │     ├─ Pretendard-Bold.woff2
│  │     ├─ Pretendard-ExtraBold.woff2
│  │     ├─ Pretendard-ExtraLight.woff2
│  │     ├─ Pretendard-Light.woff2
│  │     ├─ Pretendard-Medium.woff2
│  │     ├─ Pretendard-Regular.woff2
│  │     ├─ Pretendard-SemiBold.woff2
│  │     └─ Pretendard-Thin.woff2
│  ├─ images
│  │  ├─ main_logo.png
│  │  └─ search_icon.png
│  └─ js
├─ staticfiles
└─ templates
   └─ base.html

```
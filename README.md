# 🚀 Web Application with Docker, PostgreSQL & Flask
  
Простое веб-приложение с авторизацией, которое можно использовать как основу для собственного проекта.

## 🌟 Особенности проекта

- **Docker-ориентированный** (сборка через compose)
- **Безопасность**: секреты через ".env", healthcheck для БД
- **Автоматический деплой** через Git hooks
- **Логирование** операций деплоя

## 🛠 Технологический стек

- Frontend: Nginx со статическим html
- Backend: Python Flask
- DataBase: PostgreSQL
- Infrastructure: Docker, Docker Compose
- CI/CD: Git hooks

🔧 Архитектура проекта
Copy
container-web-app/                                                                                                                
│                                                                                                                                 
├── backend/                                                                                                                      
│   ├── requirements.txt                                                                                                          
│   └── server.py                                                                                                                 
│                                                                                                                                 
├── db/                                                                                                                           
│   └── init.sql                                                                                                                  
│                                                                                                                                 
├── frontend/                                                                                                                     
│   ├── static/                                                                                                                   
│   └── index.html                                                                                                                
│                                                                                                                                 
├── nginx/                                                                                                                        
│   ├── ssl/                                                                                                                      
│   │   ├── domain.crt                                                                                                            
│   │   ├── domain.conf                                                                                                           
│   │   └── domain.key                                                                                                            
│   └── nginx.conf                                                                                                                
│                                                                                                                                 
├── scripts/                                                                                                                      
│   └── post-receive                                                                                                              
│                                                                                                                                 
├── .env                                                                                                                          
├── docker-compose.yaml                                                                                                           
└── README.md                                                                                                                     
🔒 Безопасность
Все секреты хранятся в .env (в git не коммитятся)

Healthcheck для мониторинга состояния PostgreSQL

## CI/CD:

Автоматический деплой через Git hooks

Скрипт деплоя с логированием (/var/log/deploy.log)

## Infrastructure as Code:

Полная воспроизводимость через Docker

Версионирование образов

## Функционал
- Регистрация новых пользователей
- Авторизация существующих пользователей

## Запуск проекта

1. Клонируйте репозиторий:

   git clone https://github.com/ScoobyBo/container-web-app.git
   cd [Директория_проекта]

2. Измените под себя как минимум следующие файлы:
    - domain.conf
    - post-receive (а так же перенесите его в ./repo.git/hooks/)

3. Запустите проект через Docker Compose:
    docker-compose up --build

4. После запуска проект будет доступен по адресу:
    http://your_domain/  | 80 port

   А так же, если настроите https:
    https://your_domain/ | 443 port
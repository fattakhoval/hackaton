FROM node:14

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем package.json и package-lock.json в рабочую директорию
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем все файлы приложения из текущей директории (frontend)
COPY . .

# Собираем приложение
RUN npm run build

# Устанавливаем сервер для обслуживания статических файлов
RUN npm install -g serve

# Запускаем приложение
CMD ["serve", "-s", "dist"]

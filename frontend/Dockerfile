# Imagen base de Node
FROM node:22-alpine

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Modo desarrollo para Vite
ENV NODE_ENV=development

# Instala dependencias (copia primero package.json para aprovechar el cache)
COPY package*.json ./
RUN npm install

# Copia el resto del proyecto
COPY . .

# Puerto por defecto de Vite
EXPOSE 5173

# Servidor de desarrollo escuchando en todas las interfaces
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]

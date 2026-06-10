# Build frontend
FROM node:20 AS frontend-builder

WORKDIR /app

COPY web/package*.json ./
RUN npm install

COPY web/ .
RUN npm run build

# Nginx
FROM nginx:latest

COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/conf.d /etc/nginx/conf.d

COPY --from=frontend-builder /app/dist /usr/share/nginx/html
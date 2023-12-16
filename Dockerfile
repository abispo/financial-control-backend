FROM node:20

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY src/ ./src/

EXPOSE 3000

ENV NODE_ENV=development

CMD ["npm", "run", "dev"]

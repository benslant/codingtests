FROM node:20-alpine

WORKDIR /app

COPY ./nextjs-app ./
RUN npm install
RUN npx prisma generate
EXPOSE 3000
CMD npm run docker
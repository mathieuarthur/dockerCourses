FROM node:alpine AS builder

WORKDIR /app

COPY package*.json ./

RUN npm ci

COPY . .

RUN npm run build

FROM node:alpine AS runner

WORKDIR /app

COPY --from=builder /app/build ./build
COPY --from=builder /app/package*.json ./build

ENV HOST=0.0.0.0 \
    PORT=8000

EXPOSE 8000

CMD [ "node", "build"]
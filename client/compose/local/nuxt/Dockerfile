FROM node:16-alpine3.14

WORKDIR /

COPY ./package.json .

RUN yarn install #--prefer-offline
# --pure-lockfile
# --non-interactive
# --production=true

COPY . .
CMD ["yarn", "run", "dev"]

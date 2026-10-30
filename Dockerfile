# ECR Public mirror avoids Docker Hub rate limits on CodeBuild
FROM public.ecr.aws/docker/library/node:20-alpine

ENV NODE_ENV=production
WORKDIR /usr/src/app

COPY src/package*.json ./
RUN npm ci --omit=dev

COPY src/ .

USER node
EXPOSE 3000
CMD ["node", "app.js"]

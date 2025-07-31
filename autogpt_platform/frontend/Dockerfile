# estágio base para desenvolvimento e produção
FROM node:21-alpine AS base
WORKDIR /app
RUN corepack enable
COPY autogpt_platform/frontend/package.json autogpt_platform/frontend/pnpm-lock.yaml ./
RUN --mount=type=cache,target=/root/.local/share/pnpm pnpm install --frozen-lockfile

# estágio de desenvolvimento
FROM base AS dev
ENV NODE_ENV=development
ENV HOSTNAME=0.0.0.0
COPY autogpt_platform/frontend/ .
EXPOSE 3000
CMD ["pnpm", "run", "dev", "--hostname", "0.0.0.0"]

# estágio build para produção
FROM base AS build
COPY autogpt_platform/frontend/ .
ENV SKIP_STORYBOOK_TESTS=true
RUN pnpm build

# estágio de produção - baseado na referência do nextjs
# https://github.com/vercel/next.js/blob/64271354533ed16da51be5dce85f0dbd15f17517/examples/with-docker/Dockerfile
FROM node:21-alpine AS prod
ENV NODE_ENV=production
ENV HOSTNAME=0.0.0.0
WORKDIR /app

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

RUN mkdir .next
RUN chown nextjs:nodejs .next

COPY --from=build --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=build --chown=nextjs:nodejs /app/.next/static ./.next/static

COPY --from=build /app/public ./public

USER nextjs

EXPOSE 3000
CMD ["node", "server.js"]
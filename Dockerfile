# Build stage
FROM node:16 AS build

WORKDIR /app
COPY . .

RUN npm install
RUN npm run build

# Production stage
FROM python:3.10

ENV APP_USER=appuser
ENV APP_NAME=levreview
ENV APP_HOME=/home/${APP_NAME}/${APP_NAME}
ENV APP_PORT=8000
ENV DJANGO_SETTINGS_MODULE=${APP_NAME}.settings.prod

WORKDIR $APP_HOME
RUN adduser --disabled-password --gecos "" $APP_USER \
  && chown -R $APP_USER:$APP_USER $APP_HOME
USER $APP_USER

COPY . .
COPY --from=build /app/frontend/build/ ./frontend/build/

RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py collectstatic --noinput

EXPOSE $APP_PORT

CMD ["./deployment/run.sh"]

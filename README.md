### Приложение для аннотирования текстов на русском языке на основе [модели](https://huggingface.co/IlyaGusev/rut5_base_sum_gazeta) Ильи Гусева.

#### 1. Основные используемые библиотеки
- [Huggingface](https://huggingface.co/)
- [Pytorch](https://pytorch.org/)
- [Streamlit](https://streamlit.io/)

#### 2. Запуск на локальном компьютере
 - создаем локальное окружение (автор использует [conda](https://docs.conda.io/en/latest/));
 - устанавливаем необходимые пакеты (environment.yml или requirements.txt);
 - запускаем веб-сервер командой ```streamlit run app.py```.

PS. Файл параметров окружения conda `environment.yml` переименован в `environments.yml`, так как `https://streamlit.io` для установки зависимостей использует, при наличии, `environment.yml`, а не `requirements.txt`, что приводит к ошибке развертывания приложения.

#### 3. Запуск в [docker](https://www.docker.com/)

Создаем контейнер
```
docker build . -t streamlitapp  --progress=plain
```

Запускаем контейнер
```
docker run -p 8051:8051 streamlitapp
```

#### 4. Развернутое приложение
Ссылка на развернутое [приложение](https://losyash-text-summarizer-streamlit-app-9grqc2.streamlit.app/).
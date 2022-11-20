### Приложение для аннотирования текстов на русском языке на основе [модели](https://huggingface.co/IlyaGusev/rut5_base_sum_gazeta) Ильи Гусева.

Используются библиотеки:
- [Huggingface](https://huggingface.co/)
- [Pytorch](https://pytorch.org/)
- [Streamlit](https://streamlit.io/)

Локальное тестирование проводилось в [conda](https://docs.conda.io/en/latest/) и [docker](https://www.docker.com/).

Ссылка на развернутое [приложение](https://losyash-text-summarizer-streamlit-app-9grqc2.streamlit.app/).

PS. Файл параметров окружения conda `environment.yml` переименован в `environments.yml`, так как `streamlit` для установки зависимостей использует, при наличие, `environment.yml`, а не файл `requirements.txt`, что приводит к ошибке развертывания приложения.
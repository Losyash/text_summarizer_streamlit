# Пример приложения машинного обучения для развертывания на облачных платформах

Web-приложение для классификации изображений. Используются библиотеки:

- [TensorFlow](https://www.tensorflow.org/).
- [Streamlit](https://streamlit.io/).

Для распознавания изображений используется нейронная сеть [EfficientNetB0](https://keras.io/api/applications/efficientnet/#efficientnetb0-function). Подробности о модели в статье:

- [EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks](https://arxiv.org/abs/1905.11946).

[Ссылка на развернутое приложение](https://image-classification-demo.herokuapp.com/).

Тестирование изменений без ключа SSH

Приложение для аннотирования текстов на русском языке.

Используется готовая [модель](https://huggingface.co/IlyaGusev/rugpt3medium_sum_gazeta) Ильи Гусева.

Локальное тестирование проводилось в [conda](https://docs.conda.io/en/latest/) и [venv](https://docs.python.org/3/tutorial/venv.html).
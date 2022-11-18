import io
import streamlit as st

from text_summarizer import summirize


txt = None

st.title('Аннотирование текста')

option = st.selectbox(
    'Выберите способ ввода текста?',
    ('Загрузить из файла', 'Ввести вручную')
)

if (option == 'Ввести вручную'):
    txt = st.text_area(
        'Текст для аннотации',
        height=300,
        placeholder='Введите текст'
    )

if (option == 'Загрузить из файла'):
    file = st.file_uploader(
        'Выберить файл',
        type='txt',
        help='Выберите файл'
    )

    if file is not None:
        stringio = io.StringIO(file.getvalue().decode("utf-8"))
        txt = stringio.read()

if st.button('Аннотировать текст', disabled=True if txt is None else False):
    with st.spinner('Подождите, идет обработка текста'):
        t = summirize(txt)
        st.write(t)
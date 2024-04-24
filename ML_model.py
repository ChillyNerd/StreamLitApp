import streamlit as st
import pandas as pd
import pickle
import os

DATA_PATH = os.path.join(os.getcwd(), 'data')
MODELS_PATH = os.path.join(os.getcwd(), 'models')

st.title("Кредитный скоринг")


class StreamLitApp:
    def __init__(self):
        self.data = pd.read_csv(os.path.join(DATA_PATH, 'data.csv'))
        model_pickle = open(os.path.join(MODELS_PATH, 'model.pickle'), 'rb')
        self.model = pickle.load(model_pickle)
        self.data = self.data.drop("SeriousDlqin2yrs", axis=1)
        with st.form("Пользовательские вводы"):
            for column in self.data.columns:
                if len(self.data[column].unique()) < 10:
                    self.__setattr__(f"selected_{column}", st.selectbox(options=self.data[column].unique(), label=column))
                else:
                    self.__setattr__(f"selected_{column}", st.number_input(label=column, step=0.00001))
            st.form_submit_button()
        new_prediction = self.model.predict([[self.__getattribute__(f"selected_{column}") for column in self.data.columns]])
        st.write(f"Предсказание {new_prediction}")


st.session_state.my_instance = StreamLitApp()

"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st

class MultiApp:
    """Framework for combining multiple streamlit applications.
    """
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.

        """
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        app = st.sidebar.selectbox(
            'Selecione uma opção',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()
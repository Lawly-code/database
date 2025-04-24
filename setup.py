from setuptools import setup, find_packages

setup(
    name="lawly_db",
    version="0.2.1",
    author="VanekForest",
    author_email="zazc256@gmail.com",
    description="База данных для сайта Lawly",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Lawly-code/database",  # Ссылка на репозиторий
    packages=find_packages(),
    classifiers=[
    ],
    python_requires='>=3.11',
    install_requires=["sqlalchemy==2.0.40",
                      "asyncpg==0.30.0"]
)

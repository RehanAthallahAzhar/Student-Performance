FROM bitnami/spark:3.3.2

USER root

# Install Python & dependencies
RUN apt-get update && apt-get install -y python3 python3-pip && \
    pip3 install --upgrade pip && \
    pip3 install streamlit pandas pyspark

ENV SPARK_HOME=/opt/bitnami/spark
ENV PATH=$SPARK_HOME/bin:$PATH

WORKDIR /app
COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.enableCORS=false"]

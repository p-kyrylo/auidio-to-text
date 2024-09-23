# 
FROM nvidia/cuda:12.3.2-cudnn9-devel-ubuntu22.04

ENV NVIDIA_VISIBLE_DIVICES=all
# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt


#
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# 
COPY . /code

RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg
#
EXPOSE 8501

# 
ENTRYPOINT ["streamlit", "run", "original.py"]



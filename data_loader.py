import requests
import os


def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params={'id': id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, destination)


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None


def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)


def mkdir(path):
    is_exists = os.path.exists(path)
    # 判断结果
    if not is_exists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print
        path + ' 创建成功'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print
        path + ' 目录已存在'
        return False


if __name__ == "__main__":
    dir_data = 'classification/data/rec_news/'
    mkdir(dir_data)
    file_id = '1yDR3JxrJojhfgXbSWr8lOt27ANRHtwbP'
    destination = 'classification/data/rec_news/news_topic.json'
    download_file_from_google_drive(file_id, destination)
    file_id = '1N07oBDOdNXcb03vD5_OwFfzIghVBZbAv'
    destination = 'classification/data/rec_news/user_click_data.txt'
    download_file_from_google_drive(file_id, destination)

import boto3

session = boto3.session.Session()
s3 = session.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net'
)


def get_backet_list():
    for key in s3.list_objects(Bucket='into-the-wild-images')['Contents']:
        print(key['Key'])


def main():
    get_backet_list()


if __name__ == '__main__':
    main()

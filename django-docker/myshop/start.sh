#由于django3.0中utils移除了six，影响haystack使用
cp six.py /usr/local/lib/python3.7/site-packages/django/utils/
cp -r haystack/ /usr/local/lib/python3.7/site-packages/
python manage.py makemigrations && python manage.py migrate
supervisord -c /myshop/supervisord.conf
#supervisorctl
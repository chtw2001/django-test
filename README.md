# django-test

# users 폴더 생성후 INSTALLED_APPS에 추가하고 models.py에 모델을 정의하고 AUTH_USER_MODEL을 설정후
# makeigrations, migrate 하면 오류 발생 => 이미 모델이 만들어져있기 때문임 => sqlite3 삭제후 migrate
# sqlite3 extention 설치 후 createsuperuser => users_user에 만들어졌는지 확인
from subprocess import call

path = 'D:\IGOR\PYTHON\DJANGO_PROJ\Scripts\python'
makemigrations = '{} manage.py makemigrations'.format(path)
migrate = '{} manage.py migrate'.format(path)

if __name__ == '__main__':
    call(makemigrations, shell=True)
    call(migrate, shell=True)
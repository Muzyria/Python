def sourcetemplate(url):
    def func(**kwargs):
        if not kwargs:
            return url
        else:
            s = [f'{k}={v}' for k, v in sorted(kwargs.items())]
            return f"{url}?{'&'.join(s)}"
    return func


url = 'https://beegeek.ru'
load = sourcetemplate(url)
print(load(name='timur'))

url = 'https://stepik.org/lesson/651459/step/14'
load = sourcetemplate(url)
print(load(thread='solutions', unit=648165))

url = 'https://beegeek.ru'
load = sourcetemplate(url)
print(load())

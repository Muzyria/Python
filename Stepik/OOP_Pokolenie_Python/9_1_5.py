class DomainException(Exception):
    def __init__(self):
        super().__init__("Недопустимый домен, url или email")


class Domain:
    def __init__(self, domain):
        if not self.is_valid_domain(domain):
            raise DomainException()
        self.domain = domain

    @classmethod
    def from_url(cls, url):
        domain = cls.extract_domain_from_url(url)
        return cls(domain)

    @classmethod
    def from_email(cls, email):
        domain = cls.extract_domain_from_email(email)
        return cls(domain)

    def __str__(self):
        return self.domain

    @staticmethod
    def is_valid_domain(domain):
        # Проверяем, является ли домен корректным
        if len(domain) < 2 or domain.startswith('.') or domain.endswith('.') or '..' in domain:
            return False
        return all(c.isalpha() or c == '.' for c in domain)

    @staticmethod
    def extract_domain_from_url(url):
        # Извлекаем домен из url-адреса
        if url.startswith("http://") or url.startswith("https://"):
            domain = url.split('/')[2]
            return domain
        raise DomainException()

    @staticmethod
    def extract_domain_from_email(email):
        # Извлекаем домен из адреса электронной почты
        if '@' in email:
            _, domain = email.split('@')
            return domain
        raise DomainException()




domains = ['nikitin..biz', '.org', 'katren.', 'kubanskaja.edu.', '.', 'i.p.com', 'ooo.info+']

for d in domains:
    try:
        domain = Domain(d)
    except DomainException as e:
        print(e)
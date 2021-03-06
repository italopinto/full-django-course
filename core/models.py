from django.db import models


class ID(models.Model):  # -> example of one to one relationship
    number = models.CharField(
        verbose_name='Doc id',
        max_length=50,
        unique=True)

    def __str__(self):
        return self.number


class Client(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=70)
    last_name = models.CharField(
        verbose_name='Sobrenome',
        max_length=72,
        null=True)
    age = models.IntegerField(verbose_name='Idade')
    salary = models.DecimalField(
        verbose_name='Salario',
        max_digits=7,
        decimal_places=2)
    email = models.EmailField(verbose_name='E-mail', null=True, blank=True)
    photos = models.ImageField(
        verbose_name='Fotos',
        null=True,
        blank=True,
        upload_to='media/')
    dt_birth = models.DateField(
        verbose_name='Data de nascimento',
        null=True,
        blank=True)
    # -> CASCADE vai apagar o client se apagar o ID
    doc_id = models.OneToOneField(ID, null=True, on_delete=models.SET_NULL)
    # -> mas a ideia ainda prevalece, cada Client tem que ter apenas um ID, que sera so seu

    class Meta:
        verbose_name = 'Cliente'

    def __str__(self):
        return self.name + ' ' + self.last_name


class Product(models.Model):  # -> example of many to many
    description = models.CharField(verbose_name='Descricao', max_length=100)
    price = models.DecimalField(
        verbose_name='preco',
        max_digits=7,
        decimal_places=2)
    taxes = models.DecimalField(
        verbose_name='taxas',
        max_digits=7,
        decimal_places=2)

    class Meta:
        verbose_name = 'Produto'

    def __str__(self):
        return self.description


class Sale(models.Model):  # -> example of one to many (foreign key) relationship
    sale_number = models.CharField(
        verbose_name='Numero do vendedor',
        max_length=10,
        unique=True)
    # -> varios vendedores para um cliente
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(verbose_name='Data', auto_now_add=True)
    total = models.DecimalField(
        verbose_name='Total',
        max_digits=7,
        decimal_places=2)
    products = models.ManyToManyField(Product, blank=True)

    class Meta:
        verbose_name = 'Vendedor'

    def __str__(self):
        return self.sale_number

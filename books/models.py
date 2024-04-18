from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(max_length=1000, blank=True, null=True)


    def __str__(self):
        return self.name
    # bir nesnenin herhangi bir attiributeu çağırılmadan nesneyi çağırdığınızda ne görülsün istiyorsanız, nesneyi ne şekilde 
    #adlandırmak istiyorsanız, ne şekilde çağırmak istiyorsanız onu return etmek gerekiyor


    class Meta: # ek bilgi eklemek için kullanılır
        verbose_name = "Yazar"
        verbose_name_plural = "Yazarlar"


class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    

    class Meta: # ek bilgi eklemek için kullanılır
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"


# bu sayfa oluşturulduktan sonra admin py sayfasına tanıtılması gerekir.
# settings.py sayfasına books uygulamamızı tanıtmamız gerekir.



class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE) # yazar silindiğinde yazara ait tü kitaplar silinsin diye kullanılır.
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    description = models.TextField(max_length=1000, blank=True, null=True) # boş bırakmaya izin vermek için kullanılır.
    stock = models.IntegerField()
    price = models.FloatField()
    publication_date = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True) # auto now add otomatik olarak şuanın saatini ekler.
    activate = models.BooleanField(default=True)


    def __str__(self):
        return self.name
    

    class Meta: # ek bilgi eklemek için kullanılır
        verbose_name = "Kitap"
        verbose_name_plural = "Kitaplar"
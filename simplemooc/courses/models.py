from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse


#Customi
class CourseManager(models.Manager):
    def search(self, query):
        #Buscar pelo nome e descrição
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query)
        )

# Create your models here.
class Courses(models.Model):
    name = models.CharField('Nome',max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição',blank=True) #blacnk= true quer dizer campo não obrigatório
    start_date  = models.DateField('Data de Início',null=True, blank=True) #null=True sempre vai ter uma valor mesmoq que branco
    image = models.ImageField(upload_to='courses/image',verbose_name='Imagem',null=True, blank=True)
    created_at = models.DateField('Criado em',auto_now_add=True) #toda vez que for criado
    updated_at = models.DateField('Atualizado em ',auto_now=True)   #toda vez que for atualizado
    about = models.TextField('Sobre o Curso', blank=True)

    #não é mais o padrão, agora é customizado
    objects = CourseManager()

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('index:details', (), {'slug': self.slug})

    #Muda nome da classe no django admin
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']

class Enrollment(models.Model):
    STATUS_CHOICES = ((0,'Pendente'),(1,'Aprovado'),(2,'Cancelado'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='Usuário',related_name='enrollments')
    course = models.ForeignKey(Courses, verbose_name='Curso',related_name='enrollements')
    status = models.IntegerField('Situção',choices=STATUS_CHOICES, default=1, blank=True)
    created_at = models.DateField('Criado em', auto_now_add=True)  # toda vez que for criado
    updated_at = models.DateField('Atualizado em ', auto_now=True)  # toda vez que for atualizado

    def active(self):
        self.status = 1
        self.save()

    class Meta:
        verbose_name        = 'Inscrição'
        verbose_name_plural =  'Inscrições'
        unique_together     =   (('user','course')) #indice de unicidade
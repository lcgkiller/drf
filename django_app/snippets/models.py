from django.db import models

# Create your models here.
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)


# type(content) = bytes
# type(serializer) = snippets.serializers.SnippetSerializer
# type(serializer.data = rest_framework.uitls.serializer_helpers.ReturnDict
   # ReturnDict([('pk', 4),
   #          ('title', ''),
   #          ('code', 'foo = "bar"'),
   #          ('linenos', False),
   #          ('language', 'python'),
   #          ('style', 'friendly')])

# type(content) : bytes
    # b'{"pk":4,"title":"","code":"foo = \\"bar\\"","linenos":false,"language":"python","style":"friendly"}'

# stream = BytesIO(content) (파이썬 데이터를 파싱)
    # b'{"pk":4,"title":"","code":"foo = \\"bar\\"","linenos":false,"language":"python","style":"friendly"}'

# data = JSONParser().parse(stream)
    #     {'code': 'foo = "bar"',
    #      'language': 'python',
    #      'linenos': False,
    #      'pk': 4,
    #      'style': 'friendly',
    #      'title': ''}


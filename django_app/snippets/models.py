from django.db import models

# Create your models here.
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

from config import settings

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    # owner 필드를 추가하되, member app을 추가하고 CustomUser를 생성하고 User를 settings.AUTH_USER_MODEL을 참조하는 방식을 사용
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    highlighted = models.TextField() # HTML 코드가 들어가는 부분
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        """
        `pygments` 라이브러리를 사용하여 하이라이트된 코드를 만든다.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)

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


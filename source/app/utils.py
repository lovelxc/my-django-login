from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import re
class MyPasswordValidator:
    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        pattern = r'^(?![A-Za-z0-9]+$)(?![a-z0-9\\W]+$)(?![A-Za-z\\W]+$)(?![A-Z0-9\\W]+$)^.{8,}$'
        if re.search(pattern, password):
            raise ValidationError(
                _("你的密码没有包含大小写字母，数字和特殊符号"),
                code='password_num_char_daxiaoxiezimu',
            )

    def get_help_text(self):
        return _(
            "你的密码必须包含大小写字母，数字和特殊符号"
        )
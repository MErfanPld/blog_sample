from django.db import models
import uuid   
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import  PermissionsMixin , Group , AbstractUser 
from django.utils import timezone
from .usermanager import UserManager 
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

#from .managers import CustomUserManager

username_validator = UnicodeUsernameValidator()

class User(AbstractUser,PermissionsMixin):

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        db_table = "users"

    # general fields 
    last_login = models.DateTimeField(_('last login'), blank=True, null=True , default=timezone.now)
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier', blank=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="user_set",
        related_query_name="user",
    )


    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
        help_text=_(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(default=timezone.now , editable=False, blank=True)
    
    
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },    
    )
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    password = models.CharField(max_length=128 , blank=False)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=11 , blank=True)
    
    
    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_role(self):
        return self.role
    
    def get_group(self):
        return self.groups
    
    def get_username(self) :
        return self.username
    
    def get_password(self) :
        return self.password

    
    USERNAME_FIELD = 'username'
    objects = UserManager()    
    #filter_horizontal = ('username',)
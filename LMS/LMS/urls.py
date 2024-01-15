from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.models import User

from django_otp.admin import OTPAdminSite
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin

class OTPAdmin(OTPAdminSite):
    pass

# Create an instance of your custom admin site
admin_site = OTPAdmin(name='OTPAdmin')

# Register User and TOTPDevice with your custom admin site
admin_site.register(User)
admin_site.register(TOTPDevice, TOTPDeviceAdmin)

urlpatterns = [
    path('admin/', admin_site.urls),  # Use your custom admin site
    path('dadmin/', admin.site.urls),  # Use the default admin site
    path('', include('lmsapp.urls')),
]

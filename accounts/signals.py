from django.dispatch import Signal
from django.dispatch import receiver

certified_update= Signal(providing_args=['request', 'user'])

@receiver(certified_update)
def certified_update(sender, user, request,**kwargs):
    print("시작")
    user.profile.is_certified=False
    user.profile.save()
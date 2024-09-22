from django.core.management.base import BaseCommand

from .signal_handlers import invalidate_cached_agreements


class Command(BaseCommand):
    help = "Invalidate all TOS agreements"

    def handle(self, *args, **kwargs):
        invalidate_cached_agreements()
        self.stdout.write(self.style.SUCCESS("Successfully invalidated cached TOS agreements"))

from django.core.management.base import BaseCommand
import requests

class Command(BaseCommand):
    help = "Purge all LiteSpeed cache"

    def handle(self, *args, **options):
        r = requests.request(
            "PURGE",
            "http://localhost",
            headers={"X-LiteSpeed-Purge": "*"}
        )
        self.stdout.write(self.style.SUCCESS("LSCache purged"))

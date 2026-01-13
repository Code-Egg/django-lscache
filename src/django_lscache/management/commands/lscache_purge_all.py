from django.core.management.base import BaseCommand
from django_lscache.purging import purge_all

class Command(BaseCommand):
    help = "Purge all LiteSpeed cache URLs"

    def handle(self, *args, **kwargs):
        urls = ["/", "/about/"]  # Example: customize as needed
        server_host = "http://localhost"
        status = purge_all(urls, server_host)
        self.stdout.write(f"Purged URLs with status {status}")

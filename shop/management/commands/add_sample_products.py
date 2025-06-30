from django.core.management.base import BaseCommand
from shop.models import Product

class Command(BaseCommand):
    help = 'Add sample products to the database'

    def handle(self, *args, **kwargs):
        samples = [
            {'name': 'Wireless Headphones', 'description': 'High-quality wireless headphones with noise cancellation.', 'price': 99.99},
            {'name': 'Smart Watch', 'description': 'Track your fitness and notifications with this stylish smart watch.', 'price': 149.99},
            {'name': 'Bluetooth Speaker', 'description': 'Portable speaker with deep bass and long battery life.', 'price': 59.99},
            {'name': 'Gaming Mouse', 'description': 'Ergonomic mouse with customizable buttons and RGB lighting.', 'price': 39.99},
            {'name': '4K Monitor', 'description': 'Ultra HD monitor for stunning visuals and productivity.', 'price': 299.99},
        ]
        for prod in samples:
            Product.objects.get_or_create(name=prod['name'], defaults=prod)
        self.stdout.write(self.style.SUCCESS('Sample products added!')) 
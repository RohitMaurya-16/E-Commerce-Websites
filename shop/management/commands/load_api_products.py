import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from shop.models import Product

class Command(BaseCommand):
    help = 'Load products from fakestoreapi.com'

    def handle(self, *args, **kwargs):
        self.stdout.write("Fetching products from API...")
        try:
            response = requests.get('https://fakestoreapi.com/products')
            response.raise_for_status()  # Raise an exception for bad status codes
            products = response.json()
        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f"Failed to fetch products: {e}"))
            return

        self.stdout.write(f"Found {len(products)} products. Starting import...")

        # Category mapping from API to our model's choices
        category_map = {
            "men's clothing": "other",
            "women's clothing": "other",
            "jewelery": "accessories",
            "electronics": "electronics"
        }

        for api_product in products:
            # Map API category to our choices, default to 'other'
            api_category = api_product.get('category', 'other')
            product_category = category_map.get(api_category, 'other')

            # Use get_or_create to avoid duplicates
            product, created = Product.objects.get_or_create(
                name=api_product['title'],
                defaults={
                    'description': api_product.get('description', ''),
                    'price': api_product.get('price', 0.0),
                    'category': product_category,
                }
            )

            if created:
                self.stdout.write(f"Created product: {product.name}")
                # Handle image download
                image_url = api_product.get('image')
                if image_url:
                    try:
                        img_response = requests.get(image_url)
                        img_response.raise_for_status()
                        img_name = image_url.split('/')[-1]
                        product.image.save(img_name, ContentFile(img_response.content), save=True)
                        self.stdout.write(f"  > Image downloaded for {product.name}")
                    except requests.exceptions.RequestException as e:
                        self.stdout.write(self.style.WARNING(f"  > Could not download image for {product.name}: {e}"))
            else:
                self.stdout.write(self.style.WARNING(f"Product already exists: {product.name}. Skipping."))

        self.stdout.write(self.style.SUCCESS("Product import complete!")) 
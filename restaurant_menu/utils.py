def dich_image_path(instance, filename):
    """Задаем путь и название для изображения блюда."""
    ext = str(filename).split('.')[-1]
    return f'dish_images/{instance.name}_image.{ext}'

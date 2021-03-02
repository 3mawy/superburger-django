from django.test import TestCase
from api.models import MenuItem


# Create your tests here.

class MenuItemModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        MenuItem.objects.create(name='name here', description='description here', ingredients='ingredients here',
                                active=True, category='category here', sizes='L')

    def test_menu_item_content(self):
        menu_item = MenuItem.objects.get(id=1)
        name = f'{menu_item.description}'
        description = f'{menu_item.description}'
        ingredients = f'{menu_item.description}'
        active = f'{menu_item.description}'
        category = f'{menu_item.description}'
        sizes = f'{menu_item.description}'

        self.assertEquals(name, 'name here')
        self.assertEquals(description, 'description here')
        self.assertEquals(ingredients, 'ingredients here')
        self.assertTrue(active)
        self.assertEquals(category, 'category here')
        self.assertEquals(sizes, 'L')

    # def test_name_content(self):
    #     menu_item = MenuItem.objects.get(id=1)
    #     expected_object_name = f'{menu_item.title}'
    #     self.assertEquals(expected_object_name, 'item')
    #
    # def test_description_content(self):
    #     menu_item = MenuItem.objects.get(id=1)
    #     expected_object_name = f'{menu_item.description}'
    #     self.assertEquals(expected_object_name, 'description here')

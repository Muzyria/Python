locators = {1: {'name_product': '//a[@id="item_4_title_link"]',
                'price_product': '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div',
                'button_product': '//button[@id="add-to-cart-sauce-labs-backpack"]'},
            2: {},
            3: {},
            4: {},
            5: {},
            6: {}}

n = int(input())
print(locators[n]['name_product'])
print(locators[n]['price_product'])
print(locators[n]['button_product'])
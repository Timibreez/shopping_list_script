class Product():
    def __init__(self, name, description, price, seller, available=True):
        self.name = name
        self.description = description
        self.price = price
        self.seller = seller
        self.available = available
        self.reviews = []

    def __str__(self):
        return f'Product({self.name}, {self.description}, at ${self.price})'

class Review():
    def __init__(self, content, user, product):
        self.content = content
        self.user = user
        self.product = product

    def __str__(self):
        return 'Review by {self.user} of {self.product}'

class User():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.reviews = []

    def sell_product(self, name, description, price):
        product = Product(name, description, price, self, available=True)
        print(f'{product} is on the market!')
        return product

    def buy_product(self, product):
        if product.available:
            print(f'{self} is buying {product}')
            product.available = False
        else:
            print(f'{product} is no longer available')

    def write_review(self, content, product):
        review = Review(content, self, product)
        self.reviews.append(review)
        product.reviews.append(review)
        print(f"{self.name}'s review of {product.name}: {review.content}")
        return review

    def __str__(self):
        return f'User(id= {self.id}, name= {self.name})'

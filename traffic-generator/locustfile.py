from locust import HttpLocust, TaskSet, task, TaskSequence, seq_task, Locust
import random

users = ["eric", "phoebe", "dwight", "han"] ##User 'rob' does not exist. This to simulate a failure with incorrect user auth

products = []

userid = ""


def my_task(l):
    print("hello")

def new_task(l):
    print("new hello")

class GuestUserBrowsing(TaskSequence):

    def on_start(self):
        self.getProducts()

    @task
    def getProducts(self):
        print("Guest User - Get Products")
        self.client.get("/products")

class AuthUserBrowsing(TaskSequence):

    def on_start(self):
        self.login()

    #def on_stop(self):
     #   self.logout()
    
   # @seq_task(1)
    @task(1)
    def login(self):
        user = random.choice(users)
        body = self.client.post("/login/", json={"username": user, "password":"vmware1!"}).json()
        userid = body["token"]

    #@seq_task(2)
    @task(1)
    def getProducts(self):
        self.client.get("/products").json()["data"]

    #@seq_task(3)
    @task(2)
    def getProduct(self):
        print("Auth User - Getting products")
        products = self.listCatalogItems()
        id = random.choice(products)
        product = self.client.get("/products/"+ id).json()
        products.clear()

    
    # @seq_task(4)
    # @task(4)
    # def addToCart(self):
    #     self.listCatalogItems()
    #     productid = random.choice(products)
    #     cart = self.client.post("/cart/item/add/" + userid, json={
    #               "name": "test_" + productid,
    #               "price": "100",
    #               "shortDescription": "Test add to cart",
    #               "quantity": random.randint(1,4),
    #               "itemid": productid
    #             })
    #     print(cart)

    def listCatalogItems(self):
        items = self.client.get("/products").json()["data"]
        for item in items:
            products.append(item["id"])
        return products

    @task(2)
    def index(self):
        self.client.get("/")


class UserBehavior(TaskSet):
    tasks = {AuthUserBrowsing:1, GuestUserBrowsing:2}
    #tasks = {my_task:1, new_task:2}

class WebSiteUser(HttpLocust):

    task_set = UserBehavior
    min_wait = 2000
    max_wait = 10000
    



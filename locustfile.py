from locust import HttpUser, task, between

class QuickstartUser(HttpUser):

    @task()
    def add(self):
        for a in range(0,10):
            self.client.get(f"/calc/add?a={a}&b=9", name = "Calc Add Endpoint")
        
    @task()
    def sub(self):
        for a in range(0,10):
            self.client.get(f"/calc/sub?a={51}&b={a}", name = "Calc Sub Endpoint")

    @task()
    def mul(self):
        for a in range(0,10):
            self.client.get(f"/calc/mul?a={51}&b={a}", name = "Calc mul Endpoint")
    
    @task()
    def div(self):
        for a in range(0,10):
            for b in range(0,10):
                self.client.get(f"/calc/div?a={a}&b={b}", name = "Calc div Endpoint")

    @task()
    def mod(self):
        for a in range(0, 30):
            self.client.get(f"/calc/div?a={a}&b={2}", name = "Calc mod Endpoint")
    
    @task()
    def random(self):
        for a in range(0,10):
            for b in range(a,30):
                self.client.get(f"/calc/random?a={a}&b={b}", name = "Calc random Endpoint")
        
    @task()
    def concat(self):
        strings = ["g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]
        for string in strings:
            self.client.get(f"/str/concat?a={string}&b=abcdef", name = "Calc concat Endpoint")

    @task()
    def upper(self):
        to_upper = ["abcd", "efgh", "ijkl", "mnop", "qrst", "uvwx", "yz"]
        for string in to_upper:
            self.client.get(f"/str/upper?a={string}", name = "Calc upper Endpoint")

    @task()
    def lower(self):
        to_lower= ["abcd", "efgh", "ijkl", "mnop", "qrst", "uvwx", "yz"]
        for string in to_lower:
            self.client.get(f"/str/upper?a={string}", name = "Calc lower Endpoint")

import requests


class CatFacts:
    def __init__(self,request) -> None:
        self.request = request

    def provide(self):
        return f"Cat fact: {self._get_cat_fact()['fact']}"

    # Again, don't stub this method.
    def _get_cat_fact(self):
        response = self.request.get("https://catfact.ninja/fact")
        return response.json()


cat_fact = CatFacts(requests)

print(cat_fact.provide())
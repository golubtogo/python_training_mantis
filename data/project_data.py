import random
import string
from fixture.project import Project


def random_status():
    status_list = ["в разработке", "выпущен", "стабильный", "устарел"]
    status = random.choice(status_list)
    return status


def random_view_state():
    view_state_list = ["публичный", "приватный"]
    view_state = random.choice(view_state_list)
    return view_state


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*2
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Project(name=random_string("name1", 10), status=random_status(), view_state=random_view_state(),
            description=random_string("description1", 20))
    for i in range(1)
]


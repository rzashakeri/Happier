from factory.django import DjangoModelFactory

from post.models import Post
from user.tests.fixtures import UserFactory


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    user = UserFactory()
    caption = """
    Lorem ipsum dolor sit amet arcu 
    suspendisse litora habitasse ridiculus 
    enim aliquam non iaculis egestas laoreet 
    dis nostra quis aenean justo orci imperdiet 
    semper ipsum nunc finibus netus mi ex accumsan
    """


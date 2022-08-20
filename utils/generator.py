import time
import uuid

from ulid import monotonic as ulid

system_time = time.time()


def hex_uuid():
    return uuid.uuid4().hex


def user_directory_path(instance, filename):
    filename, extension = filename.split(".")
    if extension in ["png", "jpeg", "heic", "heif", "jpg"]:
        return "post/image/{0}.{1}".format(str(uuid.uuid4().hex), extension)
    elif extension in ["mp4"]:
        return "post/video/{0}.{1}".format(str(uuid.uuid4().hex), extension)
    elif extension in ["mp3"]:
        return "post/audio/{0}.{1}".format(str(uuid.uuid4().hex), extension)


def generate_unique_id():
    unique_id = ulid.from_timestamp(system_time).str
    return unique_id

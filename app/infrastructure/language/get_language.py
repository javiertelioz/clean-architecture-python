from fastapi import Header


def get_language(accept_language: str = Header(default="en")):
    languages = accept_language.split(",")
    return languages[0]

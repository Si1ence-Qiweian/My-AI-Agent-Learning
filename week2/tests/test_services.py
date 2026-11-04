from article_explorer.services import (
    count_articles,
    extract_bodies,
    extract_titles,
)

POSTS = [
    {"title": "Python", "body": "Learning Python"},
    {"title": "Agent", "body": "Learning Agent"},
]


def test_extract_titles():
    assert extract_titles(POSTS) == ["Python", "Agent"]


def test_extract_bodies():
    assert extract_bodies(POSTS) == ["Learning Python", "Learning Agent"]


def test_count_articles():
    assert count_articles(POSTS) == 2


def test_count_empty_articles():
    assert count_articles([]) == 0
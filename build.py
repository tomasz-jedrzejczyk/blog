"""Static blog builder.

Reads Markdown posts from posts/, renders them with the templates in
templates/, and writes a static HTML site to output/.
"""

import shutil
from dataclasses import dataclass
from pathlib import Path

import markdown
from jinja2 import Environment, FileSystemLoader

POSTS_DIR = Path("posts")
TEMPLATES_DIR = Path("templates")
STATIC_DIR = Path("static")
OUTPUT_DIR = Path("output")


@dataclass
class Post:
    title: str
    date: str
    slug: str
    html: str


def parse_post(path: Path) -> Post:
    text = path.read_text(encoding="utf-8")

    if not text.startswith("---"):
        raise ValueError(f"{path} is missing frontmatter")

    _, frontmatter, body = text.split("---", 2)

    metadata = {}
    for line in frontmatter.strip().splitlines():
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip()

    slug = path.stem  # e.g. "2026-09-14-hello-world"
    html = markdown.markdown(body.strip())

    return Post(title=metadata["title"], date=metadata["date"], slug=slug, html=html)


def build() -> None:
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir()

    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

    posts = [parse_post(p) for p in sorted(POSTS_DIR.glob("*.md"), reverse=True)]

    index_template = env.get_template("index.html")
    (OUTPUT_DIR / "index.html").write_text(
        index_template.render(posts=posts), encoding="utf-8"
    )

    post_template = env.get_template("post.html")
    for post in posts:
        out_path = OUTPUT_DIR / f"{post.slug}.html"
        out_path.write_text(post_template.render(post=post), encoding="utf-8")

    shutil.copytree(STATIC_DIR, OUTPUT_DIR / "static")

    print(f"Built {len(posts)} post(s) into {OUTPUT_DIR}/")


if __name__ == "__main__":
    build()

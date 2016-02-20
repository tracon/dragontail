# Dragontail CMS Enterprise Edition

Dragontail is the Wagtail-based successor to TraContent, the content management system that brought Tracon to light from the darkness of Wordpress, Drupal and PencilBlue.

## What's the relation of Dragontail and Wagtail?

While **Wagtail** is advertised as a content management system (CMS), a more apt description would be a _CMS construction kit_. The Wagtail developers appreciate the fact that no two sites are identical and sites often have wildly differing requirements.

Wagtail therefore does not provide basic concepts such as "content page" or "blog post", but gives the developer excellent tools to create just the kind of content pages and blog posts the developer wants.

**Dragontail**, on the other hand, is an _opinionated batteries-included CMS_ that uses Wagtail and implements basic building blocks for an actual site using the tools provided by Wagtail. Dragontail builds on the experience gained while developing TraContent and also shares many architectural choices with it.

## Dragontail vs. TraContent

| Feature | TraContent | Dragontail |
|---------|------------|------------|
| Python version | 2.7, 3.4 or 3.5 | 3.4 or 3.5 |
| Framework | Django 1.9 | Django 1.9 |
| Base CMS | None | Wagtail |
| Admin UI | Django Admin | Wagtail |
| Rich Text Editor | CKEditor | Wagtail |
| File Management | CKEditor | Wagtail |

## Standard Edition vs. Enterprise Edition

Here's a cool feature matrix:

| Feature | Standard Edition | Enterprise Edition |
|---------|------------------|--------------------|
| License | MIT | MIT |
| Price | Free | Free |
| Support | Purchased separately | Purchased separately |
| Multisite support | Yes (always on) | Yes (always on) |
| OAuth2 authentication | No | Yes |

### No, really, what's the difference?

If you have Kompassi OAuth2 support enabled, you're running the Enterprise Edition. Because starships, that's why :)

## Getting started

Install dependencies:

    virtualenv venv-tracontent
    source venv-tracontent/bin/activate
    git clone https://github.com/tracon/tracontent.git
    cd tracontent
    pip install -r requirements.txt

Setup basic example content:

    ./manage.py setup
    ./manage.py setup_tracon11 127.0.0.1:8001

Run the server and view the site in your favourite web browser:

    ./manage.py runserver 127.0.0.1:8001
    iexplore http://127.0.0.1:8001
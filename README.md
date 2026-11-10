# Salon Polo & Barbershop website

Static, SEO-first website for Salon Polo & Barbershop, 626 Admiral Drive, Suite E, Annapolis, MD 21401.

Every page is plain, pre-rendered HTML in its own folder (clean URLs like `/services/skin-fades/`), with its own title, description, canonical URL, Open Graph tags and schema.org structured data. JavaScript is only used for the live Google rating on the home page.

## Pages

| URL | Page |
| --- | --- |
| `/` | Home |
| `/services/` | All services and the full menu |
| `/services/mens-haircuts/` · `/skin-fades/` · `/hot-towel-shaves/` · `/beard-trims/` · `/gray-blending/` | One page per service |
| `/team/` | Team |
| `/team/alexis/` · `/team/amber/` · `/team/colette/` | One page per stylist |
| `/contact/` | Hours, directions, cancellation policy, FAQ |
| `/join-our-team/` | Careers |
| `/privacyterms/` | Privacy & terms |
| `/ourteam/` | Old Squarespace address, forwards to `/team/` |

Plus `sitemap.xml`, `robots.txt` and `404.html`.

## Editing

All text lives in `_src/build.py` (services, team bios, hours, phone, etc.). After changing it, rebuild from this folder:

```
python3 _src/build.py
```

Styles are in `assets/site.css`; images in `assets/img/`.

## When salonpolo.com is switched to this site

1. In `_src/build.py`, set `BASE_PATH = "/"` and rebuild.
2. Add a `CNAME` file containing `www.salonpolo.com`.
3. Submit `https://www.salonpolo.com/sitemap.xml` in Google Search Console.

from get_sitemaps import get_sitemap_urls
import produto
import categoria

sitemap_urls = get_sitemap_urls()

categoria.main(sitemap_urls)
produto.main(sitemap_urls)

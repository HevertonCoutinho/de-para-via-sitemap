import subprocess

cliente  = input("Qual cliente: ")

if cliente == "elastobor":

    def get_sitemap_urls():
        return ['https://www.elastobor.com.br/sitemap/subcategory-0.xml', 'https://www.elastobor.com.br/sitemap/category-0.xml', 'https://www.elastobor.com.br/sitemap/brand-0.xml', 'https://www.elastobor.com.br/sitemap/department-0.xml', 'https://www.elastobor.com.br/sitemap/product-0.xml', 'https://www.elastobor.com.br/sitemap/product-1.xml', 'https://www.elastobor.com.br/sitemap/product-2.xml']

elif cliente == "nwdrones":

    def get_sitemap_urls():
        return ['https://www.nwdrones.com.br/pub/media/sitemap.xml']

elif cliente == "sonco":

    def get_sitemap_urls():
        return ['https://www.soncocrowdcontrol.com/sitemap.xml']

else: 

    print("Sitemap não existe")


import subprocess


cliente  = input("Qual cliente: ")

if cliente == "elastobor":

    def get_sitemap_urls():
        return ['https://www.elastobor.com.br/sitemap/brand-1.xml', 'https://www.elastobor.com.br/sitemap/category-1.xml','https://www.elastobor.com.br/sitemap/category-2.xml', 'https://www.elastobor.com.br/sitemap/product-1.xml','https://www.elastobor.com.br/sitemap/product-10.xml', 'https://www.elastobor.com.br/sitemap/product-11.xml', 'https://www.elastobor.com.br/sitemap/product-12.xml', 'https://www.elastobor.com.br/sitemap/product-13.xml', 'https://www.elastobor.com.br/sitemap/product-13.xml', 'https://www.elastobor.com.br/sitemap/product-15.xml', 'https://www.elastobor.com.br/sitemap/product-16.xml', 'https://www.elastobor.com.br/sitemap/product-2.xml', 'https://www.elastobor.com.br/sitemap/product-3.xml', 'https://www.elastobor.com.br/sitemap/product-4.xml', 'https://www.elastobor.com.br/sitemap/product-5.xml', 'https://www.elastobor.com.br/sitemap/product-6.xml', 'https://www.elastobor.com.br/sitemap/product-7.xml', 'https://www.elastobor.com.br/sitemap/product-8.xml', 'https://www.elastobor.com.br/sitemap/product-9.xml']

elif cliente == "nwdrones":

    def get_sitemap_urls():
        return ['https://www.nwdrones.com.br/pub/media/sitemap.xml']

elif cliente == "sonco":

    def get_sitemap_urls():
        return ['https://www.soncocrowdcontrol.com/sitemap.xml']

else: 


    print("Sitemap não existe")


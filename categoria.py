import csv
import requests
import xml.etree.ElementTree as ET
from urllib.parse import urlparse

def main(sitemap_urls):
    
    urls2 = []
    for sitemap_url in sitemap_urls:
        sitemap_response = requests.get(sitemap_url)
        sitemap_xml = ET.fromstring(sitemap_response.text)
        for url in sitemap_xml.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
            loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text
            urls2.append(loc)
        print(sitemap_response)

    # Lendo URLs do arquivo CSV
    with open('categories404.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        urls1 = [row[0] for row in reader]

    # Dicionário para armazenar as palavras após o domínio de cada URL
    url_dict1 = {}
    for url in urls1:
        parsed_url = urlparse(url)
        path = parsed_url.path.strip('/')
        if '/' in path:
            path = path.split('/')
        else:
            path = path.split('-')
        url_dict1[url] = path

    url_dict2 = {}
    for url in urls2:
        parsed_url = urlparse(url)
        path = parsed_url.path.strip('/')
        if '/' in path:
            path = path.split('/')
        else:
            path = path.split('-')
        url_dict2[url] = path

    # Dicionário para armazenar as URLs semelhantes
    matches_dict = {}

    # Comparar as URLs
    for url1, words1 in url_dict1.items():
        max_similarity = 0
        most_similar_url = None
        for url2, words2 in url_dict2.items():
            if words1[0] == words2[0]:
                similarity = len(set(words1[1:]).intersection(set(words2[1:])))
                if similarity > max_similarity:
                    max_similarity = similarity
                    most_similar_url = url2
        if most_similar_url:
            matches_dict[url1] = most_similar_url
            print(f"Match encontrado para {url1}: {most_similar_url}")

    # Escrever as URLs semelhantes em um arquivo CSV
    with open('de-para-categorias.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['DE', 'PARA', 'MENSAGEM'])
        for url1, url2 in matches_dict.items():
            mensagem = ""
            if url1 == url2:
                mensagem = "URLs idênticas, possível retorno da categoria"
            else:
                parsed_url1 = urlparse(url1)
                parsed_url2 = urlparse(url2)
                path1 = parsed_url1.path.strip('/')
                path2 = parsed_url2.path.strip('/')
                words1 = path1.split('-')
                words2 = path2.split('-')
                if words1[0] != words2[0]:
                    mensagem = "Possível erro devido a baixa similaridade"
            writer.writerow([url1, url2, mensagem])
if __name__ == "__main__":
    main()

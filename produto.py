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
    with open('products404.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        urls1 = [row[0] for row in reader]

    # Dicionário para armazenar a URL mais semelhante para cada URL do arquivo CSV
    matches = {}

    # Comparar as URLs
    for url1 in urls1:
        parsed_url1 = urlparse(url1)
        path1 = parsed_url1.path.strip('/')
        words1 = path1.split('-')

        best_match = None
        best_similarity = 0

        for url2 in urls2:
            parsed_url2 = urlparse(url2)
            path2 = parsed_url2.path.strip('/')
            words2 = path2.split('-')

            if words1[0] == words2[0]:
                common_words = set(words1[1:]) & set(words2[1:])
                if common_words:
                    similarity = len(common_words) / len(set(words1[1:]))
                else:
                    similarity = 0  # Define a similaridade como 0 se não houver palavras em comum
                if similarity > best_similarity:
                    best_match = url2
                    best_similarity = similarity

        if best_match is not None:
            matches[url1] = best_match
            print(f"Match encontrado para {url1}: {best_match}")

    # Escrever as URLs semelhantes em um arquivo CSV
    with open('de-para-produtos.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['DE', 'PARA', 'MENSAGEM'])
        for url1, url2 in matches.items():
            mensagem = ""
            if url1 == url2:
                mensagem = "URLs idênticas, possível retorno ao estoque"
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

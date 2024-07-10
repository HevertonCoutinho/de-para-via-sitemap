# Redirecionamento DE/PARA URLs do Sitemap para Ecommerce
Este programa em Python facilita o redirecionamento de URLs 404 para categorias e produtos em um ecommerce, usando URLs de sitemaps para encontrar correspondências semelhantes.

## categoria.py
Este script compara URLs de categorias 404 com URLs do sitemap para encontrar correspondências próximas.

### Como Usar
1. **Preparação**:
   - Certifique-se de ter Python instalado em seu ambiente.
   - Configure o arquivo CSV `categories404.csv` contendo URLs de categorias 404.
   - Especifique os URLs dos sitemaps em `sitemap_urls` dentro do script.

2. **Execução do Script**:
   - Abra o arquivo `categoria.py` em um editor de código.
   - Execute o script usando:
     ```
     python categoria.py
     ```

3. **Resultado**:
   - O script irá baixar os sitemaps especificados, comparar as URLs de categorias 404 com as URLs do sitemap, gerar um arquivo `de-para-categorias.csv` com os pares correspondentes e uma mensagem indicando a similaridade ou possíveis erros.

## produto.py
Este script compara URLs de produtos 404 com URLs do sitemap para encontrar correspondências próximas.

### Como Usar
1. **Preparação**:
   - Certifique-se de ter Python instalado em seu ambiente.
   - Configure o arquivo CSV `products404.csv` contendo URLs de produtos 404.
   - Especifique os URLs dos sitemaps em `sitemap_urls` dentro do script.

2. **Execução do Script**:
   - Abra o arquivo `produto.py` em um editor de código.
   - Execute o script usando:
     ```
     python produto.py
     ```

3. **Resultado**:
   - O script irá baixar os sitemaps especificados, comparar as URLs de produtos 404 com as URLs do sitemap, gerar um arquivo `de-para-produtos.csv` com os pares correspondentes e uma mensagem indicando a similaridade ou possíveis erros.

### Contribuição

Sinta-se à vontade para contribuir com melhorias através de pull requests.

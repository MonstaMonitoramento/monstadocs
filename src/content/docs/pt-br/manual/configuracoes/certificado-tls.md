---
title: "Certificado TLS"
sidebar:
  order: 14
---

A tela de gerenciamento de certificados TLS permite que você configure e gerencie os certificados digitais utilizados para proteger as comunicações do seu software, garantindo a segurança e a privacidade dos dados transmitidos.

A seguir são especificados os métodos disponíveis.

## Let's Encrypt

![image-1755089232881.png](../../../../../assets/images/p79_image-1755089232881.png)

Marque este método para habilitar o uso do *Let's Encrypt*. O *Let's Encrypt* é uma Autoridade Certificadora (AC) gratuita e automatizada que permite obter certificados TLS/SSL de forma fácil e rápida. Uma vez habilitado, o Monsta se encarrega de renovar o certificado.

:::caution[Importante]
Este método necessita instalar o certbot no Linux onde o Monsta está instalado. Certifique-se de que o seu servidor possui acesso a internet.
:::

| Opção | Descrição |
| :--- | :--- |
| ![image-1755089526369.png](../../../../../assets/images/p79_OLpimage-1755089526369.png) | **Comando**: Informa onde o software do certbot deve estar instalado. |
| ![image-1755089721901.png](../../../../../assets/images/p79_image-1755089721901.png) | **Domínio**: Permite ao usuário informar o(s) domínio(s) pelo qual o Monsta irá responder. <aside class="starlight-aside starlight-aside--caution"><p class="starlight-aside__title">Atenção</p>Certifique-se de que a url informada tenha acesso à porta 80/TCP no Monsta pois o certbot utiliza essa comunicação para gerar e renovar o(s) certificado(s).</aside> |
| ![image-1755089819102.png](../../../../../assets/images/p79_image-1755089819102.png) | **E-mail**: O Letsencrypt necessita de um endereço de e-mail para contato. Informe um e-mail de sua propriedade. |



## Certificado Monsta

![image-1755090094058.png](../../../../../assets/images/p79_image-1755090094058.png)

Selecione este método gerar um novo certificado autoassinado. Um certificado autoassinado é um certificado digital que é assinado pela própria Monsta. Ele é útil para ambientes de teste ou para uso interno, mas não é recomendado para ambientes de produção, pois não oferece o mesmo nível de confiança que um certificado emitido por uma Autoridade Certificadora (AC) confiável.

## Certificado Próprio

![image-1755090175256.png](../../../../../assets/images/p79_image-1755090175256.png)

Se a sua empresa já possui um certificado disponível para utilização, utilize essa opção para fazer o upload destes arquivos. O Monsta aceita apenas chaves **RSA** codificadas no formato **PEM**.


| Opção | Descrição |
| :--- | :--- |
| ![image-1755090193642.png](../../../../../assets/images/p79_image-1755090193642.png) | **Public Key**: É a chave que irá criptografar os dados enviados do navegador ao servidor do Monsta. Utilize este campo para fazer o upload do arquivo. |
| ![image-1755090205657.png](../../../../../assets/images/p79_image-1755090205657.png) | **Private Key**: É a chave que descriptografa as informações vindas da chave pública. Utilize este campo para fazer o upload do respectivo arquivo. |

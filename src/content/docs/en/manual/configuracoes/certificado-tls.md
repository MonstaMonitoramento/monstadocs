---
title: "TLS Certificate"
sidebar:
  order: 14
---

The TLS certificate management screen allows you to configure and manage the digital certificates used to secure your software's communications, ensuring the security and privacy of transmitted data.

The available methods are described below.

## Let's Encrypt

![image-1755089232881.png](../../../../../assets/images/p79_image-1755089232881.png)

Select this method to enable the use of *Let's Encrypt*. *Let's Encrypt* is a free, automated Certificate Authority (CA) that allows you to obtain TLS/SSL certificates easily and quickly. Once enabled, Monsta will handle renewing the certificate.

:::caution[Important]
This method requires installing certbot on the Linux system where Monsta is installed. Make sure your server has internet access.
:::

| Opção | Descrição |
| :--- | :--- |
| ![image-1755089526369.png](../../../../../assets/images/p79_OLpimage-1755089526369.png) | **Command**: Indicates where the certbot software should be installed. |
| ![image-1755089721901.png](../../../../../assets/images/p79_image-1755089721901.png) | **Domain**: Allows the user to enter the domain(s) for which Monsta will respond. <aside class="starlight-aside starlight-aside--caution"><p class="starlight-aside__title">Attention</p>Ensure that the provided URL has access to port 80/TCP on Monsta because certbot uses this communication to generate and renew the certificate(s).</aside> |
| ![image-1755089819102.png](../../../../../assets/images/p79_image-1755089819102.png) | **E-mail**: Let's Encrypt requires a contact email address. Provide an email address that you own. |



## Certificado Monsta

![image-1755090094058.png](../../../../../assets/images/p79_image-1755090094058.png)

Select this method to generate a new self-signed certificate. A self-signed certificate is a digital certificate that is signed by Monsta itself. It is useful for testing environments or internal use, but it is not recommended for production environments, as it does not offer the same level of trust as a certificate issued by a trusted Certificate Authority (CA).

## Custom Certificate

![image-1755090175256.png](../../../../../assets/images/p79_image-1755090175256.png)

If your company already has a certificate available for use, use this option to upload those files. Monsta accepts only **RSA** keys encoded in **PEM** format.


| Opção | Descrição |
| :--- | :--- |
| ![image-1755090193642.png](../../../../../assets/images/p79_image-1755090193642.png) | **Public Key**: It is the key that will encrypt data sent from the browser to the Monsta server. Use this field to upload the file. |
| ![image-1755090205657.png](../../../../../assets/images/p79_image-1755090205657.png) | **Private Key**: It is the key that decrypts the information from the public key. Use this field to upload the corresponding file. |
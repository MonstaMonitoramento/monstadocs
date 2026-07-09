---
title: "Resetar a senha de root: Debian"
sidebar:
  order: 6
---

A senha de root pode ser redefinida usando o menu do **GRUB** (Grand Unified Bootloader) para iniciar o sistema em modo de usuário único (*single-user mode*) ou com um *shell* de recuperação.

## Pré-requisitos

- Acesso físico ao console do servidor/máquina.
- O sistema operacional Debian deve usar o **GRUB** como *bootloader*.

## Passo a Passo para Resetar a Senha

### 1. Acessar o Menu do GRUB

1. **Reinicie** o seu sistema Debian.
2. Aguarde o menu do GRUB ser exibido na tela;
3. Use as teclas de seta (↑ e ↓) para selecionar a entrada do kernel padrão do Debian (geralmente a primeira opção).

### 2. Editar os Parâmetros de Inicialização

1. Pressione a tecla `e` para editar os comandos de inicialização da entrada selecionada.
2. Use as setas para baixo para localizar a linha que começa com `linux` (ou `linuxefi`). Esta linha contém o caminho do kernel e seus parâmetros de inicialização.
3. Nesta linha, localize e substitua o parâmetro `ro` (read-only) por `rw` (read-write).
4. No **final dessa mesma linha**, adicione o seguinte parâmetro para carregar o shell bash como o processo de inicialização principal:  
      
    `init=/bin/bash`  
    Exemplo de como ficará a linha modificada:
    
    > `linux /boot/vmlinuz-5.10.0-23-amd64 root=UUID=... rw quiet init=/bin/bash`

![image-1764956789240.png](../../../../../assets/images/p135_image-1764956789240.png)

### 3. Iniciar o Sistema e Alterar a Senha

1. Pressione `Ctrl+X` para iniciar o sistema com os novos parâmetros.
2. O sistema irá ignorar o processo de inicialização normal e carregar diretamente um *shell* como usuário *root* (indicado por `#`).
3. Execute o comando `passwd` para redefinir a senha do usuário *root*:
    
    ```shell
    passwd    
    ```
4. Digite a **nova senha** e confirme-a quando solicitado. Os caracteres não serão exibidos (comportamento padrão de segurança).
5. Uma mensagem como `password updated successfully` (senha atualizada com sucesso) confirmará a alteração.

### 4. Reinicializar o Sistema

1. Reinicie o sistema após alterar a senha. Use o comando `exec` para voltar ao processo de inicialização normal:
    
    ```shell
    exec /sbin/init 6
    ```
2. O Debian será reiniciado. No *prompt* de login, você poderá usar o nome de usuário `root` e a **nova senha** que acabou de definir.
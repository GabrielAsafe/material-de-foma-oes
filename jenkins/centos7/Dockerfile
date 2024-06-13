# Use a imagem base do CentOS 7
FROM centos:7

# Instale o servidor OpenSSH e HTTPD
RUN yum -y install openssh-server httpd

# Configure o Apache para escutar na porta 8081
RUN sed -i 's/Listen 80/Listen 8081/' /etc/httpd/conf/httpd.conf

# Crie um usuário e configure o diretório home e SSH
RUN useradd -m -d /home/remote_user -s /bin/bash remote_user && \
    echo "remote_user:1234" | chpasswd && \
    mkdir /home/remote_user/.ssh && \
    chmod 700 /home/remote_user/.ssh && \
    chown remote_user:remote_user /home/remote_user/.ssh

# Gere as chaves SSH do sistema
RUN ssh-keygen -A

# Permitir login sem senha para fins de teste (não recomendado para produção)
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config && \
    echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config

# Exponha a porta 22 para SSH e 8081 para o servidor web
EXPOSE 22 8081

# CMD para iniciar o SSH e o Apache como processos separados
CMD ["/bin/bash", "-c", "/usr/sbin/sshd -D && /usr/sbin/httpd -DFOREGROUND"]

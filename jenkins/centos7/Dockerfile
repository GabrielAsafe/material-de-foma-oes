# Use a imagem base do CentOS 7
FROM centos:7

# Instala o servidor OpenSSH e HTTPD
RUN yum -y install openssh-server httpd

# Instala utilitários necessários
RUN yum -y install \
    yum-utils \
    device-mapper-persistent-data \
    lvm2

# Adiciona o repositório do Docker CE
RUN yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

# Instala o Docker CE
RUN yum -y install docker-ce docker-ce-cli containerd.io

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

# Exponha a porta 22 para SSH, 8081 para o servidor web e 2375 para a API do Docker
EXPOSE 22 8081 2375

# CMD para iniciar o SSH, o Apache e o Docker como processos separados
CMD ["/bin/bash", "-c", "/usr/sbin/sshd -D && /usr/sbin/httpd -DFOREGROUND && /usr/bin/dockerd -H unix:///var/run/docker.sock"]

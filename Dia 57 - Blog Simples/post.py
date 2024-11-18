class Post:
    # O método construtor __init__ é chamado quando uma nova instância da classe Post é criada
    def __init__(self, post_id, title, subtitle, body):
        # Atribui o ID do post à propriedade 'id' do objeto
        self.id = post_id
        
        # Atribui o título do post à propriedade 'title' do objeto
        self.title = title
        
        # Atribui o subtítulo do post à propriedade 'subtitle' do objeto
        self.subtitle = subtitle
        
        # Atribui o corpo do post (o conteúdo principal) à propriedade 'body' do objeto
        self.body = body

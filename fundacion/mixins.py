class medicoMixin(object):
    def get_context_data(self, **kwargs):
        context = super(medicoMixin, self).get_context_data(**kwargs)
        return context
        
    # def get_citas(self):
    #     resultados = 
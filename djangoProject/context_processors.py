from trainer.models import Trainer


# context processors este o modalitate de a furniza date sau variabile catre paginile html. Contextul este un dictionar python care
# va contine elementele ce vor fi folosite in fisierele .html

# In concluze , context processors reprezinta o modalitate eficienta de a furniza date globale in pagini html

def get_all_trainers(request):
    get_trainers = Trainer.objects.all()
    return {'trainers': get_trainers}
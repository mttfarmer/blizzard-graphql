import graphene, getter

#Diablo 3
class Quest(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    slug = graphene.String()

class Act(graphene.ObjectType):
    slug = graphene.String()
    number = graphene.Int()
    name = graphene.String()
    quests = graphene.List(Quest)

class D3(graphene.ObjectType):
    act = graphene.Field(Act)
    allActs = graphene.List(Act)

    def resolve_allActs(parent,info):
        resp = getter.getD3Acts()
        acts = [Act(slug=item["slug"], number=item["number"], name=item["name"], quests=item["quests"]) for item in resp["acts"]]
        return acts
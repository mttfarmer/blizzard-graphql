from graphene import ObjectType, String, Schema, Field, String, Int, List
from graphene.relay import Node
import getter, models

class Query(ObjectType):
    quest = Field(models.Quest)
    act = Field(models.Act)
    d3 = Field(models.D3)

    def resolve_d3(parent, info):
        return models.D3()

    


schema = Schema(query=Query)

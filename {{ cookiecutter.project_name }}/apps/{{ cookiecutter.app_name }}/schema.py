import graphene


class Queries(graphene.ObjectType):
    pass


class Mutations(graphene.ObjectType):
    pass


schema = graphene.Schema(
    query=Queries,
    mutation=Mutations,
)

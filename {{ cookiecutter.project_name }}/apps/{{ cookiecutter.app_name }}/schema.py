import graphene

schema = graphene.Schema(
    query=Queries,
    mutation=Mutations,
)

from strawberry import Schema
from strawberry.fastapi import GraphQLRouter

from app.infrastructure.configs.environment import get_environment_variables

from app.infrastructure.configs.graph_ql import get_graphql_context
from app.infrastructure.schemas.graphql import Query, Mutation


env = get_environment_variables()
schema = Schema(query=Query, mutation=Mutation)
graphql = GraphQLRouter(
    schema,
    graphiql=env.DEBUG_MODE,
    context_getter=get_graphql_context,
)

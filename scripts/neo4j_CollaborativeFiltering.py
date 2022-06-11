from neo4j import GraphDatabase


class neo4jRun:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def createGraph(self):
        with self.driver.session() as session:
            result = session.run(
                "CALL gds.graph.create('userLikesEstablishment',['User','Establishment'],"
                "{likes: { } }  )"
            )
        print("Gds graph userLikesEstablishment is created...")
        return result

    def graphEmbedding(self):
        with self.driver.session() as session:
            result = session.run(
                "CALL gds.fastRP.mutate('userLikesEstablishment',"
                "{ embeddingDimension: 256,"
                "mutateProperty: 'embedding',"
                "iterationWeights: [0.8, 1, 1, 1] })"
                "YIELD nodePropertiesWritten"
            )
        print("Gds graph userLikesEstablishment is embedded...")
        return result

    def writeEmbedding(self):
        with self.driver.session() as session:
            result = session.run(
                "CALL gds.graph.writeNodeProperties('userLikesEstablishment', ['embedding'], ['User'])"
            )
        print(
            "Gds graph userLikesEstablishment's embedding result is written into original graph..."
        )
        return result

    def writeKNN(self):
        with self.driver.session() as session:
            result = session.run(
                "CALL gds.beta.knn.write('userLikesEstablishment', { "
                "   topK: 5, "
                "  nodeWeightProperty: 'embedding', "
                "   randomSeed: 42, "
                "  concurrency: 1, "
                "  sampleRate: 1.0, "
                " deltaThreshold: 0.0, "
                "   writeRelationshipType: 'SIMILAR', "
                "  writeProperty: 'similarityScore', "
                "   maxIterations:100 })"
                " YIELD nodesCompared, relationshipsWritten, similarityDistribution   "
                " RETURN nodesCompared, relationshipsWritten, similarityDistribution.mean as meanSimilarity   "
            )
        print("Finding the most 5 similar users via KNN method...")
        return result

    def userBasedRecommendation(self):
        session = self.driver.session()
        result = session.run(
            "MATCH (m:User)-[:likes]->(e1:Establishment) "
            "WITH m,COLLECT(e1) AS historyLikes "
            "MATCH (m)-[r:SIMILAR]->(n:User)-[:likes]->(e2:Establishment) "
            "WHERE NOT e2 IN historyLikes "
            "RETURN ID(m) as userId,COLLECT(DISTINCT e2.name) as recommendedEstablishments"
        )
        print("Output the results...")
        result_dict = {}
        for record in result:
            result_dict[record["userId"]] = record["recommendedEstablishments"]
        return result_dict

    def collaborativeFiltering(self):
        self.createGraph()
        self.graphEmbedding()
        self.writeEmbedding()
        self.writeKNN()
        result = self.userBasedRecommendation()
        return result


if __name__ == "__main__":
    neo4jrun = neo4jRun("bolt://localhost:7687", "neo4j", "sdm_pp")
    # neo4jrun.createGraph()
    # neo4jrun.graphEmbedding()
    # neo4jrun.writeEmbedding()
    # neo4jrun.writeKNN()
    print(neo4jrun.collaborativeFiltering())
    neo4jrun.close()

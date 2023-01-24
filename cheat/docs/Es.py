from docs.base import Base


class Es(Base):

    _doc = {
        "init": """
USER="elastic"
PASS="password"
URL="http://localhost:9200"
""",
    "index": """
curl -u "$USER:$PASS" -k "$URL/_cat/indices?v"
curl -u "$USER:$PASS" -k "$URL/$INDEX/_mapping"
curl -u "$USER:$PASS" -k "$URL/$INDEX/_search?size=10"
""",
    "cluster": """
curl -u "$USER:$PASS" -k "$URL/_cluster/health"
curl -u "$USER:$PASS" -k "$URL/_cluster/health?level=indices"
curl -u "$USER:$PASS" -k "$URL/_cat/shards"
curl -u "$USER:$PASS" -k "$URL/_cat/nodes"
""",
    }

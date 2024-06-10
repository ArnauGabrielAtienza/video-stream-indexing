# Milvus config
MILVUS_HOST = "localhost"
MILVUS_PORT = "19530"
MILVUS_NAMESPACE = "default"

# Pravega config
PRAVEGA_CONTROLLER = "172.28.1.1:9090"
PRAVEGA_SCOPE = "examples"

# Inference Logs
DO_LATENCY_LOG = True
DO_BATCH_LOG = False

# Path for all logs
LOG_PATH = "/project/results"
RESULT_PATH = "/project/results"

# Query params
QUERY_ACCURACY = 0.9

if __name__ == "__main__":
    """Print the environment variables for the shell scripts"""
    print(f"export MILVUS_HOST={MILVUS_HOST}")
    print(f"export MILVUS_PORT={MILVUS_PORT}")
    print(f"export MILVUS_NAMESPACE={MILVUS_NAMESPACE}")
    print(f"export PRAVEGA_CONTROLLER={PRAVEGA_CONTROLLER}")
    print(f"export PRAVEGA_SCOPE={PRAVEGA_SCOPE}")
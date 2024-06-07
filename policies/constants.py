MILVUS_HOST = "localhost"
MILVUS_PORT = "19530"
MILVUS_NAMESPACE = "default"

PRAVEGA_CONTROLLER = "172.28.1.1:9090"
PRAVEGA_SCOPE = "examples"

DO_LATENCY_LOG = True
DO_BATCH_LOG = False

if __name__ == "__main__":
    """Print the environment variables for the shell scripts"""
    print(f"export MILVUS_HOST={MILVUS_HOST}")
    print(f"export MILVUS_PORT={MILVUS_PORT}")
    print(f"export MILVUS_NAMESPACE={MILVUS_NAMESPACE}")
    print(f"export PRAVEGA_CONTROLLER={PRAVEGA_CONTROLLER}")
    print(f"export PRAVEGA_SCOPE={PRAVEGA_SCOPE}")